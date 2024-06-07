# --- TUPLES ---
# Tuples are another kind of sequence that functions much like a list
# they have elements which are indexed starting at 0
# simpler and more efficient in terms of memory use and performance than lists 
# temporary variables, prefer tuples over list

'''
# x = ('Glenn', 'Sally', 'Joseph')
# print(x[2])
# y = (1, 9, 2)
# print(y)
# print("Maximum value in y is ", max(y))

for i in y:
    print(i)

# unlike a list, once you create a tuple, you cannot alter its contents - similar to string
# k = (9, 8, 7)
# k[2] = 6 # error 
# print(k)

# does not allow to sort, append, or reverse a tuple
# x.sort()
# x.append('Maria')
# x.reverse()

# t = tuple()
# print(dir(t))

# one to one correspondance 
(x, y) = (4, 'fred')
print(y)
(a, b) = (2, 5)
print(a)

# items() method in dictionaries returns a list of (key, value) tuples 



print((0, 1, 2) < (5, 1, 2))
print((8, 1, 2) < (5, 1, 2))
# if matches, looks for second one 
print((0, 1, 2000000) < (0, 3, 4))
print(('Jones', 'Sally') < ('Jones', 'Sam'))
print(('Jones', 'Sally') > ('Adams', 'Sam'))

d = {'a': 10, 'c':22, 'b':1}
print(d.items())
# sort the items by keys
print(sorted(d.items()))


j = {'b': 1, 'c': 22, 'a': 10}
# sort by keys
t = sorted(j.items())

for k, v in t:
    print(k, v)

c = {'a': 10, 'b': 1, 'c':22, 'm': 10}
tmp = list()

for k, v in c.items():
    # reverse the order where value is the first item and key is second
    tmp.append((v, k))
print(tmp)
# sort by value in descending order 
tmp = sorted(tmp, reverse=True)
print(tmp)



fhand = open('romeo.txt')
counts = dict()

for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10]:
    print(key, val)


c = {'a': 10, 'b': 1, 'c':22}
# list comprehension 
# for all create a tuple with v, k
# for each k, v in c items 
print(sorted([(v, k) for k, v in c.items()], reverse=True))



days = ('Mon', 'Tue', 'Wed')
print(days[2])

'''

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

# create a dictionary
hours = dict()
for line in handle:
    # trim trailing space
    line = line.rstrip()
    # check if the length of line is greater than 5
    # also make sure the line starts with 'From ' 
    if len(line) > 5 and line.startswith('From '):
        # split the line by :, which is used to separate time
        # here we are assuming there is no : in other areas
        words = line.split(':')
        # make sure the length of words is bigger than 0
        if(len(words) > 0):
            # based on the split, the hour stamp should be the
            # last two characters of the first word
            word = words[0].strip()
            length = len(word)
            # obtain the hour stamp
            hour = word[length-2: length]
            # put the hour and count in the dictionary
            hours[hour] = hours.get(hour, 0) + 1

# create sorted list of tuples 
lst = sorted([(k, v) for k, v in hours.items()])

# loop to print each item 
for key, val in lst:
    print(key, val)

