# https://www.codeeval.com/open_challenges/13/

import sys

for line in open(sys.argv[1], 'r'):
    if line in ['\n', '\r\n']:
        continue

    string, chars = line.rstrip().split(', ')
    for char in chars:
        string = string.replace(char, '')
    print string
