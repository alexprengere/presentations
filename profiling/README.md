# Profilers

## Line profiler

```
pip install line_profiler
# Then add “@profile” to the functions you want to profile
kernprof --line-by-line --view main.py data
```

## Memory profiler

```
pip install memory_profiler
# Then add “@profile” to the functions you want to profile
python -m memory_profiler main.py data
```

## Py-spy

```
pip install py-spy
py-spy record -o profile.svg -- python main.py data
```

## Memray

```
pip install memray
memray run -o output.bin main.py data
memray flamegraph output.bin
```

### IPython

```
%timeit parse_date('2011-11-11')
```
