# https://www.codeeval.com/open_challenges/102/

import sys
import json

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test in ['\n', '\r\n']:
        continue

    items = json.loads(test)['menu']['items']
    sum = 0
    for item in items:
        if item is not None and item.get('label') is not None:
            sum += item['id']
    print sum

test_cases.close()
