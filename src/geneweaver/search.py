from .models import CandidateHit
from .sequence import mismatch_count, normalize_dna

def find_candidate_hits(guide, targets, max_mismatches=3):
    """
    Scan each target using ungapped windows of guide length.
    Coordinates are zero-based, end-exclusive.
    """
    guide = normalize_dna(guide)
    if max_mismatches < 0:
        raise ValueError("max_mismatches must be zero or greater")

    hits = []
    width = len(guide)
    for target_id, raw_target in targets:
        target = normalize_dna(raw_target)
        if len(target) < width:
            continue
        for start in range(0, len(target) - width + 1):
            window = target[start:start + width]
            mismatches = mismatch_count(guide, window)
            if mismatches <= max_mismatches:
                hits.append(CandidateHit(
                    target_id=target_id,
                    start=start,
                    end=start + width,
                    mismatches=mismatches,
                    guide=guide,
                    target_window=window,
                ))
    return sorted(hits, key=lambda hit: (hit.mismatches, hit.target_id, hit.start))
