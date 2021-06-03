cd ./video/median
python3 run.py
cd ../..
sleep 5
cd ./video/net
python3 run.py
cd ../..
sleep 5
cd ./video/tail/
python3 run.py
cd ../..
sleep 5
echo video

cd ./statelesscost/median
python3 run.py
cd ../..
sleep 5
cd ./statelesscost/net 
python3 run.py
cd ../..
sleep 5
cd ./statelesscost/tail/
python3 run.py
cd ../..
sleep 5
echo statelesscost


cd ./sort/median
python3 run.py
cd ../..
sleep 5
cd ./sort/net 
python3 run.py
cd ../..
sleep 5
cd ./sort/tail/
python3 run.py
cd ../..
sleep 5
echo sort

