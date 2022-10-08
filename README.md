# UI-Suite
It's a Robot Framework task for checking UI-interface

```bash
.
├── ChromeLib.py
├── keywords.resource     <====
├── Locators
│   └── PageElements.py
├── log.html
├── output.xml
├── pyproject.toml
├── report.html
├── requirements.txt
├── setup.py
├── tox.ini
└── UI-test.robot
```
You can set the current chromedriver version and a server path using ***keywords.resource*** file:

Just set the chromedriver version to **latest** if you are using the latest version of chrome.

```bash

***Settings***
Documentation    Please select the server path:port as a first parameter and
...              a chromedriver version as a second argument

Library    ChromeLib.py    http://127.0.0.1:6969    90.0.4430.24

*** Variables ***
```


# How to start
Each project uses a tox management tool to create an isolated environment.
First, you must to install the packages from **requirements.txt** in a root directory.

To start the tests, just go to the appropriate directory and run:
```bash
python3 -m tox
```

For Example:
```bash
paul@C0FFEE:~/ROBOTEST/tests/UI_Suite$ python3 -m tox
py37 create: /home/paul/ROBOTEST/tests/UI_Suite/.tox/py37
py37 installdeps: -r/home/paul/ROBOTEST/tests/UI_Suite/requirements.txt
py37 installed: async-generator==1.10,attrs==22.1.0,certifi==2022.9.24,charset-normalizer==2.1.1,distlib==0.3.6,exceptiongroup==1.0.0rc9,filelock==3.8.0,h11==0.14.0,idna==3.4,importlib-metadata==5.0.0,outcome==1.2.0,packaging==21.3,platformdirs==2.5.2,pluggy==1.0.0,py==1.11.0,pyparsing==3.0.9,PySocks==1.7.1,python-dotenv==0.21.0,requests==2.28.1,robotframework==5.0.1,selenium==4.5.0,six==1.16.0,sniffio==1.3.0,sortedcontainers==2.4.0,toml==0.10.2,tox==3.25.1,tqdm==4.64.1,trio==0.22.0,trio-websocket==0.9.2,typing_extensions==4.4.0,urllib3==1.26.12,virtualenv==20.16.5,webdriver-manager==3.8.3,wsproto==1.2.0,zipp==3.8.1
py37 run-test-pre: PYTHONHASHSEED='2739644563'
py37 run-test: commands[0] | robot UI-test.robot
==============================================================================
UI-test
==============================================================================
...
_________________________________________________________________________________ summary __________________________________________________________________________________
  py37: commands succeeded
  congratulations :)
```
