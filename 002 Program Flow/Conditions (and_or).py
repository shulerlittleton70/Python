age = int(input("How old are you?"))

#if age >= 16 and age <= 65:
if 16<=age<= 65: #Chained Comparison
    print("Have a great day at work!")
else:
    print("Enjoy your free time!")

print("-" * 80) #visual line in execution block

if age < 16 or age >65:
    print("Enjoy your free time")
else:
    print ("Have a great day at work!")
