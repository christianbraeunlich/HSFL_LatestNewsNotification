# HSFL_LatestNewsNotification

> Our university of applied sciences doesn't inform us of the latest news or the announcement of grades. This is where we come in!

## Features

* [Latest News](https://hs-flensburg.de/hochschule/aktuelles) 
* [Latest Grades](https://hs-flensburg.de/hochschule/pruefungsmanagement/notenaushaenge) 

## Telegram Channels

| News     	| referral link                                         	| enabled               |
|-----------------------	|-------------------------------------------------------	|-------------------	|
| | | |
| Aktuelle Neuigkeiten    	| [HSFL News](https://t.me/joinchat/AAAAAFc_lsnfWrpeiC1qYg) 	    | :heavy_check_mark:   	|

<br>

| course of studies     	| referral link                                         	| enabled               |
|-----------------------	|-------------------------------------------------------	|-------------------	|
| | | |
| Maschinenbau    	| [Notenaushang MB](https://t.me/joinchat/AAAAAFc_lsnfWrpeiC1qYg) 	    | :heavy_check_mark:   	|
| Schiffsbautechnik 	| [Notenaushang SBT](https://t.me/joinchat/AAAAAE7fyckec7dWnfLOcA) 	    | :heavy_check_mark:    |
| Schiffsmotorbau 	| [Notenaushang SMB](https://t.me/joinchat/AAAAAEXT3FoxZScH9-tbkQ) 	    | :heavy_check_mark:    |
| Seeverkehr, Nautik und Logistik 	| [Notenaushang SNL](https://t.me/joinchat/AAAAAEaZouCDskZ6I3MHNg) 	    | :heavy_check_mark:    |
| Biotechnology and Process Engineering 	| [Notenaushang BTPE](https://t.me/joinchat/AAAAAEaL-2ex1tl01G8IvQ) 	    | :heavy_check_mark:    |
| Systemtechnik 	| [Notenaushang ST](https://t.me/joinchat/AAAAAEeCh9t7ggV-J72WWA) 	    | :heavy_check_mark:    |
| | | |
| Bio-, Lebensmittel- und Verfahrenstechnologie 	| [Notenaushang BLVT](https://t.me/joinchat/AAAAAFVhiwJsol18Ydsjjg) 	    | :heavy_check_mark:    |
| Biotechnologie-Verfahrenstechnik 	| [Notenaushang BVT](https://t.me/joinchat/AAAAAENC1sRwF7riSgZADQ) 	    | :x:    |
| Energiewissenschaften 	| [Notenaushang EW](https://t.me/joinchat/AAAAAFaastXV0beunrXusg) 	    | :x:    |
| | | |
| Applied Bio and Food Sciences 	|               |     |
| Automatisierungstechnik 	|                	    |     |
| Wind Engineering 	| [Notenaushang WE](https://t.me/joinchat/AAAAAFkB5NBpKr49V95Scg) 	    | :heavy_check_mark:    |
| | | |
| Angewandte Informatik   	| [Notenaushang AI](https://t.me/joinchat/AAAAAEsonoQ-cTNMtJzF-Q) 	    | :x:    |
| Internationale Fachkommunikation   	| [Notenaushang IFK](https://t.me/joinchat/AAAAAFiVLB7akYZH0co4dA) 	    | :heavy_check_mark:    |
| Medieninformatik   	| [Notenaushang MI](https://t.me/joinchat/AAAAAEYK2OmFKMGJmRKg-A) 	    | :heavy_check_mark:    |
| Intermedia & Marketing   	|  	    |           |
| | | |
| Betriebswirtschaft   	| [Notenaushang BW](https://t.me/joinchat/AAAAAESd1cCXYWO4LeAANA) 	    | :heavy_check_mark:    |
| Wirtschaftsinformatik   	| [Notenaushang WI](https://t.me/joinchat/AAAAAFZZgCVhiJO6adiNHg) 	    | :heavy_check_mark:    |
| Business Management   	| [Notenaushang BM](https://t.me/joinchat/AAAAAFdpMMJv7EA6Xiv3rw) 	    | :heavy_check_mark:    |
| eHealth   	|  	    |       |

> **_NOTE:_**  verbal re-examination excluded

## Release History

* 0.4
    * ADD: latest News to telegram channel
    * CHANGE: [telegram.ext.JobQueue](https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.jobqueue.html) instead of os.system()
    * ADD: control panel to change crawling behavior
* 0.3
    * ADD: broadcast all exams for business informatics to the telegram channel
    * CHANGE: exclude token from online-version
    * CHANGE: output format of the bot-messages
    * CHANGE: hsfl_lnn.db includes columns to save ```course_study``` and ```course_study_id``` attributes
    * CHANGE: spider crawles the mentioned attributes into the database
* 0.2
    * CHANGE: [telegram-python-bot 12.3.0](https://python-telegram-bot.readthedocs.io/en/stable/changelog.html#version-12-3-0) 
    * ADD: Recursive function from base url to all the other courses
* 0.1
    * The first proper release
    * FEATURE: News Notification
    * FEATURE: Grades Notification

# Installation

## Raspberry-Pi

```
sudo raspi-config
sudo reboot
sudo apt-get update
sudo apt-get -d upgrade
sudo apt-get -y upgrade
sudo reboot
sudo rpi-update
sudo reboot

" Disable Bluetooth
sudo systemctl disable hciuart.service
```

## Change the Python default version to 3.x
```
ls -lh /usr/bin/python3 /usr/bin/python
# lrwxrwxrwx 1 root root /usr/bin/python -> python2.7
# lrwxrwxrwx 1 root root /usr/bin/python3 -> python3.7

mv /usr/bin/python /usr/bin/python.bak
cp /usr/bin/python3 /usr/bin/python
python --version
# Python 3.7.x
```

## Install HSFL-LatestNewsNotification
```
# Dependecies for scrapy
sudo apt-get install libffi-dev
sudo apt-get install libxml2-dev
sudo apt-get install libxslt1-dev
sudo apt-get install libssl-dev
sudo apt-get install python3-dev

sudo apt-get install python3-distutils
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py

# Testing with Pytest
pip install pytest

# prebuild lxml library - much faster installation
sudo apt install python3-lxml
sudo pip install scrapy
pip -vvvv install --upgrade pyOpenSSL

# Python Telegram Bot Library
sudo pip install python-telegram-bot

# Git to clone the latest version of HSFL_LNN
sudo apt-get install git
git clone https://github.com/OtterWhisperer/HSFL_LatestNewsNotification

# setup the sqlite3 database
python setup_sqlite3.py
```

## Bot-Configuration

```
File: ./HSFL_LNN/bot_config.py

BOT_TOKEN = 'INSERT YOUR BOT TOKEN HERE'    <-- add your bot-token here

BOT_ADMINS = []                             <-- add your chat_id here
```

## Starting the service on the raspberry pi

```
sudo cp hsfl_lnn.service /etc/systemd/system/hsfl_lnn.service
sudo chmod 644 /etc/systemd/system/hsfl_lnn.service
sudo chmod 775 /home/pi/HSFL_LatestNewsNotification/HSFL_LNN_BOT.py
sudo systemctl daemon-reload
sudo systemctl enable hsfl_lnn.service
sudo systemctl start hsfl_lnn.service
```

# Contributing to this project

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
