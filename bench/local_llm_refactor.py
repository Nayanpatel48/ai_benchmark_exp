# more algorithmic change but introduces helper overhead (simulate slower complex change)
import random
from functools import lru_cache

def generate_data(n=2000):
    return [{"id": i, "value": random.randint(0, 100)} for i in range(n)]

@lru_cache(maxsize=None)
def helper(ids_tuple, values_tuple):
    # simulate complex helper that is expensive to construct
    return sum(v for v in values_tuple if v > 90)

def process_data(n=2000):
    data = generate_data(n)
    ids = tuple(d["id"] for d in data)
    vals = tuple(d["value"] for d in data)
    hot = helper(ids, vals)
    out = []
    for item in data:
        # rebuild/transform inside loop to simulate overhead
        transformed = [{"k": d["id"], "v": d["value"]} for d in data]
        s = 0
        for o in transformed:
            if o["k"] == item["id"] + 1:
                s += o["v"]
        if s or hot:
            out.append((item["id"], s + hot))
    return out

if __name__ == "__main__":
    process_data()
