from collections import namedtuple, Counter

_separators = namedtuple('_separators', 
        ['field_separator', 'record_separator'])

_record_separator = b'\n'

class GuessException(Exception):
    pass


def guessfieldseparator(byte_iter):
    accumulated_counter = None
    counter = Counter()
    for b in byte_iter:
        if b == _record_separator:
            if accumulated_counter is None:
                accumulated_counter = dict(counter)
            else:
                new_accum = {}
                for k, v in accumulated_counter.items():
                    if v == counter[k]:
                        new_accum[k] = v
                if len(new_accum) == 1:
                    for k in new_accum:
                        return k
                accumulated_counter = new_accum
            counter = Counter()
        else:
            counter[b] += 1
    raise GuessException()

def guess(file_obj):
    field_separator = guessfieldseparator(file_obj.read())
    return _separators(field_separator=field_separator,
            record_separator=_record_separator)
