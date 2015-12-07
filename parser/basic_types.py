from collections import namedtuple

# `Match` instances holds info about the tokens and their regexes.
# Name must be a string, and the rest are lists of strings containing
# pseudo-regexes.
Match = namedtuple('Match', 'name labels values breakers')

