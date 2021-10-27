import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    result = re.search(r'cat.*?cat', line)
    if result is not None:
        print(line)
