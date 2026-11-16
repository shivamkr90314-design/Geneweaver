
from pathlib import Path
from .sequence import normalize_dna

def read_fasta(path):
    """Read and validate a FASTA file."""

    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"FASTA file not found: {path}")

    records = []
    current_id = None
    chunks = []
    seen_ids = set()

    with path.open("r", encoding="utf-8") as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            line = raw_line.strip()

            if not line:
                continue

            if line.startswith(">"):
                if current_id is not None:
                    sequence = normalize_dna("".join(chunks))
                    records.append((current_id, sequence))

                current_id = line[1:].strip()

                if not current_id:
                    raise ValueError(
                        f"Empty FASTA header at line {line_number}."
                    )

                if current_id in seen_ids:
                    raise ValueError(
                        f"Duplicate FASTA ID: {current_id}"
                    )

                seen_ids.add(current_id)
                chunks = []

            else:
                if current_id is None:
                    raise ValueError(
                        f"Sequence before FASTA header at line {line_number}."
                    )

                chunks.append(line)

    if current_id is not None:
        sequence = normalize_dna("".join(chunks))
        records.append((current_id, sequence))

    if not records:
        raise ValueError("FASTA file contains no records.")

    return records