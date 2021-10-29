import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    result = re.sub(r'a+', '', line, 1)
    print(result)
