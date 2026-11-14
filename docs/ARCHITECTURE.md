# Architecture

```text
FASTA inputs
    |
    v
fasta.read_fasta() ---> sequence.normalize_dna()
    |
    v
search.find_candidate_hits()
    |
    v
CandidateHit records
    |
    +----> exporters.write_csv()
    |
    +----> exporters.write_json()
```

## Current design decisions
- The core uses Python's standard library to keep setup simple.
- The first algorithm scans ungapped windows equal in length to the guide.
- Coordinates are zero-based and end-exclusive.
- Results are candidate sequence matches, not biological efficacy predictions.
- CPU implementation is the baseline for any future optimized/GPU implementation.
