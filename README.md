# HBYC
![license](https://img.shields.io/github/license/hugocoding/HBYC)
![last_commit](https://img.shields.io/github/last-commit/hugocoding/HBYC)
![Discord](https://img.shields.io/discord/977204156043509780)
[![EMU900!!!](./public/images/banner.jpeg)](https://reurl.cc/GxQqdy)

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
或者你會env的話也可以自己建檔設定token。

## 專案特色
其實沒什麼特色，就是最簡單的code而已。

## 專案包含
* 純pycord達成簡易的許多功能
* 達成以pycord部署簡易斜線指令
* 簡易的音樂功能
* 簡易的遊戲功能（預計將在v0.0.2開始開發）
* Cog實例
* 以core的方式定義__init__
* 簡易聊天功能

## 授權方式
請見LICENSE檔案。

## 相依性套件
請見requirements.txt。

## 作者
恐龍#2549/hugocoding。
</br>

有關於其他問題可以使用Discord聯絡或是加入作者正在建立中的[程式伺服器](https://discord.gg/J7X2nWXszp)。