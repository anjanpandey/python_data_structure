# --- LIST ---
# A collection allows us to put many values in a single "variable"
# A collection is nice because we can carry many values around in one convenient package 

friends = ['Monica', 'Phoebe', 'Rachel', 'Joseph', 'Chandler', 'Ross']

# list contents are surrounded by [] and elements are separated by ,
# list element can be any python object - even another list 
# a list can be empty

'''
print([1,2,3])
print(friends)
print(['red', 'blue', 'yellow'])
print(['red', 24, 98.6])
print([1, [5,6], 7])
print([])

for i in [5,4,3,1]:
    print(i)
print("It's over!")


for i in [5,4,"kim",1]:
    print(i)
print("It's over!")

for friend in friends:
    print("You were so great:", friend)
print("Done!")

# prints Chandler 
print(friends[4])

# unlike string LIST are MUTABLE 
nums = [2, 14, 26, 41, 63]
print(nums)
nums[2] = 23
print(nums)
# total length of nums 
print(len(nums))

# range function returns a list of numbers that range from 0 to 1 less than the parameter
# we can construct an index loop using for and an integer iterator 

print(range(4))
print(list(range(len(friends))))
print(range(len(nums)))

# iteration variable 
# counted loop - going through range of numbers 
for i in range(len(friends)):
    friend = friends[i]
    print("Hey there:", friend)


# LIST MANIPULATION


a = [1,2,3] 
b = [4,5,6]
# concatenate two list 
c = a + b # does not change a or b 
print(c)

t = [9,41,12,3,74,15]
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])

# x = list()
# print(type(x))
# print(dir(x))

# building a list from scratch 

stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
# added to the end of the list 
stuff.append('tot bag')
print(stuff)

some = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# in operation does not change the list 
print(10 in some)
print(21 in some)
print(4 not in some)

# list maintains order 

# we can sort list 
# the sort method, unlike in strings, means 'sort yourself'
friends.sort()
print(friends)
print(friends[3])

print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

# manually constructed 
total = 0
count = 0
while True:
    inp = input("Enter a number: ")
    if inp == 'done' : break
    value = float(inp)
    total += value
    count += 1
average = total / count
print('Average:', average)

# using data structure to solve the same problem 
numlist = list()
while True:
    inp = input("Enter a number: ")
    if inp == "done" : break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print("Average:", average)




# split
abc = "With three words"
items = abc.split()
print(items)
print(len(items))
print(items[1])

for item in items:
    print(item)

# when you do not specify a delimeter, multiple spaces are treated like one delimeter
# you can specify what delimeter character to use in the splitting

line = "A lot        of spaces"
etc = line.split()
print(etc)

# you can specify what delimeter character to use in the splitting 
line = "first;second;third"
umm = line.split()
print(umm)
print(len(umm))
thing = line.split(";")
print(thing)
print(len(thing))



fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    print(words[2])




# double split pattern 

data = "From anjan.pandey@ut.tx.us Thu Jun  6 12:34:17 2024"

words = data.split()
email = words[1]
print(email)
pieces = email.split('@')
print(pieces)
host = pieces[1]
print(host)



fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = line.split()
    for word in words:
        if not word in lst:
            lst.append(word)
lst.sort()          
print(lst)

'''

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0


'''
validation 
'''
for line in fh:
    line = line.rstrip()
    if line.startswith("From "):
        if line == '' : continue
        words = line.split()
        email = words[1]
        print(email)
        count += 1

print("There were", count, "lines in the file with From as the first word")

'''

Always add validation before assumptions

'''