#Input request input on the behalf of the user
#The below code:
    #Request Name (ENTER)
    #Request Age from Name inserted (Enter)
    #Prints the Age given
    #Int () will keep the input/output as a number (This limits age input to a int or Error)


name = input("Please enter your name: ")
age = int(input("How old are you, {0}?".format(name)))
print(age)

#IF statement for program to check age for programming

if age >= 18:
    print("You are old enough to vote!")
    print("Please proceed to the next line.")
    print("Thank you!")
else:
    print("You will have to come back in {0} years! Thank you".format(18-age))







