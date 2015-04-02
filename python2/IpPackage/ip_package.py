# https://www.codeeval.com/open_challenges/154/

import sys

for line in open(sys.argv[1], 'r'):
    if line in ['\n', '\r\n']:
        continue

    bytes = line.rstrip().split(' ', 26)[:26]   # new IPs(2) + fixed IP header(20) + options(4)
    new_src = bytes.pop(0)
    new_dst = bytes.pop(0)

    # check IHL(second nibble) - if > 5, then options are present
    if (int(bytes[0][1], base=16) <= 5):
        bytes = bytes[:-4]

    # convert IP addresses and substitute them in bytes
    bytes[12:16] = [format(int(x), '02x') for x in new_src.split('.')]
    bytes[16:20] = [format(int(x), '02x') for x in new_dst.split('.')]

    # calculate new checksum
    words = [''.join(bytes[i:i+2]) for i in range(0, len(bytes), 2) if i != 10]
    csum = 0
    for word in words:
        csum += int(word, base=16)
    csum += (csum >> 16)
    csum = csum & 0xffff ^ 0xffff
    csum = format(csum, '02x')
    bytes[10:12] = [csum[:2], csum[2:]]

    # print correct header
    print ' '.join(bytes)
