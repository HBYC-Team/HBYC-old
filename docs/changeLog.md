# HBYC ChangeLog
This docs is use ENGLISH only, do not use translate.

Or you may got wrong understanding.

# v0.0.1
Release date:2022.06.08

## app.py
* Add the main program.
* Load/Unload/Reload commands.

## /core
* Add `__init__`

## Fast-Install Packages
* Add Batch file to ./bat
* Add Shell Script to ./sh

## /cmds
Add the commands.

* chat.py - Add say/repeat/thinking commands
* evenit.py - Add some event of the bot
* help.py - Add help commands
* music.py  - Add join/play/pause/resume/stop/leave commands(volume/now command is still in fix)
* game - This file will be .py file which will add more commands in future versions

# v0.0.2
Release date:2022.06.13.

## app.py
* Load/Unload/Reload commands if you don't have password then you can't use these commands.
* Print bot in what the guilds.Use `for guild in client.guilds`

## /cmds
Add and remove some commands.

* chat.py - Fixed say command + Add more emojis to thinking command.
* event.py - Add react when the bot got mentioned.
* help.py - typo.
* music.py  - Remove volume/now command + Fixed join command.
* user.py - Add avatar command.

## game
The `guessnum` command will out soon.

## 2022.6.17
v0.0.2 bug fixes-
* app.py
* chat.py
* event.py
* help.py
* music.py

# v0.0.3
Release date:2022.06.21

## app.py
Removed the rich presence at the start.

## /cmds
* chat.py - Added timestamp to print.
* event.py - Added some little event.
* help.py - Changed the embed + Added field of `report` command + Added timestamp to print.
* music.py - Added timestamp to print.
* user.py - Added `report`, `presence`, `ping` commands + Added timestamp to print.

# v0.0.4
Release date:

## app.py
Added the message command.

## /cmds
* chat.py - Added the message command. + Bug fixes.
* event.py - Bug fixes + Changed some event.
* help.py - Added the message command. + Bug fixes.
* music.py - Added the message command. + Bug fixes.
* user.py - Added the message command. + Bug fixes. + Added announcement command.

## end
