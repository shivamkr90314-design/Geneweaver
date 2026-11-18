
import csv
import json
from pathlib import Path

FIELDS = [
    "target_id",
    "start",
    "end",
    "mismatches",
    "guide",
    "target_window"
]

def write_csv(path, hits):
    path = Path(path)

    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()

        for hit in hits:
            writer.writerow(hit.to_dict())

def write_json(path, payload):
    path = Path(path)

    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, ensure_ascii=False)