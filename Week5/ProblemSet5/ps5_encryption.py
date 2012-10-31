# 6.00x Problem Set 5
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    letters_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    letters_1dic = {}
    letters_2dic = {}
    i = 0
    for letter in string.ascii_lowercase:    
        if i < len(string.ascii_lowercase)-shift: 
            letters_1dic[letter] = letters_lower[i + shift]
            letters_2dic[letter.upper()] = letters_lower[i + shift].upper()
            i += 1 
        if i >= len(string.ascii_lowercase)-shift and shift != 0:
            letters_1dic[letter] = letters_lower[i + shift - 27]
            letters_1dic[letter.upper()] = letters_lower[i + shift - 27].upper()
            i += 1
    return dict(letters_1dic.items() + letters_2dic.items())
    

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    coder_c = coder.copy()
    s = ""
    for character in text:
        if character not in coder_c:
            s += character
        else:
            s += coder_c.get(character, 0)
    return s



def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    return applyCoder(text, buildCoder(shift))

    

#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    # 1. Set the maximum number of real words found to 0.
    max_words_found = 0
    # 2. Set the best shift to 0.
    best_shift = 0
    current_shift = 0
    # 3. For each possible shift from 0 to 26:
    while current_shift < 26:
    #     4. Shift the entire text by this shift.
          coded_text = applyShift(text, current_shift)
    #     5. Split the text up into a list of the individual words.
          coded_words = []
          coded_words = coded_text.split(' ')
    #     6. Count the number of valid words in this list.
          words_found = 0
          for word in coded_words:
            if isWord(wordList, word):
                words_found += 1
    #     7. If this number of valid words is more than the largest number of
    #        real words found, then:
          if words_found > max_words_found:
    #         8. Record the number of valid words.
              max_words_found = words_found
    #         9. Set the best shift to the current shift.
              best_shift = current_shift
    #     10. Increment the current possible shift by 1. Repeat the loop
    #        starting at line 3.
          current_shift += 1
    # 11. Return the best shift.
    return best_shift



def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    text = getStoryString()
    shift = findBestShift(wordList, text)
    return applyCoder(text, buildCoder(shift))

#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    wordList = loadWords()
    print decryptStory()

#Jack Florey is a mythical character created on the spur of a moment to help cover an 
#insufficiently planned hack. He has been registered for classes at MIT twice before, but has 
#reportedly never passed a class. It has been the tradition of the residents of East Campus to 
#become Jack Florey for a few nights each year to educate incoming students in the ways, means, 
#and ethics of hacking.
