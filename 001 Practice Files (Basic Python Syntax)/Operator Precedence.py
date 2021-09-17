a = 12
b = 3

print(a+b/3-4*12)
print(a+(b/3)-(4*12))
print((((a+b)/3)-4)*12)

#Please excuse my dear aunt sally.

#PEMDAS - Parentheses, Exponents, Multi/Div, Add/Sub
#BEDMAS - Brackets, Exponents, Div/Multi, Add/Sub
#BODMAS - Brackets, order, Div/Multi,Add/Sub
#BIDMAS - Brackets, Index, Division/Multi, Add/Sub

#The above can at times be confusing:
# Multi/Div have equal precedence, but are read lefft to write

c = a + b
d = c / 3
e = d - 4
print(e * 12)

print()

print(a / (b * a) /b)

