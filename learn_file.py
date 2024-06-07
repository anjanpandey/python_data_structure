 # --------- READING FILES ----------
 # handle = open(filename, mode) 
 # mode can be read (r) or write (w) - it's optional
 # filename is string
 # returns a handle use to manipulate the file

 # fhand = open('mbox-short.txt' 'r')

# fhand = open('mbox-short.txt')
# not the acutal file, it gives the info of a file
# print(fhand)

# we use a special character called the 'newline' to indicate when a line ends
# we represent it as \n in strings
# newline is still one character not two

# stuff = "Hello\nWord"
# print(stuff)
# print(len(stuff)) # 10 including newline 9 + 1 = 10

# fhand = open('mbox-short.txt')
'''
count = 0
for line in fhand:
    count += 1
print('Line Count:', count)
# after the above operation, the handle is at the end of the file
# any operation done on the file won't start from the beginning 
'''
# .read() does not split lines, includes newline as part of a string
# inp = fhand.read() 
# print(len(inp))
# print(inp[:20])

'''
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        # print adds a new line
        # and there is a new line at the end of each line
        # sp we add line 36 to fix it
        print(line)
print("----------")

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue # skip
    print(line)



# ask users to enter file name
# save the file name in fname and get the handle
fname = input("Enter the file name: ")

# error handling 
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count += 1
print("There were", count, "subject lines in", fname)


fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    ls = line.rstrip()
    print(ls.upper())

'''

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
occurance = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    pos = line.find(":")
    num_str = line[pos+1:]
    num = float(num_str.strip())
    occurance += 1
    total += num
    
print("Average spam confidence:", total/occurance)