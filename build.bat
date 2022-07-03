@echo off

SET /P lang="Choose a Language: EN or ZH-TW"

if %lang% == "EN" (
	echo ">>install: Install the dependencies."
	echo ">>start: Run the bot."

	SET /P todo="Please Enter \"install\" or \"start\" "

	if %todo% == "install" (
		echo "Install the dependencies..."
		python3 -m pip install -r requirements.txt
	) else if %todo% == "start" (
		echo "Start the bot..."
		python3 app.py
	) else (
		echo "Please Enter a true argument."
		return
	)

) else if %lang% == "ZH-TW" (
	echo ">>install: 安裝依賴項（請先確認已經安裝Python3）"
	echo ">>start: 使機器人上線（請先確認已經填入token）"

	SET /P todo="請輸入 \"install\" 或 \"start\" "

	if %todo% == "install" (
		echo "安裝依賴項..."
		python3 -m pip install -r requirements.txt
	) else if %todo% == "start" (
		echo "執行機器人..."
		python3 app.py
	) else (
		echo "請填入正確的參數"
		return
	)
) else (
	echo "Please Enter EN or ZH-TW."
	return
)