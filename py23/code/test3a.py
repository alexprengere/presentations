
from typing import Iterator

def fib(n: int) -> Iterator[str]:
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

print(list(fib(5)))
