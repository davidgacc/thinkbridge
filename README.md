### Make enviroment ###

In linux:
```
pyenv shell 3.9.5 && python -m venv .venv && source .venv/bin/activate
```
or Windows:
```
pyenv shell 3.9.5 && python -m venv .venv && source .venv/Scripts/activate
```

Install packages:

```
pip install -U pip setuptools
pip install -r requirements.txt
```

### Run ###

```
python main.py path/to/csv_companies.csv path/to/output_csv.csv
```