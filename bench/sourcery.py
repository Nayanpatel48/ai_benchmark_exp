# refactor using dict mapping and comprehensions (expected faster)
import random

def generate_data(n=2000):
    return [{"id": i, "value": random.randint(0, 100)} for i in range(n)]

def process_data(n=2000):
    data = generate_data(n)
    id_map = {d["id"]: d for d in data}   # single pass mapping
    hot_values = [d["value"] for d in data if d["value"] > 90]
    out = [(item["id"], id_map.get(item["id"]+1, {}).get("value", 0) + sum(hot_values))
           for item in data if (id_map.get(item["id"]+1) or hot_values)]
    return out

if __name__ == "__main__":
    process_data()
