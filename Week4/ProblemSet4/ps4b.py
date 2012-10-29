from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList):
    """
    Given a hand and a wordList, find the word that gives
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    def isWordInHand(word, hand):
        wordFreq = getFrequencyDict(word)
        for key in wordFreq:
            if wordFreq[key] > hand.get(key, 0):
                return False
        return True
    # Create a new variable to store the maximum score seen so far (initially 0)
    max_score = 0
    score = 0
    # Create a new variable to store the best word seen so far (initially None)
    best_word = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isWordInHand (word, hand):
            # Find out how much making that word is worth
            score = getWordScore(word, HAND_SIZE)
            # If the score for that word is higher than your best score
            if score > max_score:
                # Update your best score, and best word accordingly
                max_score = score
                best_word = word
    # return the best word you found.
    return best_word
#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is
    displayed, the remaining letters in the hand are displayed, and the
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).

    hand: dictionary (string -> int)
    wordList: list (string)
    """
    # Keep track of two numbers: the number of letters left in your hand and the total score
    hand_c = hand.copy()
    letters_len = calculateHandlen(hand_c)
    total_score = 0
    # As long as there are still letters left in the hand
    while letters_len > 0:
        #Display the hand
        print "Current Hand: ", displayHand(hand_c)
        #The computer choses a word
        word = compChooseWord(hand_c, wordList)
        if word == None:
            print "Total score: ", total_score, "points."
            print
            break
        #Display word choosed and score
        score = getWordScore(word, HAND_SIZE)
        total_score += score
        print word, "earned", score, "points. Total: ", total_score, "points"
        print
        # Update hand and show the updated hand to the user
        hand_c = updateHand(hand_c, word)
        letters_len = calculateHandlen(hand_c)
        # Game is over (user entered a '.' or ran out of letters), so tell user the total score
        if letters_len == 0:
            print "\nRun out of letters. Total score: ", total_score, "points."
            break

#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.

        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    #Initialize the hand and the command
    hand_c = {}
    user_input_valid = "nre"
    game_input_valid = "uc"
    while(True):
        command = str(raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: "))
        print
        if command not in user_input_valid:
            print "Invalid command."
            print
            continue
        elif command == str('n'):
            hand = dealHand(HAND_SIZE)
            hand_c = hand.copy()
        elif command == str('r'):
            if hand_c != {}:
                hand = hand_c.copy()
            else:
                print "You have not played a hand yet. Please play a new hand first!"
                print
                continue
        elif command == str('e'):
            break
        while(True):
            command2 = str(raw_input("Enter u for User Game or c for Computer Game "))
            if command2 not in game_input_valid:
                print "Invalid command."
                continue
            elif command2 == 'u':
                playHand(hand, wordList, HAND_SIZE)
                print
                break
            elif command2 == 'c':
                compPlayHand(hand, wordList)
                print
                break

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
##wordList = loadWords()
#print compChooseWord({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList)
#print compChooseWord({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList)
#print compChooseWord({'q': 2, 'x': 2, 'z': 2, 't': 2, 'n': 2}, wordList)
#print compChooseWord({'a': 1, 'd': 1, 'i': 1, 'k': 1, 'o': 1, 'n': 1, 'y': 1}, wordList)
#print compChooseWord({'a': 2, 'd': 2, 'i': 2, 'k': 2, 'o': 2, 'n': 2}, wordList)
#print compChooseWord({'a': 1, 'd': 2, 'i': 2, 'k': 1, 'o': 1, 'n': 1}, wordList)

#print compPlayHand({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList)
#print compPlayHand({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList)
#print compPlayHand({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList)
