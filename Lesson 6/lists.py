users = ['Dave', 'John', 'Sara']

data = ['Dave', 42, True]

emptylist = []

print("Dave" in emptylist)

print(users[0])
print(users[-2])

print(users.index("Sara"))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

users.append("Mario")
print(users)

users += ['Jason', 'Lucas']
print(users)

users.extend(['Robert', 'Ben', 'Jimmy'])
print(users)

# users.extend(data)
# print(users)

users.insert(0, 'Bob')
print(users)

users[2:2] = ['Eddie', 'Alex']
print(users)

users[1:3] = ['Robert', 'JPJ']
print(users)

users.remove('Bob') # removes Bob from the list
print(users)

print(users.pop()) # remove the last element
print(users)

del users[0] # delete the first element
print(users)

# del data
data.clear()
print(data)

users[1:2] = ["dave"]
users.sort() # alphabetically sort the list
print(users)

users.sort(key=str.lower) # alphabetically sort the list
print(users)

nums = [1, 2, 3, 414, 5]
nums.reverse()
print(nums) # reverse the list

# nums.sort(reverse=True) # sorts in descending order
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

numsCopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numsCopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, 'Neil', True])
print(mylist)

# tuples

mytuple = (("Dave", 42, True))

anothertuple = (1, 2, 5, 8, 2, 2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append("Neil")
newtuple = tuple(newlist)
print(newtuple)

(one, two, *hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))