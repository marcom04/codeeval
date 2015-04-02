# https://www.codeeval.com/open_challenges/62/

import sys

for line in open(sys.argv[1], 'r'):
    if line in ['\n', '\r\n']:
        continue
    
    N, M = (int(x) for x in line.rstrip().split(','))
    print "%d" % (N - N/M*M)
