# https://www.codeeval.com/open_challenges/21/

import sys

def sum_digits(n):
    if n == '':
        return 0
    return int(n[0]) + sum_digits(n[1:])


for line in open(sys.argv[1], 'r'):
    if line in ['\n', '\r\n']:
        continue

    print sum_digits(line.rstrip())
