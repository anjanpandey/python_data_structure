'''
# https://www.py4e.com/code3/
# Learning Python String Manipulation 

# input items are stored as string 
name = input("What's your name?")
print("You said your name is ", name)

# concatenation 
a = "Anjan"
b = "Pandey"
print(a+b)
print(a+' '+b)

word = "banana"

len(word)
dir(word)
type(word)

word.upper()
word.lower()
print(word[2])
# 3 not included 
print(word[0:3]) 

index = 0
for letter in word:
    if letter == "a":
        index += 1
print(index)

line = "   space exploration  "
print(line.lstrip())
print(line.rstrip())
print(line.strip())
# first position of 'a'
print(word.find('a'))
# -1 if not in string
print(word.find('y'))
# replace all 'na' with 'ca'
print(word.replace('na', 'ca'))

if 'n' in word:
    print("Found it!")

test = "Cal III"
test.startswith("Cal") # True
test.startswith("C") # True
test.startswith("c") # False
test.startswith("cal") # False


data = "From anjan.pandey@ut.tx.us Thu Jun  6 12:34:17 2024"
atpos = data.find('@')
# first position of @
print(atpos)

# in find you can put second param to set a start point 
# here the code starts at @ sign
sppos = data.find(' ', atpos)
print(sppos)

# slice the string from after the position of @
# to the space, without including the space index 
host = data[atpos+1 : sppos]
print(host)


print(len('banana')*7)

# exercise
text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(":")
nums = text[pos + 1:]
# print(nums)
num = float(nums.strip())
print(num)

'''







