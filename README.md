# ROS_janken
ROSを用いてcpとジャンケンを行い結果を表示するプログラムを作成した。

#janken.py  
-実行方法：$ rosrun mypkg janken.py
-実行すると
-"三つから選んでください　グー(0) チョキ(1) パー(2) :"
-と表示され、入力された数字がデータとしてjudg.pyに渡される。

#judg.py
実行方法：$ rosrun mypkg judg.py
実行するとシステムが出す手を乱数から決め、janken.pyから渡されたデータと比較して勝敗を決定し、
出した手と勝ち負けが表示される。また、janken.pyの際に0,1,2,以外の数字が入力された際には"retray"
が表示される。
