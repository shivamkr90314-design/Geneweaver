
import sys
from pathlib import Path
from time import perf_counter
from statistics import mean, median

# Add src directory to Python path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from geneweaver.search import find_candidate_hits

def generate_targets(count=1000):
    """Generate sample DNA targets."""
    guide = "ACGT" * 5

    targets = [
        (
            f"target_{i}",
            ("T" * 40) + guide + ("G" * 40)
        )
        for i in range(count)
    ]

    return guide, targets

def run_benchmark():
    """Run repeated DNA search benchmarks."""

    guide, targets = generate_targets(1000)

    runs = 5
    execution_times = []
    total_hits = 0

    print("=" * 45)
    print("GENEWEAVER PERFORMANCE BENCHMARK")
    print("=" * 45)

    print(f"Total targets: {len(targets)}")
    print(f"Benchmark runs: {runs}")
    print()

    for run in range(1, runs + 1):

        started = perf_counter()

        hits = find_candidate_hits(
            guide,
            targets,
            max_mismatches=2
        )

        elapsed = perf_counter() - started

        execution_times.append(elapsed)
        total_hits = len(hits)

        print(
            f"Run {run}: {elapsed:.6f} seconds"
        )

    average_time = mean(execution_times)
    median_time = median(execution_times)

    targets_per_second = (
        len(targets) / average_time
        if average_time > 0
        else 0
    )

    print()
    print("=" * 45)
    print("BENCHMARK SUMMARY")
    print("=" * 45)

    print(f"Total targets: {len(targets)}")
    print(f"Total hits: {total_hits}")
    print(f"Total runs: {runs}")

    print(f"Average time: {average_time:.6f} seconds")
    print(f"Median time: {median_time:.6f} seconds")

    print(
        f"Targets per second: {targets_per_second:.2f}"
    )

    print("=" * 45)

def main():
    run_benchmark()

if __name__ == "__main__":
    main()