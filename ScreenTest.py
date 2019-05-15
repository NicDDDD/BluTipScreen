
# Question 1: 
# For this question, I thought it easiest to iterate through the string and just replace
# the letters with numbers as I go. This meant creating case statements (if, else in python as it doesn't
# support case statements)

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
# Basically, a counter is used to increment by 1 any time we encounter a letter that is equal to the previous
# one as we iterate through the string. Once the previous letter is not equal to the current one, we add that letter and the counter plus 1 to
# account for the first instance of the letter.

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

# In Both questions, a new string was generated because Python does not allow the original string to be
# changed as python strings are immutable by design

