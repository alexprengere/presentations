# Different ways of testing

Setup:

```
virtualenv .env -p py39
source .env/bin/activate
pip install -r requirements.txt
```

Run the tests:

```
py.test -v
py.test --cov --cov-report term-missing
py.test --hypothesis-show-statistics
py.test --gherkin-terminal-reporter
```

Run `mutmut` to test the tests:

```
mutmut run --paths-to-mutate module.py
```
