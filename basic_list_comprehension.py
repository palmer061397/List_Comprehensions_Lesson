# Populating a list with a for loop
nums = [12,8,21,3,16]
new_nums = []
for num in nums:
	new_nums.append(num + 1)
print(new_nums)

#List comprehension Doing above in ONE LINE OF CODE

nums2 = [12, 8, 21, 3, 16]
new_nums2 = [num + 1 for num in nums]
print(new_nums2)

# List comprehension using range()

nums3 = [num for num in range(11)]
print(nums3)

nums4 = [num *2 for num in range(11)]
print(nums4)
