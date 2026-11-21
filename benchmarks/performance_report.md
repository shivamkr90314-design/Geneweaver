
# GeneWeaver Performance Report

## 1. Overview

This report documents the performance benchmark results
of the GeneWeaver FASTA search engine.

## 2. Benchmark Configuration

- Total Targets: 1000
- Benchmark Runs: 5
- Total Hits: 1000
- Maximum Mismatches: 2

## 3. Individual Benchmark Results

| Run | Execution Time (seconds) |
|-----|--------------------------|
| 1   | 0.294878 |
| 2   | 0.347302 |
| 3   | 0.324108 |
| 4   | 0.290758 |
| 5   | 0.303806 |

## 4. Benchmark Summary

- Average Execution Time: 0.312170 seconds
- Median Execution Time: 0.303806 seconds
- Targets Per Second: 3203.38
- Total Targets Processed: 1000
- Total Hits Found: 1000

## 5. Testing Results

The project test suite was executed using pytest.

- Total Tests: 6
- Passed: 6
- Failed: 0

All tests passed successfully.

## 6. Conclusion

The benchmark processed 1000 targets and found
1000 hits across five benchmark runs.

The measured average execution time was 0.312170
seconds, with a throughput of 3203.38 targets
per second.

These results provide a baseline for future
performance improvements in GeneWeaver.
