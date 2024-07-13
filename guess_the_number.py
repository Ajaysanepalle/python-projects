import random
easy=10
hard=5
def game():
	def level_choosing(level):
		if level=='easy':
			return easy
		elif level=='hard':
			return hard
		else:
			return

	def check_answer(guessed_number,random_number,attempts):
		if guessed_number<random_number:
			print('your guess is too low')
			return attempts-1
		elif guessed_number>random_number:
			print('your guess is too high')
			return attempts-1
		# elif guessed_number>50 and guessed_number<0:
		# 	print("enter the valid input and in the range")
		# 	return
		else:
			print(f'CONGRTS YOU GUESSED COREECT NUMBER!! AND YOUR NUMBER IS {guessed_number}')
		
	print('Guess the Number between 1 to 50')
	random_number=random.randint(1,50)
	#print(random_number)
	level=input('choose the level : easy or hard : ')
	attempts=level_choosing(level)

	if attempts!=easy and attempts!=hard:
		print('enter the valid level ')
		return


	guessed_number=0 


	while guessed_number!=random_number:

		print(f'you have {attempts} remaing to guess the number')
		guessed_number=int(input('Guess The Number is : '))
		attempts=check_answer(guessed_number,random_number,attempts)



game()
