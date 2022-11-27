from ctypes.wintypes import HACCEL
from hashlib import sha3_512


s= int(input())
c='H'
for i in range (s):
    print((c*i).rjust(s-1)+c+(c*i).ljust(s-1))

for i in range (s+1):
    print((c*s).center(s*2)+(c*s).center(s*6))

for i in range ((s+1)//2):
    print((c*(s*5)).center(s*6))

for i in range (s+1):
    print((c*s).center(s*2)+(c*s).center(s*6))

for i in range (s):
    print(((c*(s-i-1)).rjust(s)+c+(c*(s-i-1)).ljust(s)).rjust(s*6))