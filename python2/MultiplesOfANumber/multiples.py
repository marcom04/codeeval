# https://www.codeeval.com/open_challenges/18/

import sys
import time

for test in open(sys.argv[1], 'r'):
    if test in ['\n', '\r\n']:
        continue    
    
    x, n = (int(tok) for tok in test.split(','))
    
    i = 1
    while i*n < x:
        i += 1
    
    print i*n
