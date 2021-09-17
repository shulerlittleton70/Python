# Strings are a sequence data type
#         01234567890123
parrot = "Norwegian Blue"

print(parrot)

#print(parrot[3]) #prints w, programing starts counting at 0, N = 0, o = 1, ....


######MINI CHALLENGE#######
#Challenge: Add some code to the program so that it prints we win
#Each character should appear on a serperate line
#The program should get the characters from the parrot string, using indexing

print(parrot[-11])
print(parrot[-10])
print()
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])
print()


##Reverse Index
print(parrot[-1])

#start counting back from -1, start forward at 0

print (parrot[0:6]) #Norweg

#"UP TO BUT NOT INCLUDING!" 0:6 includes 0 - 5 and stops up to 6


print(parrot[3:5]) #we

print(parrot[0:9]) #Norwegian
print(parrot[:9]) #Norwegian

print(parrot[10:]) #Blue
print(parrot[10:14]) #Blue

print(parrot[10]) #Index
print(parrot[10:11]) #slice
#Both Show B

print(parrot[:]) #Full Word
#If you dont provide a start value, it auto start at 0
#If you dont provide a stop value, it assume the end





