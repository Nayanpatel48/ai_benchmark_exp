import csv, matplotlib.pyplot as plt

rows=[]
with open("results.csv") as f:
    r=csv.DictReader(f)
    for row in r:
        rows.append(row)

labels=[row['module'].split('.')[-1] for row in rows]
means=[float(row['mean']) for row in rows]
cis=[float(row['ci95']) for row in rows]

plt.figure(figsize=(8,5))
bars=plt.bar(labels, means, yerr=cis, capsize=6)
plt.ylabel("Seconds (mean)")
plt.title("AI refactor benchmark")
plt.tight_layout()
plt.savefig("assets/benchmark_bar.png", dpi=150)
