# https://www.codeeval.com/open_challenges/14/

import sys

def permute(string, start, end):
    current = 0
    if start == end-1:
        if not string in permute.result:
            permute.result.append(string)
    else:
        for current in range(start, end):
            x = list(string)
            x[start], x[current] = x[current], x[start]
            permute(''.join(x), start+1, end)
            x[start], x[current] = x[current], x[start]


for string in open(sys.argv[1], 'r'):
    if string in ['\n', '\r\n']:
        continue

    string = string.rstrip()
    permute.result = []
    permute(string, 0, len(string))
    print ','.join(sorted(permute.result))
