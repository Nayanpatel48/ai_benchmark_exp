# generator-based approach to reduce intermediate memory allocations
import random

def generate_data(n=2000):
    for i in range(n):
        yield {"id": i, "value": random.randint(0, 100)}

def process_data(n=2000):
    data = list(generate_data(n))
    hot_values_gen = (d["value"] for d in data if d["value"] > 90)
    hot_sum = sum(hot_values_gen)
    out = []
    for item in data:
        s = 0
        for other in data:
            if other["id"] == item["id"] + 1:
                s += other["value"]
        if s or hot_sum:
            out.append((item["id"], s + hot_sum))
    return out

if __name__ == "__main__":
    process_data()
