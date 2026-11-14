import csv
import json

FIELDS = ["target_id", "start", "end", "mismatches", "guide", "target_window"]

def write_csv(path, hits):
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(hit.to_dict() for hit in hits)

def write_json(path, payload):
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
