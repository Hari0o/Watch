import random

def welcome():

	name = input("welcome to the hangeman Game!Plase enter your preferred name: ").capitalize()
	
	if name.isalpha()== True:
		print("""HI!""",name,"""Glad to have you here!
		you will be playing against the computer today.
		the computer will raandomly choose a word and will try to guess what the word is.
		You can always invite your friends for a fun time together
		==========
		Good luck ! have Fun Playing""")
	else:
		print('Please enter your name using letter only')
		name= input('enter a game name here:')
		print('hi!',name,'please go through the rules again')

def play_again():
	response= input('would you like to play again? YES(Y)/NO(N): ').lower()

	if response=='y':
		game_run()
	else:
		print('Hope you hade fun!,see you next time')

def get_word():
	words=['python','cool','money','scavenger','avenger']
	return random.choice(words).lower()

def game_run():
	welcome()

	alphabet=('abcdeffghijaklmnopqrstuvwxyz')

	word=get_word()

	letter_guessed=[]

	tries=7

	guessed = False

	print()

	print('the word contains',len(word),'letters')
	print(len(word)*'_')

	while guessed== False and tries > 0:
		print ('you have'+ str(tries)+ 'tries')

		guess=input('guess a letter in the word ').lower()

		if len(guess)==1:
			if guess not in alphabet:
				print('check your entry is alphaber or not')
			elif guess in letter_guessed:
				print('you already guessed that letter')
			elif guess not in word:
				print('sory,that letter is not in word:')
				letter_guessed.append(guess)
				tries -=1
			elif guess in word:
				print('great , that letter present in word')
				letter_guessed.append(guess)
			else:
				print('check your entery again')

		elif len(guess)==len(word):
			if guess==word:
				print('great job! the word is correct')
				guessed = True
			else:
				print('sorry,that was not the word')
				tries -=1
		else:
			print('the length of word is not same as length of correct word')

		status=''
		if guessed == False:
			for letter in word:
				if letter in letter_guessed:
					status +=letter
				else:
					status += '_'
			print(status)
		
		if status == word:
			print('great job!yor guess is correct')
			guessed =True
		elif tries==0:
			print ('opps!you ran out of guesses')


	play_again()

game_run()