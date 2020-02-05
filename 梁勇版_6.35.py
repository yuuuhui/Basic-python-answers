from random import *

def getRandomCharacter(ch1,ch2):
    return chr(randint(ord(ch1),ord(ch2)))


def getRandomLowerCaseLetter():
    return getRandomCharacter('a','z')


def getRandomUpperCaseLetter():
    return getRandomCharacter('A','Z')


def  getRandomDigitcharacter():
    return getRandomCharacter('0','9')


def getRandomASCIICharacter():
    return chr(randint(0,127))
count = 0 
for i in range(10000):
    a = getRandomUpperCaseLetter()
    if a == "A":
        count += 1
print(count)
