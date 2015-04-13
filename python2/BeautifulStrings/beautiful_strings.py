# https://www.codeeval.com/open_challenges/83/

import sys


for line in open(sys.argv[1], 'r'):
    if line in ['\n', '\r\n']:
        continue

    letters = {}
    for c in line.rstrip():
        if c.isalpha():
            c = c.upper()
            if c in letters:
                letters[c] += 1
            else:
                letters[c] = 1

    beauty = 26
    tot = 0
    for reps in sorted(letters.values(), reverse=True):
        tot += (reps * beauty)
        beauty -= 1

    print tot
