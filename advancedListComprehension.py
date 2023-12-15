#Conditionals in comprehensions in the input expression
conditional = [num ** 2 for num in range(10) if num % 2 == 0]
print(conditional)

#Conditionals in the output expression
conditional1 = [num ** 2 if num % 2 == 0 else 0 for num in range(10)]
print(conditional1)

# Creating dictionaries
pos_neg = {num: -num for num in range(9)}
print(pos_neg)

#########################
##Practice
#Prints names with 7 characters or more
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
new_fellowship = [member for member in fellowship if len(member) >= 7]
print(new_fellowship)
##########################
#Prints names with 7 characters or more, else prints emtpy string
empty_fellowship = [member if len(member) >= 7 else "" for member in fellowship]
print(empty_fellowship)
##########################
#Prints dictionary with member as key and member length as value
dic_member = {member: len(member) for member in fellowship}
print(dic_member)
