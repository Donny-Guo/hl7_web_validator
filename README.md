# hl7_web_validator

hl7_web_validator is a web-based validator for HL7 V2 messages according to HL7 specifications. In particular, this validator is designed for CDPH HL7 specifications.

- This is a fork of [hl7apy](https://github.com/crs4/hl7apy) and modified to meet the 2024 CDPH (California Department of Public Health) HL7 specifications.

- This web validator is based on [Flask framework](https://github.com/pallets/flask).



## Installation

Get its latest release by the following command:

```
git clone https://github.com/Donny-Guo/hl7_web_validator.git
```

Set up python virtual environment:

```
python -m venv env
```

Activate virtual environment env:

```
# Windows
.\env\Scripts\Activate.ps1

# Linux/Mac
source env/bin/activate
```

To install it by the following command:

```
pip install .
```

To run it:

```
# Windows
python .\flask\app.py

# Linux/Mac
python flask/app.py
```

The above command will open up a browser window at `127.0.0.1:5000` (You can configure this in "flask/app.py"). Press CTRL+C to quit the app.

You can also choose to use development server (werkzeug) or production server (waitress). Just comment out either one of the lines in "flask/app.py".

```python
# app.run(host=host, port=port) # use dev server
serve(app, host=host, port=port) # use prod server
```



## Package
To package all files to one executable, [pyinstaller](https://github.com/pyinstaller/pyinstaller) is used in this project. Be sure to read [this](https://pyinstaller.org/en/stable/operating-mode.html) to understand the limitation of pyinstaller.
To package it:


```
# dev server
pyinstaller --onefile --hidden-import werkzeug --add-data ".\flask\templates:templates" --add-data "hl7apy:hl7apy" flask\app.py

# prod server
pyinstaller --onefile --hidden-import waitress --add-data ".\flask\templates:templates" --add-data "hl7apy:hl7apy" .\flask\app.py
```