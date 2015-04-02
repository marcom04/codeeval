# https://www.codeeval.com/open_challenges/20/

import sys
import time

for test in open(sys.argv[1], 'r'):
    if test in ['\n', '\r\n']:
        continue    
    
    print test.rstrip().lower()
