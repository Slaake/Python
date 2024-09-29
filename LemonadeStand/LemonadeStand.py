import random
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

print("Hello ",username," and welcome to your stand, ",standname,". Now that we have that out of the way, let's buy some supplies before we open for the day.", sep="")
print("Now that we have that out of the way, let's buy some supplies before we open for the day.")
print("You have taken a loan from the bank for $100 to start your business\n")

money = 100
sugar_price = random.randint(1,5)
water_price = random.randint(1,3)
cups_price = random.randint(1,3)
lemons_price = random.randint(2,7)
supplies = [['Sugar', 'Water', 'Cups','Lemons'], [0,0,0,0]]

answer = input(str("Would you like to buy supplies for today? Yes/No\n"))
if answer in ['y', 'Y', 'yes', 'Yes', 'YES']:
    print('For',supplies[0][0],'press 1')
    print('For',supplies[0][1],'press 2')
    print('For',supplies[0][2],'press 3')
    print('For',supplies[0][3],'press 4')
    print('To check your current supplies press 5')
    print('To open your business for the day press 6')
    choice = int(input(''))
    
while choice != 6:
    if choice == 1:
        print('The price of Sugar today is: $',sugar_price, sep='')
        print('You currently own',supplies[1][0],'bags of sugar.')                
        sugar_own = int(input('How much sugar would you like to buy today? Enter 0 to cancel.\n'))
        if sugar_own != 0:
            print('You now own',sugar_own,'bags of sugar.')
            money = money-sugar_own*sugar_price
            supplies[1][0] = sugar_own + supplies[1][0]
            print('You have $',money,' left.',sep = '')
        else:
            print('For',supplies[0][0],'press 1')
            print('For',supplies[0][1],'press 2')
            print('For',supplies[0][2],'press 3')
            print('For',supplies[0][3],'press 4')
            print('To check your current supplies press 5')
            print('To open your business for the day press 6')
            choice = int(input(''))
    elif choice == 2:
        print("The price of Water today is: $",water_price, sep="")
        water_own = int(input('How many water bottles would you like to buy today? Enter 0 to cancel.\n'))
        if water_own != 0:
            print('You now own',water_own,'bottles of water.')
            money = money-water_own*water_price
            supplies[1][1] = water_own + supplies[1][1]
            print('You have $',money,' left.',sep = '')
        else:
            print('For',supplies[0][0],'press 1')
            print('For',supplies[0][1],'press 2')
            print('For',supplies[0][2],'press 3')
            print('For',supplies[0][3],'press 4')
            print('To check your current supplies press 5')
            print('To open your business for the day press 6')
            choice = int(input(''))
    elif choice == 3:
        print("The price of Cups today is: $",cups_price, sep="")
        cups_own = int(input('How many cups would you like to buy today? Enter 0 to cancel.\n'))
        if cups_own != 0:
            print('You now own',cups_own,'cups.')
            money = money-cups_own*cups_price
            supplies[1][2] = cups_own + supplies[1][2]
            print('You have $',money,' left.',sep = '')
        else:
            print('For',supplies[0][0],'press 1')
            print('For',supplies[0][1],'press 2')
            print('For',supplies[0][2],'press 3')
            print('For',supplies[0][3],'press 4')
            print('To check your current supplies press 5')
            print('To open your business for the day press 6')
            choice = int(input(''))
    elif choice == 4:
        print("The price of Lemons today is: $",lemons_price, sep="")
        lemons_own = int(input('How many lemons would you like to buy today? Enter 0 to cancel.\n'))
        if lemons_own != 0:
            print('You now own',lemons_own,'lemons.')
            money = money-lemons_own*lemons_price
            supplies[1][3] = lemons_own + supplies[1][3]
            print('You have $',money,' left.',sep = '')
        else:
            print('For',supplies[0][0],'press 1')
            print('For',supplies[0][1],'press 2')
            print('For',supplies[0][2],'press 3')
            print('For',supplies[0][3],'press 4')
            print('To check your current supplies press 5')
            print('To open your business for the day press 6')
            choice = int(input(''))
    elif choice == 5:
        print('You currently have:',supplies[1][0], supplies[0][0])
        print('You currently have:',supplies[1][1], supplies[0][1])
        print('You currently have:',supplies[1][2], supplies[0][2])
        print('You currently have:',supplies[1][3], supplies[0][3])
        print('')
        print('For',supplies[0][0],'press 1')
        print('For',supplies[0][1],'press 2')
        print('For',supplies[0][2],'press 3')
        print('For',supplies[0][3],'press 4')
        print('To check your current supplies press 5')
        print('To open your business for the day press 6')
        choice = int(input(''))
    else:
        print(choice,'is not a valid option. Please try again.')
        print('For',supplies[0][0], 'press 1')
        print('For',supplies[0][1], 'press 2')
        print('For',supplies[0][2], 'press 3')
        print('For',supplies[0][3], 'press 4')
        print('To check your current supplies press 5')
        print('To open your business for the day press 6')
        choice = int(input(''))
