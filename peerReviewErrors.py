# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <Will Head-CIS245-T303>
# Creation Date: <2/10/22>
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
     cave = ''
     while cave != '1' and cave != '2':
         print('Which cave will you go into? (1 or 2)')
         cave = input()

     return cave



def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(2)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		print('Gobbles you down in one bite!')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
	displayIntro()
	caveNumber = chooseCave()
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no":
		print("Thanks for playing")


#Line 20- Indentation error on “while cave” 
#Line 24- “caves” is used instead of “cave” which is defined on line 19
#Line 34- “time.sleep” should be set to 2 seconds instead of 3
#Line 44- no parentheses around “Gobbles you down in one bite!”
#Line 47-  “=” should be replaced with “==”
#Line 49- “choosecave” should be “chooseCave”
#Line 55- “planing” should be “playing”
#I only found 7 errors, and the program is running as expected after those were corrected. 
#The first indention error I notated on line 20 was also causing issues with lines 21,22, and 24.
#(If those account for the other 3 errors?) 
