#Copyright(C) dragonyc1002
@echo off

echo "--install: Install the dependencies."
echo "--start: Run the bot."

SET /P todo="Please Enter \"--install\" or \"--start\" "

if %todo% == "--install" (
	echo "Install the dependencies..."
	python3 -m pip install -r requirements.txt
) else if %todo% == "--start" (
	echo "Start the bot..."
	python3 app.py
) else (
	echo "Please Enter a true argument."
	return
)

