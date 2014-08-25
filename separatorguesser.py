from collections import namedtuple, Counter

_separators = namedtuple('_separators', 
        ['field_separator', 'record_separator'])

_record_separator = b'\n'

class GuessException(Exception):
    pass

class Guesser(object):
    def __init__(self, record_separator):
        self.record_separator = record_separator
        self._candidates = None
        self.counter = Counter()

    def addbyte(self, byte):
        if byte == self.record_separator:
            if self._candidates is None:
                self._candidates = dict(self.counter)
            else:
                candidates = {}
                for b, count in self._candidates.items():
                    if count == self.counter[b]:
                        candidates[b] = count
                self._candidates = candidates
            self.counter.clear()
        else:
            self.counter[byte] += 1

    def candidates(self):
        if self._candidates:
            return list(self._candidates.keys())
        return []

def guessfieldseparator(byte_iter):
    guesser = Guesser(_record_separator)
    for b in byte_iter:
        guesser.addbyte(b)
        candidates = guesser.candidates()
        if len(candidates) == 1:
            return candidates[0]
    raise GuessException()

def guess(file_obj):
    field_separator = guessfieldseparator(file_obj.read())
    return _separators(field_separator=field_separator,
            record_separator=_record_separator)
