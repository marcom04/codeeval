# https://www.codeeval.com/open_challenges/10/

import sys

for line in open(sys.argv[1], 'r'):
    if line in ['\n', '\r\n']:
        continue
    
    elements = line.rstrip().split(' ')
    M = int(elements.pop())
    if len(elements) >= M:
        print elements[-M]
