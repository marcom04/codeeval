# https://www.codeeval.com/open_challenges/82/

import sys

def sum_nthpow_digits(num, n, acc):
    if num == '':
        return acc
    return sum_nthpow_digits(num[1:], n, acc+(int(num[0])**n))

for line in open(sys.argv[1], 'r'):
    if line in ['\n', '\r\n']:
        continue
    
    line = line.rstrip()
    print sum_nthpow_digits(line, len(line), 0) == int(line)
    
