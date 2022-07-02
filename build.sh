#!/bin/sh

echo "--install: Install the dependencies."
echo "--start: Run the bot."
echo "Please Enter \"--install\" or \"--start\" "
read todo

if [ $todo = "--install" ]
then
	python3 -m pip install -r requirements.txt
elif [ $todo = "--start" ] 
then
	python3 app.py
else
	echo "Please Enter the true argument."
	return
fi