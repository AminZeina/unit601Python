# Created By Amin Zeina
# Created On Mar 2018
# Lets User choose a number and see if their number == random number


import random
randomNumber = random.randint(1,6)
print(randomNumber)

numberGuessed = int(input('Guess a number between 1 and 6:'))

if numberGuessed == randomNumber:
	print( 'You Win!' )
else:
	print( 'You Lose!' )
	
input("end")