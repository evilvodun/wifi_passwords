## Steal wifi saved windows passwords with Flipper Zero 

### Installation

```bash
git clone https://github.com/FlaviusMosneagu/wifi_passwords.git
cd wifi_passwords
python -m venv env
source ./env/bin/activate
pip install -r requirements
```

### Start the Dashboard
```bash
python main.py
```

On `/static` route it is a basic dashboard to list all the wifis captured by flipper zero.  
Also take a look at the `routes` in `main.py` to see all available endpoints.
