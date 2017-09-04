# Python-Flask - Login and logout of a webpage

This is an example to show how we can use Flask framework for creating a webpage.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* Python 2.7 or later
* Flask 0.11.1 or later
* functools any versions
* MySQLdb 1.2.5 or later
```

import base64
from flask import *
import os
from datetime import datetime
from functools import wraps

import MySQLdb

```
