import random
y=random.choice(['R','P','S'])
print(y)
x=input('ROCK(R),PAPPER(P),SCISSOR(S): ').upper()

if x==y:
    print('draw')
elif (x=='R' and y=='S') or (x=='S' and y=='P') or (x=='P' and y=='R'):
    print('you won')
else:
    print('computer won')
        # sx=input('ROCK(R),PAPPER(P),SCISSOR(S): ').upper
