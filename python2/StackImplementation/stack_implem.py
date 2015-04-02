# https://www.codeeval.com/open_challenges/9/

import sys


def stack_push(x):
    global stack
    stack.append(x)


def stack_pop():
    global stack
    r = stack.pop()
    if stack:
        stack.pop()
    return r


for line in open(sys.argv[1], 'r'):
    if line in ['\n', '\r\n']:
        continue

    stack = []

    # Push
    splitted = line.rstrip().split()
    for x in splitted:
        stack_push(x)

    # Pop
    while stack:
        print stack_pop(),
    print ""
