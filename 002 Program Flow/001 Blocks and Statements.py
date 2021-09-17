#Like many languages, Python works in blocks of code.

#One of the design principles of Python, thoughm was that it
#should be uncluttered and easy to read.

#Because of this, Python doesnt use delimiters around blocks of code.

#If you have used other languages, you may have seen them use braces {} or BEGIN and END around code.
#Python doesnt use anything like thatm but instead uses indentation to indicate when a new block starts.

#Whenever a line ends with a :, this tells Python that a new code block is starting
#Backspace pulls out of block
    #Shift/Tab will also exit
#Tab can take you back to it

#############First Try at Blocks#####################

for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
    print("*" * 80) #creates a line of *



