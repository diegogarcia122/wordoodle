import random
import sys

def print_colored(text, color, end='\n'):
    colors = {'red': '\x1b[31m', 'green': '\x1b[32m', 'yellow': '\x1b[33m', 'blue': '\x1b[34m'}
    reset = '\x1b[0m'
    sys.stdout.write(colors.get(color, '') + text + reset + end)


file = open("dic.txt", "r")
words = file.read()

listOfWords = words.split("\n")

listOfWords = [x.upper() for x in listOfWords]
randWord = random.choice(listOfWords)

print(randWord)

y = "a"

while y != randWord:
    y = input()
    y = y.upper()



    if len(y) == 5:
        if y in listOfWords:
            for i in range(5):
                if y[i] == randWord[i]:
                        if i == 4:
                            #print("in the index " + i.__str__() + " is the letter " + y[i].__str__())
                            print_colored(y[i].__str__(), color='green')
                        else:
                                #print("in the index " + i.__str__() + " is the letter " + y[i].__str__())
                                print_colored(y[i].__str__(), color='green', end=" ")
                elif y[i] in randWord:
                        if i == 4:
                            #print("the letter " + y[i].__str__() + " is not in the index " + i.__str__() + " but is somewhere else...") 
                            print_colored(y[i].__str__(),color="yellow")
                        else:  
                            #print("the letter " + y[i].__str__() + " is not in the index " + i.__str__() + " but is somewhere else...") 
                            print_colored(y[i].__str__(),color="yellow", end=" ")
                else:
                        if i == 4:
                            print(y[i].__str__())
                        else:
                            print(y[i].__str__(), end=" ")
                        
        else:
             print("This word doesn't exist...")
    else:
        print("Please input a 5 letter word.")

print("Thank you for Playing!")


