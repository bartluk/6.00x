# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    letterMatch = []
    for letter in lettersGuessed[:]:
        if letter in secretWord:
           letterMatch.append(1)
        else:
           letterMatch.append(0)
    return sum(letterMatch) == len(secretWord)



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    finalString = ""
    for letter in secretWord:
        if letter in lettersGuessed:
           finalString += letter
        else:
           finalString += "_ "
    return finalString



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    allLetters = string.ascii_lowercase
    for letter in lettersGuessed:
        if letter in allLetters:
           allLetters = allLetters.replace(letter, "")
    return allLetters
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
def hangman(secretWord):
    attempt = 8
    call = 0
    lettersGuessed = []
    mistakesMade = []
    g = ''
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + " letters long."
    
    while attempt >= 1:
          print '-------------'
          print 'You have ' + str(attempt) + ' guesses left.'
          print 'Available letters: ' + str(getAvailableLetters(lettersGuessed))
          letterInput = str(raw_input('Please guess a letter: '))
          letterInput = string.lower(letterInput)

          if letterInput in mistakesMade or letterInput in lettersGuessed:
             lettersGuessed.append(letterInput)
             print 'Oops! You\'ve already guessed that letter: ' + str(getGuessedWord(secretWord, lettersGuessed))
          if letterInput in secretWord and letterInput not in lettersGuessed:
             lettersGuessed.append(letterInput)
             print 'Good guess: ' + str(getGuessedWord(secretWord, lettersGuessed))
          if letterInput not in secretWord and letterInput not in mistakesMade:
              lettersGuessed.append(letterInput)
              print 'Oops! That letter is not in my word: ' + str(getGuessedWord(secretWord, lettersGuessed))
              attempt -= 1
              mistakesMade.append(letterInput)
         
          if str(getGuessedWord(secretWord, lettersGuessed)) == secretWord:
             print '-----------'
             print 'Congratulations, you won!'
             break
          
          call += 1
    if str(getGuessedWord(secretWord, lettersGuessed)) != secretWord:     
          print '-----------'
          print 'Sorry, you ran out of guesses. The word was ' + str(secretWord) + '.'                           
             
          
	





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
