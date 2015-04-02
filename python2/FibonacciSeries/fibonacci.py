# https://www.codeeval.com/open_challenges/22/

import sys

numbers = {0:0, 1:1}    # memoization

def fibonacci(n):
    if not n in numbers:
        numbers[n] = fibonacci(n-1) + fibonacci(n-2)
    return numbers[n]

for line in open(sys.argv[1], 'r'):
    if line in ['\n', '\r\n']:
        continue

    print fibonacci(int(line))
