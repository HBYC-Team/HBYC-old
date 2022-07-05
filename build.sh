#########################################
#**********HBYC Bot Build File**********#
#**Type: Shell Script~for Linux, MacOS**#
#**********Author: dragonyc1002*********#
#********Release Date:2022.07.05********#
#*************Version: 0.0.5************#
#*********Lisence: BSD 3-Clause*********#
#########################################

#!/bin/sh
echo "Choose Language: EN or ZH-TW."
read lang

if [ $lang = "EN" ]
then
	echo ">>install: Install the dependencies."
	echo ">>start: Run the bot."
	echo "Please Enter \"install\" or \"start\" "
	read todo

	if [ $todo = "install" ]
	then
		python3 -m pip install -r requirements.txt
	elif [ $todo = "start" ] 
	then
		python3 app.py
	else
		echo "Please Enter a true argument."
		return
	fi

elif [ $lang = "ZH-TW" ]
then
	echo ">>install:安裝依賴項（請先確認已經安裝Python3）。"
	echo ">>start:讓機器人上線（請先確認已經填入token）。"
	echo "請輸入\"install\" 或 \"start\"。"
	read script

	if [ $script = "install" ]
	then
		python3 -m pip install -r requirements.txt
	elif [ $script = "start" ]
	then
		python3 app.py
	else
		echo "請輸入正確的參數。"
		return
	fi
else
	echo "Please Enter EN or ZH-TW."
	return

fi