# https://www.codeeval.com/open_challenges/2/

import sys

lines = []
data = open(sys.argv[1], 'r')

with data:
    N = int(data.readline())
    lines = [line.rstrip() for line in data if line not in ['\n', '\r\n']]
    lines.sort(lambda x,y: cmp(len(y), len(x)))
    print '\n'.join(lines[:N])
