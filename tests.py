from separatorguesser import guess

from unittest import TestCase

class DsvSeparatorGuesserTests(TestCase):
    def assertSeparators(self, filename, field, record):
        with open(filename) as f:
            g = guess(f)
            self.assertEqual(g.field_separator, field)
            self.assertEqual(g.record_separator, record)

    def test_csv(self):
        self.assertSeparators('test.csv', b',', b'\n')
   
    def test_tsv(self):
        self.assertSeparators('test.tsv', b'\t', b'\n')
   
