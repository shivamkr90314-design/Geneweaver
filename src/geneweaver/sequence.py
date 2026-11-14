VALID_BASES = set("ACGTN")

def normalize_dna(sequence: str) -> str:
    """Remove whitespace, uppercase the sequence, and validate DNA symbols."""
    normalized = "".join(sequence.split()).upper()
    if not normalized:
        raise ValueError("DNA sequence is empty.")
    invalid = sorted(set(normalized) - VALID_BASES)
    if invalid:
        raise ValueError(f"Invalid DNA character(s): {', '.join(invalid)}")
    return normalized

def mismatch_count(left: str, right: str) -> int:
    """Count positional mismatches; sequences must have equal length."""
    if len(left) != len(right):
        raise ValueError("Sequences must have equal length for mismatch counting.")
    return sum(a != b for a, b in zip(left, right))
