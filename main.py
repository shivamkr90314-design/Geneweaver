import argparse
from pathlib import Path
from geneweaver.fasta import read_fasta
from geneweaver.search import find_candidate_hits
from geneweaver.exporters import write_csv, write_json

def build_parser():
    parser = argparse.ArgumentParser(
        description="GeneWeaver: educational CRISPR guide/target mismatch screening"
    )
    parser.add_argument("--guide", required=True, help="FASTA file containing one guide sequence")
    parser.add_argument("--targets", required=True, help="FASTA file containing target sequences")
    parser.add_argument("--max-mismatches", type=int, default=3, help="Maximum allowed mismatches")
    parser.add_argument("--output", default="results", help="Output directory")
    return parser

def main():
    args = build_parser().parse_args()
    if args.max_mismatches < 0:
        raise SystemExit("--max-mismatches must be zero or greater")

    guides = read_fasta(args.guide)
    targets = read_fasta(args.targets)
    if not guides:
        raise SystemExit("No guide sequence found.")
    if len(guides) != 1:
        raise SystemExit("Please provide exactly one guide sequence in the guide FASTA.")

    guide_id, guide = guides[0]
    hits = find_candidate_hits(guide, targets, args.max_mismatches)

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    write_csv(output_dir / "hits.csv", hits)
    write_json(output_dir / "hits.json", {
        "guide_id": guide_id,
        "guide_sequence": guide,
        "max_mismatches": args.max_mismatches,
        "hit_count": len(hits),
        "hits": [hit.to_dict() for hit in hits],
    })
    print(f"Guide: {guide_id} ({len(guide)} bases)")
    print(f"Candidate hits found: {len(hits)}")
    print(f"CSV:  {output_dir / 'hits.csv'}")
    print(f"JSON: {output_dir / 'hits.json'}")

if __name__ == "__main__":
    main()
