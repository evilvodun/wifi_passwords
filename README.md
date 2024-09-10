# Steal wifi saved windows passwords with Flipper Zero

![version](https://img.shields.io/badge/version-1.0.0-blue)
[![GPL-3 License](https://img.shields.io/badge/license-GPLv3-green)](https://choosealicense.com/licenses/gpl-3.0/)


**Table of Contents**

- [Installation](#installation)
- [Execution / Usage](#execution--usage)
- [Technologies](#technologies)
- [Features](#features)
- [License](#license)

## Installation

```bash
git clone https://github.com/FlaviusMosneagu/wifi_passwords.git
cd wifi_passwords
python -m venv env
source ./env/bin/activate
pip install -r requirements
```

### Execution / Usage

```bash
python main.py
```

On `/static` route it is a basic dashboard to list all the wifis captured by flipper zero.  
Also take a look at the `routes` in `main.py` to see all available endpoints.

## Technologies

**Steal wifi saved windows passwords with Flipper Zero** uses the following technologies and tools:

- [Python](https://www.python.org/): ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
- [SQLite](https://sqlite.org/): ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
- [FastAPI](https://fastapi.tiangolo.com/): ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi&logoColor=ffdd54)

## Features

**Steal wifi saved windows passwords with Flipper Zero** currently has the following set of features:

- Windows compatible through powershell script
- Linux support is *work in progress*

## License

**Steal wifi saved windows passwords with Flipper Zero** is distributed under the GPL-3.0 license. See [`LICENSE`](LICENSE.md) for more details.