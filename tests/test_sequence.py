import unittest
from geneweaver.sequence import normalize_dna, mismatch_count

class SequenceTests(unittest.TestCase):
    def test_normalize(self):
        self.assertEqual(normalize_dna("acg t\nAC"), "ACGTAC")

    def test_invalid_character(self):
        with self.assertRaises(ValueError):
            normalize_dna("ACGX")

    def test_mismatch_count(self):
        self.assertEqual(mismatch_count("AAAA", "AATA"), 1)

    def test_length_mismatch(self):
        with self.assertRaises(ValueError):
            mismatch_count("AAA", "AA")

if __name__ == "__main__":
    unittest.main()
