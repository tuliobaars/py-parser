import re
from io import StringIO


def sectionize(filepath, x, y):
    """Returns a section of the original file starting at line y, row x.

    x and y are 0-based.
    """
    output = StringIO()
    
    with open(filepath) as fp:
        lines = fp.readlines()

    for idx, line in enumerate(lines):
        if idx >= x:
            output.write(line[y:])

    return output

