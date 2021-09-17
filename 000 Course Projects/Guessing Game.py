import time as t

answer = 5

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess < answer:
    print("Please guess higher: ")
    guess = int(input())
    if guess == answer:
        print("Well done! You guessed it!")
    else:
        print("GAME OVER")
        t.sleep(5)


elif guess > answer:
    print ("Please guess lower: ")
    guess = int(input())
    if guess == answer:
        print("Well done! You guessed it!")
    else:
        print("GAME OVER")
        t.sleep(5)

else:
    print("You got it the first time!")
    t.sleep(5)
