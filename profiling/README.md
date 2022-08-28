# Different ways of testing

## Line profiler

```
pip install line_profiler
# Then add “@profile” to the functions you want to profile
cat data | kernprof --line-by-line --view main.py
```

## Memory profiler

```
pip install memory_profiler
# Then add “@profile” to the functions you want to profile
cat data | python -m memory_profiler main.py
```

## VMProf

```
pip install vmprof
# You need to set up the backend on 0.0.0.0:8000
cat data | python -m vmprof --web --web-url 0.0.0.0:8000 main.py
cat data | python -m vmprof --web --web-url --mem 0.0.0.0:8000 main.py
```

## Py-spy

```
# First find the PID, then
py-spy --pid 26234 --flame main.svg
```

### IPython

```
%timeit parse_date('2011-11-11')
```
