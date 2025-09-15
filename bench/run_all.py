# orchestrator: runs each candidate in a fresh python process and writes CSV
import subprocess, json, csv, os
import sys

MODULES = ["bench.original", "-m","bench.sourcery_refactor","bench.tabnine_refactor","bench.local_llm_refactor"]
OUT = "results.csv"

def run_module(mod):
    p = subprocess.run([sys.executable,"bench/bench_runner.py", mod, "12", "2000"],
                       capture_output=True, text=True, check=True)
    return json.loads(p.stdout)

def main():
    rows = []
    for m in MODULES:
        r = run_module(m)
        rows.append(r)
    # write CSV (mean,stdev,ci95)
    with open(OUT,"w",newline="") as f:
        w = csv.writer(f)
        w.writerow(["module","mean","stdev","ci95"])
        for r in rows:
            w.writerow([r["module"], r["mean"], r["stdev"], r["ci95"]])
    print("Wrote", OUT)

if __name__ == "__main__":
    main()
