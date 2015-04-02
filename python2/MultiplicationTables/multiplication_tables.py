# https://www.codeeval.com/open_challenges/23/

for i in range(1, 13):
    line = ""
    for j in range(1, 13):
        line += "%4d" % (i*j)
    print line.lstrip()
