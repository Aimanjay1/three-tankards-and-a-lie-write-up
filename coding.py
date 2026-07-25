import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    Q = int(input_data[2])

    tankard = [i for i in range(N + 1)]
    pos = [i for i in range(N + 1)]

    idx = 3

    for _ in range(M):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        idx += 2

        item_a = tankard[a]
        item_b = tankard[b]

        tankard[a] = item_b
        tankard[b] = item_a

        pos[item_a] = b
        pos[item_b] = a

    for _ in range(Q):
        p = int(input_data[idx])
        idx += 1
        print(pos[p])

if __name__ == '__main__':
    solve()
