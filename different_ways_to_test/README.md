# Different ways of testing

Setup:

```
virtualenv .env -p py39
source .env/bin/activate
pip install -r requirements.txt
```

Run the tests:

```
pytest -v
pytest --cov --cov-report term-missing
pytest --hypothesis-show-statistics
pytest --gherkin-terminal-reporter
```

Run `mutmut` to test the tests:

```
mutmut run --paths-to-mutate module.py
```
