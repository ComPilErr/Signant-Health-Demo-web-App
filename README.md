# Look for more
https://github.com/sh-rdtaci/Flasky

# UI_Suite
It's a Robot Framework task for checking the UI-interface.

You can set the current chromedriver version and a server path using ***keywords.resource*** file:

```bash

***Settings***
Documentation    Please select the server path:port as a first parameter and
...              a chromedriver version as a second argument

Library    ChromeLib.py    http://127.0.0.1:6969    90.0.4430.24    <==

*** Variables ***
```
Just set the chromedriver version to **latest** if you are using the latest version of chrome.

# API_Suite
It's a Python API task.
Mainly it uses a **requests** library for make an API queries and a pytest as a shell-framework.

You can set the server path option in **conftest.py** configuration file:
```bash
@pytest.fixture(scope="function")
def point():
    check = api_connector("http://127.0.0.1:6969")   <==
    yield check

```

# How to start
Each project uses a **tox** management tool to create an isolated environment.
First, you must to install this package from the **requirements.txt** in a root directory.

To start the tests, just go to the appropriate directory and run:
```bash
python3 -m tox
```
