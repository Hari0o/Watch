n,m = map(int, input().split())
s='.|.'
s1="WELCOME"

# TOP
for i in range(n//2):
    print((s*((i*2)+1)).center(m,"-"))

print(s1.center(m,"-"))

for i in range(((n//2)-1),-1,-1):
    print((s*((i*2)+1)).center(m,"-"))
