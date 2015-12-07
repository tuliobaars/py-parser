import itertools
import re
from collections import namedtuple

from .sanitize import asciize

# `Match` instances holds info about the tokens and their regexes.
# Name must be a string, and the rest are lists of strings containing
# pseudo-regexes.
Match = namedtuple('Match', 'name labels values breakers')


def compile_match_regexes(match):
    """Transforms match's pseudo-regexes into single, compiled regexes.

    Example:
      In :  [r'Valor', r'valor', r'VALOR']  <-- match.values
      Out:  r'Valor|valor|VALOR'            <-- match.values
    """
    new_labels = re.compile('|'.join(match.labels))
    new_values = re.compile('|'.join(match.values))
    new_breakers = re.compile('|'.join(match.breakers))

    new_match = Match(match.name, new_labels, new_values, new_breakers)

    return new_match


def matches_to_slices(list_of_matches):
    """Gets a list of SRE_Match objects and returns a list of slices
    between their starting points.
    """
    starts = [i.span()[0] for i in list_of_matches]
    breakpoints = [0] + starts + [-1]  # Also add ^ and $
    bp_pairs = [
        (breakpoints[i], breakpoints[i + 1])
        for i in range(len(breakpoints) - 1)
    ]
    return bp_pairs


class PageScanner:
    """Gets pages and matches, reutrns a dict with results.
    """

    def __init__(self, page_file, matches, encoding='utf-8'):

        self.page_file = page_file
        self.encoding = encoding

        self.matches = [compile_match_regexes(m) for m in matches]

        # A regex composed of set of unique breakers
        # TODO: Put this under a function
        breakers = set()
        for match in matches:  #NOTE: this block will use original matches
            assert isinstance(match.breakers, list)
            for breaker in match.breakers:
                breakers.add(breaker)
            assert isinstance(match.labels, list)  # labels are also breakers
            for label in match.labels:
                breakers.add(label)
        # Now for the combined regex
        self.breaker = re.compile('|'.join(breakers))

    def scan(self):
        results = []

        # Read whole page to memory
        with open(self.page_file, encoding=self.encoding) as fp:
            lines = [asciize(line.lower()) for line in fp.readlines()]

        # Iterate over lines
        for line_no, line in enumerate(lines):
            # split the line into segments at breakers
            breakers = self.breaker.finditer(line)

            if not breakers:  # means no labels were found either
                continue  # move on to the next line

            # Iterate over breakpoints/segments
            slices = matches_to_slices(list(breakers))
            for s in slices:
                segment = line[slice(*s)]

                # Look for labels on each segment
                for match in self.matches:
                    label = match.labels.match(segment)
                    if not label:
                        continue  # move on to the next label
                    # Look for values
                    value = match.values.findall(segment)
                    if not value:
                        # TODO: multiline search
                        # sectionize the file and search through lines
                        continue  # NOTE: Multiline not implemented yet

                    # Sanity check
                    # At this point, we have both label and value[s], so we
                    # can report them.
                    results.append(dict(
                        file=self.page_file,
                        line=line_no,
                        cols=s,
                        label=match.name,
                        value=value,
                    ))

        return results
