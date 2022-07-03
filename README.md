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
Windows使用者可以直接運行`build.bat` 進行配置。
</br>

Linux, Mac使用者可以直接運行`build.sh` 進行配置。（請記得將運行此script的權限開啟）
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
我也是藉此而精進自己，像是Python的基本操作都是從模組上去學，也趁機學點基本shell script。

## 專案包含
* 純pycord達成簡易的許多功能
* 達成以pycord部署斜線指令及訊息指令
* 簡易的音樂指令
* 簡易的遊戲指令（預計將在之後的版本開始開發）
* Cog實例
* 以core的方式定義__init__
* 簡易聊天指令

## 指令列表
請見[指令列表](./docs/command_list.md)檔案。

## 授權方式
請見[LICENSE](./LICENSE)檔案。

## 相依性套件
請見[requirements.txt](./requirements.txt)檔案。

## 更新日誌
請見[更新日誌](./docs/changeLog.md)檔案(EN-Only)。

## 作者
恐龍#2549/hugocoding。

有關於其他問題可以使用Discord聯絡或是加入作者正在建立中的[程式伺服器](https://discord.gg/J7X2nWXszp)。
