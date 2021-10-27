import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    result = re.search(r'\\', line)
    if result is not None:
        print(line)
