from pwn import *

p = remote('pwnable.kr', 9007)
# m = p.recv()
# print(m)

m = p.recvuntil('- Ready? starting in 3 sec... -\n\t\n')
print(m)
# print(m)
# print('es')
while True:
    m = p.recvregex(br'N=(\d+) C=(\d+)\n', capture=True)
    N, C = (int(x) for x in m.groups())
    print(N, C)
    start, end = 0, N-1
    for i in range(C):
        if start == end:
            p.sendline(b'0')
            p.recvline()
            continue
        mid = (start + end) // 2
        p.sendline(' '.join([str(x) for x in range(start, mid + 1)]).encode())
        r = int(p.recvregex(br'(\d+)\n', capture=True).group(1))
        print(f'searching in [{start}, {mid}] = {r}')
        if r % 10 == 0:
            start = mid + 1
        else:
            end = mid
    print(f'guessing {start}')
    p.sendline(str(start).encode())
    print(p.recvline())