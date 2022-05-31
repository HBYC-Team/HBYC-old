# HBYC
一個非常簡易的discord機器人，使用pycord模組編寫。

## 如何做一台跟這台一樣的機器人
自己fork這份專案或抓source code回去。
</br>

取得source code的方式可以在Release的區塊找到。

## 如何讓機器人上線
```bash
$ python app.py
```
Windows使用者可以直接運行`/bat/run.bat`使機器人上線，若要自動裝相依性套件可以直接使用`/bat/install.bat`
</br>

Linux, Mac使用者可以直接運行`/sh/run.sh`使機器人上線，若要自動安裝相依性套件可以直接使用`/sh/install.sh`
</br>

切記將`config.json`裡面的`token`欄位填上你自己的token,並將`app.py`的
```py
token = os.getenv()
```
刪除，並將
```py
if __name__ == "__main__":
    client.run(token)
```
改成
```py
if __name__ == "__main__":
    client.run(conf["token"])
```
或者你會env的話也可以自己弄。

## 授權方式
請見LICENSE檔案。

## 相依性套件
請見requirements.txt。

## 作者
恐龍#2549/hugocoding