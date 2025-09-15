# baseline: intentionally inefficient nested loops and repeated dict lookups
import random

def generate_data(n=2000):
    return [{"id": i, "value": random.randint(0, 100)} for i in range(n)]

def process_data(n=2000):
    data = generate_data(n)
    out = []
    # O(n^2) pattern with repeated lookups
    for item in data:
        s = 0
        for other in data:
            if other["id"] == item["id"] + 1:
                s += other["value"]
        # repeated mapping scan below
        for other in data:
            if other["value"] > 90:
                s += other["value"]
        if s:
            out.append((item["id"], s))
    return out

if __name__ == "__main__":
    process_data()
