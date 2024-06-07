# Dictionaries 
# A linear collection of key-value pairs 
# lookup by "tag" or "key"
# abstract objects
# we insert values into a dictionary using a key and retrieve them using a key

'''

cabinet = dict()
cabinet["summer"] = 12
cabinet["fall"] = 3
cabinet["spring"] = 75
print(cabinet)
# extract by key
print(cabinet["fall"])

# changes the dictionary 
cabinet["fall"] += 2
# check the new cabinet 
print(cabinet)

# constant dictionary
jjj = {'chuck': 1, 'fred': 2, 'jan': 100}
print(jjj)
# empty dictionary 
ooo = {} 
print(ooo)

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1
print(counts)

# the get method for dictionaries
# the pattern of checking to see if a key is already in a dictionary and 
# assuming a default value if the key is not there is so common that there
# is a method call get() that does this for us

if name in counts:
    x = counts[name]
else:
    x = 0
# get value by key
x = counts.get(name, 0)



counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)



counts = dict()
print("Enter a line of text:")
line = input('')

words = line.split()

print('Words:', words)
print("counting....")
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)


jjj = {'chuck': 1, 'fred': 2, 'jan': 100}
# gets the keys 
print(list(jjj))
# gets the keys 
print(list(jjj.keys()))
# gets the values 
print(list(jjj.values()))
# get both key and value
# list of tuples 
print(list(jjj.items()))

for aaa,bbb in jjj.items():
    print(aaa,bbb)


name = input('Enter file:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1


bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)

stuff = dict()
print(stuff['candy'])

stuff = dict()
print(stuff.get('candy', -1))

'''

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

# create a dictionary
emails = dict()

for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        if len(words) > 3:
            email = words[1]
            emails[email] = emails.get(email, 0) + 1
            

highestCount = None
highestSender = None

for email, count in emails.items():
    if highestCount is None or count > highestCount:
        highestSender = email
        highestCount = count

print(highestSender, highestCount)