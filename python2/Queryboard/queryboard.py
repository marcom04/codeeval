import sys

INIT_VAL = 0
ROWS = 256
COLS = 256
board = [[INIT_VAL] * COLS for row in range(ROWS)]


for line in open(sys.argv[1], 'r'):
    if line in ['\n', '\r\n']:
        continue

    line = line.rstrip()
    try:
        cmd, n, val = line.split()
        n = int(n)
        val = int(val)
        if cmd == 'SetCol':
            for row in board:
                row[n] = val
        if cmd == 'SetRow':
            board[n] = [val for col in range(COLS)]
    except ValueError:
        cmd, n = line.split()
        n = int(n)
        if cmd == 'QueryRow':
            print reduce(lambda x,y: x+y, board[n])
        if cmd == 'QueryCol':
            print reduce(lambda x,y: x+y, [row[n] for row in board])
