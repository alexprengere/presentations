
This is the doc

```python
>>> from aggregate import aggregate
>>>
>>> with open('flights.csv') as f:
...     data = aggregate(f)
>>> data['CDG']
8.0
>>> data['ORY']
1.0

```
