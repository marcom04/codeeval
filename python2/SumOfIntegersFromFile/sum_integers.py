# https://www.codeeval.com/open_challenges/24/

import sys

sum = 0    
for line in open(sys.argv[1], 'r'):
    if line in ['\n', '\r\n']:
        continue
    sum += int(line.rstrip())
     
print sum
