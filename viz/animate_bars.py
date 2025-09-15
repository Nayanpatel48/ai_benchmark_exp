import matplotlib.pyplot as plt
import csv
labels, means = [], []
with open("results.csv") as f:
    r = csv.DictReader(f)
    for row in r:
        labels.append(row['module'].split('.')[-1])
        means.append(float(row['mean']))

# create incremental frames for animation
for i in range(1, 21):
    frac = i / 20
    vals = [m * frac for m in means]
    plt.figure(figsize=(8,5))
    plt.bar(labels, vals)
    plt.ylim(0, max(means) * 1.1)
    plt.title("Benchmark — build animation")
    plt.tight_layout()
    plt.savefig(f"assets/frames/frame_{i:03d}.png")
    plt.close()
# combine frames to mp4 using ffmpeg in next step
