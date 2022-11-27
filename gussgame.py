import random

ans= random.randint(1,100)
print(ans)
guess=int(input('guess the number: '))
count=1
while guess!=ans and count<5:
    if guess>ans:
        print('guessed number is greater')
    if guess<ans:
        print('guessed number is lower')
    guess=int(input('guess again: '))
    count +=1
if count==4:
    print('you lost!,the answer is:',ans)
else:
    print('you won in',count,"attempts")
    