# https://www.codeeval.com/open_challenges/39/

import sys

memo = []

def sum_square_digits(n, acc):
    if n == '':
        return acc
    return sum_square_digits(n[1:], acc+(int(n[0])**2))

def is_happy(x):  
    sum = sum_square_digits(x, 0)
    if sum == 1:
        return 1
    if x in memo:
        return 0
    memo.append(x)
    return is_happy(str(sum))

for line in open(sys.argv[1], 'r'):
    if line in ['\n', '\r\n']:
        continue
    
    print is_happy(line.rstrip())
    memo = []
