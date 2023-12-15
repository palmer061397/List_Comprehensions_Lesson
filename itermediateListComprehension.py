#Nested loops list comprehension
# using for loop
pairs1 = []
for num1 in range(0,2):
	for num2 in range(6,8):
		pairs1.append((num1,num2))
print(pairs1)

#doing same in one line
pars2 = [(num1, num2) for num1 in range(0,2) for num2 in range(6,8)]
print(pars2)

##another example prints first letter in each string within list
doctor = ["house", "coddy", "chase"]
result = [doc[0] for doc in doctor]
print(result)

#Create list comprehension that squares numbers 0 to 9
squares = [i**2 for i in range(0,10)]
print(squares)

# Creating a 5 x 5 matrix 
matrix = [[col for col in range(5)] for row in range(5)]
print(matrix)