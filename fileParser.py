import re
from collections import Counter
print("Welcome to File Parser\n")
print("Most Frequent Words\n")
words = re.findall(r'\w+', open('fileToParse.txt').read().lower())
count = Counter(words).most_common(15)
print(count)
print("\n")
print("Enter text to find")
fh = open("fileToParse.txt", "r")
word=input("input")
print("\n")
s=" "
count=1
print(word)
print("Let's run")
print("\n")
#------------------------------------------------
while(s):
    s=fh.readline()

    L=s.split()

# search whole string match from list of words
#     if word in L:
#         print("Line Number:", count, ":", s)

# seach for substring 
    result = s.find(word)
    if (result != -1):
        print("Line Number:", count, ":", s)
        
    count +=1
#------------------------------------------------    
fh.close()