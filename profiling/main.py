import sys
from datetime import datetime

from collections import Counter


def main():
    stats = Counter()
    for row in open(sys.argv[1]):
        row = row.strip().split(",")
        d = row[2]
        datetime.strptime(d, "%Y-%m-%d")
        stats[d] += 1

    return stats


print(main())
