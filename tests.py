from separatorguesser import guess

from unittest import TestCase

class DsvSeparatorGuesserTests(TestCase):

    def test_csv(self):
        with open('test.csv') as f:
            g = guess(f)
            self.assertEqual(g.field_separator, b',')
            self.assertEqual(g.record_separator, b'\n')
   
    def test_tsv(self):
        with open('test.tsv') as f:
            g = guess(f)
            self.assertEqual(g.field_separator, b'\t')
            self.assertEqual(g.record_separator, b'\n')
   
