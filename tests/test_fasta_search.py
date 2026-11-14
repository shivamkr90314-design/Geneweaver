import tempfile
import unittest
from pathlib import Path
from geneweaver.fasta import read_fasta
from geneweaver.search import find_candidate_hits

class FastaSearchTests(unittest.TestCase):
    def test_read_fasta_and_find_exact_hit(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "input.fasta"
            path.write_text(">t1\nTTTACGTAAA\n", encoding="utf-8")
            records = read_fasta(path)
            hits = find_candidate_hits("ACGT", records, max_mismatches=0)
            self.assertEqual(len(hits), 1)
            self.assertEqual(hits[0].start, 3)
            self.assertEqual(hits[0].end, 7)

    def test_mismatch_threshold(self):
        hits = find_candidate_hits("AAAA", [("t", "AATA")], max_mismatches=1)
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0].mismatches, 1)

if __name__ == "__main__":
    unittest.main()
