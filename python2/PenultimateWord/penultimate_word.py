# https://www.codeeval.com/open_challenges/92/

import sys

for test in open(sys.argv[1], 'r'):
    if test in ['\n', '\r\n']:
        continue

    print test.split()[-2]
