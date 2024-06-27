# Setup Flask Project

## create venv
```sh
python3 -m venv .venv
```
or 
```sh
uv venv
```

## Activate venv
```sh
source .venv/bin/activate (for linux)
```
or
```sh
.\venv\Scripts\activate (for Windows)
```


## Run
```sh
pip install -r requirements.txt
```
or
```sh
uv pip install -r requirements.txt
```

## start dev server
```sh
python3 -m flask run --reload
```

## start wsgi server (Production)
```sh
python3 wsgi.py (for unix)
```
or
```sh
python wsgi.py (for windows)
```