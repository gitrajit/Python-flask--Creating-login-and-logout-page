# Python-Flask - Login and logout of a webpage.

This is an example to show how we can use Flask framework for creating a webpage.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* Python 3.7 or later
* Flask 0.11.1 or later
* sqlite3
```

import base64
from flask import *
from functools import wraps


```


### Installing

Need to Install Python and pip.

For unix

```
apt-get python
apt-get pip

yum install python
yum install python
```
Once pip installed , you can use pip to install flask and others packages

```
pip install flask

```

You can also put all the packages in requirement.txt and install all at once.

```
pip install -r requirements.txt

```

for window users

1. From https://www.python.org/downloads download appropriate Python 3.X Windows Installer. (If that link doesn't work, check https://www.python.org/downloads/)
Run the file
2. Select install for all users or install just for me, click Next
3. You'll see it installs under the C:\Python27 folder, click Next
4 .Click Next again for the 'Customize Python' step
5. Click Finish
6. Open Control Panel, then System
7. Click 'Advanced system settings' on the left
8. Click the 'Environment Variables' button
9. Under 'System variables' click the variable called 'Path' then the 'Edit...' button. (This will set it for all users, you could instead choose to edit the User variables to just set python as a command prompt command for the current user)
10. Without deleting any other text, add C:\Python; (include the semi-colon) to the beginning of the 'Variable value' and click OK.
11. Click OK on the 'Environment Variables' window.
12. Open a new command prompt window type python, you will have python running in the command prompt. Note: command prompt windows open prior to setting the Environment Variable will not have the python command available.

open Command prompt as **Administrator**

C:\Python\Scripts>

```
C:\Python\Scripts>pip -r requirements.txt

```

End with an example of getting some data out of the system or using it for a little demo

## Running the webpage

Run the main python file to start.

```
C:\Python\python.exe login_logout.py
 * Running on http://127.0.0.1:10/ (Press CTRL+C to quit)
 
 ```
