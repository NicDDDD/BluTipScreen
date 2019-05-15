
# Question 1: 

def leetTransform(stringToChange):
    finalString = ''
    for i in range(len(stringToChange)):
        letter = stringToChange[i]
        if letter == "a" or letter == "A":
            finalString += str(4)
        elif letter == "e" or letter == "E":
            finalString += str(3)
        elif letter == "i" or letter == "I":
            finalString += str(1)
        elif letter == "o" or letter == "O":
            finalString += str(0)
        elif letter == "s" or letter == "S":
            finalString += str(5)
        elif letter == "t" or letter == "T":
            finalString += str(7)
        elif letter == "d" or letter == "D":
            finalString += str(5)
        else: finalString += stringToChange[i]
    print(finalString)

stringTest = "Let's have some fun"
print(stringTest)
leetTransform(stringTest)

# Question 2:

def countRepeats(stringToCount):
    count = 0
    returnString = ''
    for i in range(1,len(stringToCount)):
        if stringToCount[i-1] == stringToCount[i]:
            count += 1
            if i == len(stringToCount)-1:
                returnString = returnString + stringToCount[i-count] + str(count+1)   
        elif count != 0:
            returnString = returnString + stringToCount[i-1] + str(count+1)
            count = 0
            if i == len(stringToCount)-1:
                returnString = returnString + stringToCount[i]
        else:
            count = 0
            returnString = returnString + stringToCount[i-1]
            if i == len(stringToCount)-1:
                returnString = returnString + stringToCount[i]
    print(returnString)

anotherString = "aaabbdcccccffffghklmnoppppkl"
print(anotherString)
countRepeats(anotherString)

