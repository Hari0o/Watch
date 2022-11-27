# reverse , odd digits add,evendigits twice in single digit, add odd 

n=input('Enter the credit card number:')
reverse=n[::-1]
print(reverse)
o=0
e=0
for i in reverse[::2]:
    o=o+int(i)
print(o)

for i in reverse[1::2]:
    x=int(i)*2
    # print(x)
    while x>=10:
        s=0
        while(x!=0):
            r=x%10
            s+=r
        # e+=(1+r)
            x=x//10
        e+=s    
    else:
        e+=x
print(e)
total=e+o
print(total)

if total%10==0:
    print('valid')
else:
    print('not valid')
