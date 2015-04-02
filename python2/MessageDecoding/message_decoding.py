# https://www.codeeval.com/open_challenges/36/

import math
import sys

mappings = {}

def binary_formatter(digits):
    return "{0:0"+str(digits)+"b}"
def max_bin_num(digits):
    return 2**digits-1
def sector_terminator(keys_len):
    return binary_formatter(keys_len).format(max_bin_num(keys_len))


def map_key(max_digits):
    num = 0
    digits = 1
    while digits <= max_digits:
        yield binary_formatter(digits).format(num)

        num += 1
        if num == max_bin_num(digits):
            num = 0
            digits += 1


def generate_mappings(header):
    key_gen = map_key(len(header))

    for c in header:
        mappings[key_gen.next()] = c


def parse(patterns):
    patterns = list(patterns)
    msg = ""
    while patterns:
        # get length of keys in next sector
        keys_len = ''.join(patterns[:3])
        patterns = patterns[3:]
        if keys_len == '000':
            break
        keys_len = int(keys_len, 2)
        terminator = sector_terminator(keys_len)

        # get keys in next sector
        key = ''.join(patterns[:keys_len])
        while key != terminator:
            msg += mappings[key]
            patterns = patterns[keys_len:]
            key = ''.join(patterns[:keys_len])

        # ignore sector terminator
        patterns = patterns[keys_len:]

    return msg


for line in open(sys.argv[1], 'r'):
    if line in ['\n', '\r\n']:
        continue

    line = line.rstrip()
    sep = min(line.index('0'), line.index('1'))

    generate_mappings(line[:sep])

    print parse(line[sep:])
