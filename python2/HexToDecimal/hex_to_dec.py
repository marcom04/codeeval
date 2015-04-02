# https://www.codeeval.com/open_challenges/67/

import sys

digits = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}

for line in open(sys.argv[1], 'r'):
    if line in ['\n', '\r\n']:
        continue
    
    res = 0
    for i, c in enumerate(reversed(line.rstrip())):
        res += (16**i * int(c if c.isdigit() else digits[c]))
    print res
