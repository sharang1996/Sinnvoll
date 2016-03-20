#!/bin/sh

user1=`python signin.py`
echo "$user1" >> data2.txt
user2=`python signin.py`
echo "$user2" >> data2.txt
if [ "$user1" == "death_stalker" and "$user" == "ashish" ]
then
	python admin.py
    javac BinarySearchTree.java
    java BinarySearchTree
else
	ch=0
	while [ "$ch" -ne "4" ]
	do
		echo "enter 1 for blackJack , 2 for file splitter , 3 for TextEditor and 4 to exit"
		read ch
		if [ "$ch" -eq "1" ]
		then
			javac Game.java
			java Game >> data2.txt
		elif [ "$ch" -eq "2" ]
		then
			python splitter.py
		elif [ "$ch" -eq "3" ] 
		then
			python texteditor.py
		fi
	done
fi
