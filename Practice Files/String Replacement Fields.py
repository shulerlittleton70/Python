#str function

age = 24
print("My age is " + str(age)+ " years old")

#str converts data types into strings
#above it converted int 24 into string 24


#Another wat is by using replacement fields {} that "Index" against the provided formating field. Starts at 0

print("my age is {0} years old".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))
