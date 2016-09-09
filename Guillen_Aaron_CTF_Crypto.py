#The following is a cipher based on a cipher sent by
#Robert Patterson to Thomas Jeffersion in 1801
#An explanation of this cipher can be found here:
#http://online.wsj.com/news/interactive/CIPHER0907?ref=SB124648494429082661
#
#While the above cipher forms the basis for what I do here, my cipher is
#only loosely based on it and quite a bit weaker.
#
#Aaron Guillen

import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabetU = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#Supporting Methods for Ceasar cipher
def numToChar (i):
    i = i % 26
    return alphabet[i]

def charToNum (i):
    x = 0
    for y in alphabet:
        if y == i:
            return x
        x += 1
    x = 0
    for y in alphabetU:
        if y == i:
            return x
        x += 1

#Caesar Cipher-------------------------------------------------------
def encryptCaesar(plainText, rot):                                  #
    cipherText = ""                                                 #
    for i in plainText:                                             #
        if i in alphabet or i in alphabetU:                         #
            cipherText += numToChar((charToNum(i) + rot) % 26)      #           #
        else:                                                       #
            cipherText += i                                         #
    return cipherText                                               #
                                                                    #
def decryptCaesar(cipherText, rot):                                 #
    plainText = ""                                                  # 
    for i in cipherText:                                            #
        if i in alphabet or i in alphabetU:                         #
            plainText += numToChar((charToNum(i) + rot) % 26)       #
        else:                                                       #
            plainText += i                                          #
    return plainText                                                #
#Caesar Cipher-------------------------------------------------------

#The following code will print out our blocked plain text in a simple form
def simplePrint(): 
    for i in range(0, len(cipherText)):
        for j in range(0, numCol):
            if (cipherText[i][j] != 0) and (cipherText[i][j] != "0"):
                print cipherText[i][j],
        print

#The following code will print out our blocked text in blocked form
def printBlocked():
    print "-" * ((numCol * 2) + 7)
    for i in range(0, len(cipherText)):
        print ((i % 7) + 1), ":\t",
        for j in range(0, numCol):
            if (cipherText[i][j] != 0) and (cipherText[i][j] != "0"):
                print cipherText[i][j],
        if (i + 1) % 7 == 0:
            print
            print "-" * ((numCol * 2) + 7)
        else:
            print

#We use the key to swap rows as such:
#The first digit of each number in the key represents the order
#the rows are to be swapped to, for example, if the key is
#k = [21, 14, 69, 51, 75, 41, 38] The rows in each block should
#be in the order 2, 1, 6, 5, 7, 4, 3
def swapRows():
    order = []
    temp = []
    for i in range(0, 7):
        order.append(k[i] / 10)
    for i in range(0, 3):       #Because we have 3 blocks
        for j in range(0, 7):   #of 7 rows each
            temp.append(cipherText[(i * 7) + order[j]])
    #To make the key make sense to people
    for i in range (0, 7):
        k[i] += 10
    return temp

#Our plain text string
plainText = ("When in the Course of human events it becomes necessary "
"for one people to dissolve the political bands which have connected "
"them with another and to assume among the powers of the earth, the separate "
"and equal station to which the Laws of Nature and of Nature's God entitle "
"them, a decent respect to the opinions of mankind requires that they should "
"declare the causes which impel them to the separation.")

#Instantiate our random key
k = []
x = 1
for i in range(0, 7):
    k.append(random.randint(x, x + 8))
    x += 10
    
#Ensure randomness of order
for i in range(0, 300):
    index1 = random.randint(0, 6)
    index2 = random.randint(0, 6)
    temp = k[index1];
    k[index1] = k[index2]
    k[index2] = temp    

#Remove any spaces from the plain text
plainText = plainText.replace(" ", "")

#Number of columns we'll have in our blocks
cipherLength = len(plainText)
numCol = cipherLength / 21
if cipherLength % 21 > 0:
    numCol += 1

#Convert plainText to a list because they're easier to work with
cipherText = [[0 for x in xrange(numCol)] for x in xrange(21)]
counter = 0
for i in range(0, numCol):
    for j in range(0, 21):
        if counter < cipherLength:
            cipherText[j][i] = plainText[counter]
            counter += 1
            
printBlocked()              ###############################################

#Now encryption begins. We use the key to swap rows as such:
#The first digit of each number in the key represents the order
#the rows are to be swapped to, for example, if the key is
#k = [21, 14, 69, 51, 75, 41, 38] The rows in each block should
#be in the order 2, 1, 6, 5, 7, 4, 3
cipherText = swapRows()

#Convert it back into a string
cipherStr = ""
for i in range(0, len(cipherText)):
    for j in range(0, numCol):
            cipherStr += (str)(cipherText[i][j])
            counter += 1

print k                    #################################################
printBlocked()
print
print cipherStr         ####################################################

#An important part of our encryption algorithm follows.
#Now that we've obfucated our text, we will encypt with
#a classic caesar cipher. The rotation depends on the key.
#You add up all the numbers in the key, modulo 26, and that's
#your ROT
x = 0
for i in k:
    x += i
cipherStr = encryptCaesar(cipherStr, (x % 26))
    
print "\n", cipherStr         ####################################################

#Now we put it back into a list
temp = [[]]
counter = 0
for i in range(0, 21):
    temper = []
    for j in range(0, numCol):
        temper.append(cipherStr[counter])
        counter += 1
    temp.append(temper)
temp.remove([])
cipherText = temp

printBlocked()
#print("Hello and welcome to our wonderful cryptography challenge!")
#print("It is your job to decode the following cipher.")
#print("It won't be easy, so I'll give you the key:")
#print k
#print("A nickel for your thoughts? Good luck!")
#print
#simplePrint()
