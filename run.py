import boto3
import paramiko
import threading,time,shlex
from subprocess import DEVNULL, STDOUT, check_call
import subprocess as sp
import shlex
import os, glob
import sys
import shutil
import statistics
FNULL = open(os.devnull, 'w')

def run_lam(nj, parallel):
    num=int(nj/parallel)
    i=1
    pro_list=[]
    start_time=time.time()
    while i <=num:
        command= "aws lambda invoke --function-name scaling_test_fft --payload \'{\"key1\":\""+str(parallel)+"\"}\' response" +str(i)+".txt"
        p=sp.Popen(shlex.split(command),stdout=FNULL )
        pro_list.append(p)
        i+=1
    scaling_time=time.time()-start_time
    for p in pro_list:
        while (1):
            poll = p.poll()
            if poll == None:
                    continue
            else:
                    break                   
    filenames=["response"+str(i+1)+".txt" for i in range(num)]
    with open('response.txt', 'w') as outfile:
        for fname in filenames:
            try:
                with open(fname) as infile:
                        outfile.write(infile.read())
                        outfile.write("\n")
            except:
                pass

    for file in filenames:
            try:
                    command="sudo rm "
                    command+=file+" "
                    sp.check_output(shlex.split(command))
            except:
                    pass           
    print("scaling time is ", scaling_time)
    print ("service time is ", time.time()-start_time)

run_lam(3000,2)
