# usage: python bench_runner.py module_name iterations
import importlib, sys, time, statistics, json

def single_run(module_name, n):
    m = importlib.import_module(module_name)
    start = time.perf_counter()
    m.process_data(n)
    return time.perf_counter() - start

def run(module_name, iterations=10, n=2000):
    times = []
    for i in range(iterations):
        t = single_run(module_name, n)
        times.append(t)
    mean = statistics.mean(times)
    stdev = statistics.stdev(times) if len(times) > 1 else 0.0
    stderr = stdev / (len(times)**0.5) if len(times) > 1 else 0.0
    ci95 = 1.96 * stderr
    return {"module": module_name, "times": times,
            "mean": mean, "stdev": stdev, "ci95": ci95}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python bench_runner.py bench.original 10 2000")
        sys.exit(1)
    mod = sys.argv[1]
    iters = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    n = int(sys.argv[3]) if len(sys.argv) > 3 else 2000
    out = run(mod, iterations=iters, n=n)
    print(json.dumps(out))
