from datetime import date, timedelta
import random
import string

from neobase import NeoBase

G = NeoBase()
keys = list(G)

TODAY = date.today()
DAY = timedelta(days=1)

if __name__ == "__main__":
    import sys

    N = int(sys.argv[1])
    n = 0
    while n < N:
        n += 1
        origin_key, destin_key = random.sample(keys, 2)
        adv = random.randint(0, 365)
        stay = random.randint(0, 10)
        base_amount = random.choice([734.41, 754.41, 777.87, 802.25])
        taxes = random.uniform(10, 20)
        price = base_amount + taxes

        origin = G.get(origin_key, "iata_code")
        destin = G.get(destin_key, "iata_code")
        dep_date = TODAY + adv * DAY
        ret_date = TODAY + (adv + stay) * DAY

        carf = "".join(random.choice(string.ascii_lowercase) for _ in range(16))
        print(
            "{},{},{},{},{},{},{}".format(
                origin, destin, dep_date, ret_date, price, taxes, carf
            )
        )
