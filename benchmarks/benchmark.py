import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from time import perf_counter
from geneweaver.search import find_candidate_hits

def main():
    guide = "ACGT" * 5
    targets = [(f"target_{i}", ("T" * 40) + guide + ("G" * 40)) for i in range(1000)]
    started = perf_counter()
    hits = find_candidate_hits(guide, targets, max_mismatches=2)
    elapsed = perf_counter() - started
    print(f"targets={len(targets)}")
    print(f"hits={len(hits)}")
    print(f"elapsed_seconds={elapsed:.6f}")
    print(f"targets_per_second={len(targets) / elapsed:.2f}")

if __name__ == "__main__":
    main()
