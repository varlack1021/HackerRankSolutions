'''
Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his handwriting.
He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. 

The words in his note are case-sensitive and he must use only whole words available in the magazine.
He cannot use substrings or concatenation to create the words he needs.
Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.

For example, the note is "Attack at dawn". The magazine contains only "attack at dawn". 
The magazine has all the right words, but there's a case mismatch. The answer is no
'''

#My Solution
mn = input().split()

check = True


x = int(mn[0])

n = int(mn[1])

magazine = input().rstrip().split()

#For this list compare it to the dictionary, if it never exists exit the loop 
#if it all exists then it exists 

note = input().rstrip().split()

print(magazine[0])
print(note)

#Creates a dictionary
words = { }

#Puts the items in a dictionary to assign them key values
for x in range(x):
    words[magazine[x]] = None

#Checks to see if a key value is in magazine

for x in note:
    if x not in words:
        check = False
        print("Not compatible")
        break

if check:
    print("Compatible")   
     