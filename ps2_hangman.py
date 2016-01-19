
import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(words):
    
    return random.choice(words)

def userGuess():

    letter = raw_input("Please guess a letter > ")
    return letter


def lettersRemaining(letter, listOne):

    listOne.append(letter)
    print "Here are the letters you have guessed", ", ".join(listOne)
    return listOne


def letterCheck(letter, listOne, listTwo):

    for i, (x,y) in enumerate(zip(listOne, listTwo)):
        if letter == x:
            listTwo[i] = letter

    return listTwo     

def compWordToList(word):

    newList = []
    for x in word:
        newList.append(x)
    return newList

def createBlankWord(listOne):

    newList = []
    for x in listOne:
        newList.append('_')
    return newList

def main():

    wordChoices = loadWords()
    computersWord = chooseWord(wordChoices)
    computersWord = compWordToList(computersWord)
    print computersWord #helper to see what word is

    correctWord = createBlankWord(computersWord)

    guessedList = []
    guesses = 10
    
    print "Hi there welcome Pete's Hangman Game!"
    while(guesses > 0):
        print "You have", guesses, "guesses to discover the chosen word"
        userLetter = userGuess()
        guessedList = lettersRemaining(userLetter, guessedList)
        correctWord = letterCheck(userLetter, computersWord, correctWord)
        print ' '.join(correctWord)
        guesses -= 1

            
main()
    
    

