import random
import sys

print( 
''' 
==================================================== 
|                                                  |
|    Welcome to the Python Lemonade Stand game!    |
|                                                  |
| In this game you are in charge of a new business | 
|   that is looking to grow by selling lemonade.   |
|                                                  |
|      Help make decisions a grow your stand!      |
==================================================== 
'''
	) 



username = input(str("First off, what is your name?\n"))
standname = input(str("Next, what would you like to name your new Lemonade stand?\n"))

print("Hello",username, "and welcome to your stand,",standname,". Now that we have that out of the way let's buy some supplies before we open for the day." )

answer = input(str("Would you like to buy supplies for today? Yes/N\n"))
if answer in ['y', 'Y', 'yes', 'Yes', 'YES']:
    print('"1" for Sugar')
    print('"2" for Water')
    print('"3" for Cups')
    print('"4" for Lemons')
    print('"5" to stop shopping')
    choice = int(input(''))
    
while choice > 5:
    print(choice,'is not a valid option. Please try again.')
    print('"1" for Sugar')
    print('"2" for Water')
    print('"3" for Cups')
    print('"4" for Lemons')
    print('"5" to stop shopping')
    choice = int(input(''))
    
if choice == 1:
    
elif choice == 2:
    
elif choice == 3:
    
elif choice == 4:
    
else:
