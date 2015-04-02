# https://www.codeeval.com/open_challenges/31/

import sys

for line in open(sys.argv[1], 'r'):
    if line in ['\n', '\r\n']:
        continue
        
    S, t = line.rstrip().split(',')
    print S.rfind(t)
        
