f=open('copy.txt','r')
a=f.readlines()
e=open('even.txt','w')
o=open('odd.txt','w')
for i in range (len(a)):
    if i%2==0:
        o.write(a[i])
    else:
        e.write(a[i])
f.close()
e.close()
o.close()
