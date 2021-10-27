import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'\b(.+)\1\b'
    result = re.search(pattern, line)
    if result is not None:
        print(line)
