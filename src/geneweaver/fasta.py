from pathlib import Path
from .sequence import normalize_dna

def read_fasta(path):
    """Read a FASTA file into [(record_id, normalized_sequence), ...]."""
    path = Path(path)
    records = []
    current_id = None
    chunks = []

    with path.open("r", encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            line = raw_line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if current_id is not None:
                    records.append((current_id, normalize_dna("".join(chunks))))
                current_id = line[1:].strip()
                if not current_id:
                    raise ValueError(f"Empty FASTA header at line {line_number}.")
                chunks = []
            else:
                if current_id is None:
                    raise ValueError(f"Sequence data before FASTA header at line {line_number}.")
                chunks.append(line)

    if current_id is not None:
        records.append((current_id, normalize_dna("".join(chunks))))
    return records
