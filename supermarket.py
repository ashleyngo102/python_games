
#Name: Ashley Ngo
#Penn ID: 65868419
#I work alone without help

# import the random module
# use "winnings = random.randint(2, 10)" to generate a random int from 2 - 10 and store in a variable "winnings"
import random

# unit price of a lottery ticket
constant_lottery_unit_price = 2

# unit price of an apple
constant_apple_unit_price = .99

# unit price of a can of beans
constant_canned_beans_unit_price = 1.58

# unit price of a soda
constant_soda_unit_price = 1.23

# the user has initial $5 for shopping
money = 5

# the user has spent $0 initially
money_spent = 0

# the amounts of lottery tickets, apples, cans of beans, and sodas the user has purchased
lottery_amount, apple_amount, canned_beans_amount, soda_amount = 0, 0, 0, 0

#welcome message
print("Welcome to our store, today's deals include a lottery ticket $2 each, an apple $0.99$ each, a can of beans $1.58 each, soda $1.23 each")
print(" ")
#available money
print("Your initial cash balance is $" + str(money) + " First, do you wanna buy a lottery ticket for a chance at winning $2-$10? (y/n or Y/N)")
buy = str(input("answer:"))

#check the condition
if buy == "Y" or buy == "y":
    money = money - 2
    lottery_amount += 1
    a = random.randint(0,2)
    if a >= 2:
        winnings = random.randint(2,10)
        money = money + winnings
        print("Congrats, you win $", winnings)
    else:
        winnings = 0
        print("We're sorry, you didn't win")
else:
    winnings = 0
    print("Let's buy some apples!")
print(" ")

#buy apple
print("Your current cash balance is $" + str(money) + " Do you wanna buy apples? (y/n or Y/N)")
buy = str(input("answer:"))
if buy == "Y" or buy == "y":
    apple_amount = input("how many?")
    #cast the input
    try:
        apple_amount = int(apple_amount)
    except ValueError as e:
        print("Your input is not integer. Let's buy something else")
    else:
        a = apple_amount*constant_apple_unit_price
        print("You want to buy {} apple(s). This will cost {}".format(apple_amount,a))
        if money >= a:
            money = round(money - a,2)
            print("You purchased successfully")
        else:
            apple_amount = 0
            print("Not enough money")
else:
    print("no apples were purchased, let's buy something else")
print(" ")

#buy beans
print("Your current cash balance is $" + str(money) + " Do you wanna buy beans? (y/n or Y/N)")
buy = str(input("answer:"))
if buy == "Y" or buy == "y":
    canned_beans_amount = input("how many?")
    #cast the input
    try:
        canned_beans_amount = int(canned_beans_amount)
    except ValueError as e:
        print("Your input is not integer. Let's buy something else")
    else:
        a = canned_beans_amount*constant_canned_beans_unit_price
        print("You want to buy {} can(s) of beans. This will cost {}".format(canned_beans_amount,a))
        if money >= a:
            money = round(money - a,2)
            print("You purchased successfully")
        else:
            canned_beans_amount = 0
            print("Not enough money")
else:
    print("no cans of beans were purchased, let's buy something else")
print(" ")

#buy soda
print("Your current cash balance is $" + str(money) + " Do you wanna buy sodas? (y/n or Y/N)")
buy = str(input("answer:"))
if buy == "Y" or buy == "y":
    soda_amount = input("how many?")
    #cast the input
    try:
        soda_amount = int(soda_amount)
    except ValueError as e:
        print("Your input is not integer. Let's buy something else")
    else:
        a = soda_amount*constant_soda_unit_price
        print("You want to buy {} can(s) of soda. This will cost {}".format(soda_amount,a))
        if money >= a:
            money = round(money - a,2)
            print("You purchased successfully")
        else:
            soda_amount = 0
            print("Not enough money")
else:
    print("no cans of soda were purchased, this is the end of your shopping trip")
print(" ")

#question 6: the end of the shopping trip
print("Your remaining cash balance is $",money)
print("Here is your receipt! " +"lottery ticket: "+str(lottery_amount)+ " winning $" +str(winnings))
print("Apple(s): {}, Can(s) of beans: {}, Can(s) of soda: {}".format(apple_amount, canned_beans_amount, soda_amount))
print("Thank you for shopping with us")

