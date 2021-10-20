import time as t

answer = 5

print("Please guess an number between 1 and 10: ")
guess = int(input())

if guess != answer:
    if guess < answer:
        print("Please Guess Higher")
    else: # guess must be greater than
        print("Ple3"
              "ase Guess Lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it!")
    else:
        print("Sorry, you have not guessed correctly")
else:
    print("You got it the first time!")

# if guess < answer:
#     print("Please guess higher: ")
#     guess = int(input())
#     if guess == answer:
#         print("Well done! You guessed it!")
#     else:
#         print("GAME OVER")
#         t.sleep(5)
#
#
# elif guess > answer:
#     print ("Please guess lower: ")
#     guess = int(input())
#     if guess == answer:
#         print("Well done! You guessed it!")
#     else:
#         print("GAME OER")
#         t.sleep(5)
#
# else:
#     print("You got it the first time!")
#     t.sleep(5)



#less than <
#Less than or equal to <=
#Greater than >
#Greater than or equal to >=
#Equal to ==
#Not Equal to !=







