# 6.00x Problem Set 4A Template
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
# Modified by: Sarina Canelake <sarina>

###############################################################
'''THE ORDER IN WHICH WE`RE PRESENTED WITH THE FUNCTIONS WE HAVE TO WRITE:
    getWordScore
    dealHand
    updateHand
    isValidWord
    calculateHandlen
    playHand
    playGame
    ----[this is as far as I got in problem set 4, when taking the course]
    compChooseWord
    compPlayHand
    playGame [with option for computer to play too]
'''
###############################################################

'''
MY TEST VALUES:
hand = {'a':1, 'x':1, 'l':3, 'e':1, 's': 2, 'n': 1}
word = "sale"
wordList = ['shovel', 'ate', 'over', 'rich', 'hide', 'rule', 'bun', 'lover', 'nor', 'sad', 'sale']
'''

###############################################################

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

###############################################################

# HELPER CODE (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary in which keys are set to the elements of the sequence argument,
    and values are integer counts of the number of times an element is repeated in the sequence.
    sequence:   string or list
    return:         dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	
# (end of helper code)

###############################################################

"""This problem set is structured so that you will write a number of modular 
functions and then glue them together to form the complete  game. Instead of 
waiting until the entire game is coded, you should test each function as you 
write it, individually, before moving on. This approach is known as unit testing
and will help you debug your code.

--After writting each new function, unit test it by running "test_ps4a.py" to 
check your work.
--If your code passes the unit tests you'll see a SUCCESS message; otherwise 
a FAILURE message.
--These tests aren't exhaustive. You could test your code in other ways too."""

###############################################################

# Problem #1: Scoring a word
# CORRECT
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.
    The score is the sum of the points for letters in the word, multiplied by the
    length of the word, PLUS 50 points if all n letters are used on the first turn.
    Letters are scored as in Scrabble (see SCRABBLE_LETTER_VALUES).
    word:        string (lowercase)
    n:               integer (HAND_SIZE; i.e., hand size required for additional points)
    returns:    int >= 0
    Note: your could should not reference the variable HAND_SIZE.
    """
    score = 0
    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter]
    score *= len(word)
    if len(word) == n: score += 50     
    return score
# CORRECT

###############################################################

# Problem #2: Make sure you understand how this function works and what it does!
# (displayHand was predefined; I didn't write the code)
'''DISPLAYING A HAND
Given a hand represented as a dictionary, we want to display it in a user-
friendly way. We have provided the implementation for this in the displayHand 
function. Take a few minutes right now to read through this function carefully 
and understand what it does and how it works.'''
def displayHand(hand):
    """
    Displays the letters currently in the hand.
    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    should print out something like:
       a x x l l l e
    (The order of the letters is unimportant.)
    hand:   dictionary (string -> int)
    """
##    for letter in hand.keys():
##        for j in range(hand[letter]):
##            print letter,           # print all on the same line (orig vers was: print letter,)
##    print                               # print an empty line
    # My refactoring of the original:
    handDisplay = ''
    pairs = hand.items()     #Create a list of all the key/value pairs from the hand dict
    for kv in pairs:
        handDisplay += (kv[0]*kv[1] + " ")   #Multiply each letter by its quantity, and build a string out of them.
    print handDisplay
    
# ---------------------------------
# Problem #2: Make sure you understand how this function works and what it does!
# (dealHand was predefined; I didn't write the code)
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.  [my note: about one third]
    Hands are represented as dictionaries. The keys are letters and the values
    are the number of times the particular letter is repeated in that hand.
    n:  int >= 0
    returns:    dictionary (string -> int)
    """
    hand={}
    numVowels = n / 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand
# d.get(key,default) returns value for key if key is in dictionary d, else default; (in this case, 0.)


# ---------------------------------
# Problem #2: Update a hand by removing letters
#
# Hint:  Copying Dictionaries -- You may wish to review the .copy method of
# Python dictionaries (and other dict methods as well).
# Your code for updateHand should be short. It doesnt need to call any helper functions.

def updateHand(hand, word):
    """
   1 Assumes that 'hand' has all the letters in word.  I.e., it assumes that however many 
    times a letter appears in 'word', 'hand' has at least as many of that letter in it. 
   2 Updates hand: uses up letters in the given word and returns the new hand without those letters in it.
   3 Has no side effects: does not modify hand.
    hand:   dictionary (string -> int)    
    word:   string
    returns:    dictionary (string -> int)
    """
    # It must not mutate the hand passed in; instead, return a copy of hand 
    # with each used letter's key now having a value 1 less than it was.
    # (All that this func is doing is decrement values of keys in a dict; the predefined
    # func displayHand() will show the player the letters that still have value >= 1.)

'''LATER: I revised the code to delete from hand any key that equals 0 after updating.
    updHand = hand.copy()
    for letter in word:
        updHand[letter] = updHand.get(letter, 0) - 1
        if updHand[letter] == 0:
            del updHand[letter]
    return updHand
'''
# THIS VERSION WORKS TOO:
# 1st version:
    updHand = hand.copy()
    for letter in word:
        updHand[letter] = updHand.get(letter, 0) - 1
    return updHand
# CORRECT

# (my pseudo-code --)
    #for letter in word:
    #reference it as a key in hand,
        #updHand[letter] = hand.get(letter, 0) - 1   # -1 the value of that key
   # add it to updHand.


###############################################################

# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if: word is in wordList and is composed entirely of letters in the hand.
    Otherwise: returns False.  Does not mutate hand or wordList.
    word:       string
    hand:       dictionary (string -> int)
    wordList:   list of lowercase strings
    """
# Testing "word" for two conditions:  if word in wordList | if each letter in word is in hand.
    # test 1
    inHand = False
    for letter in word:
        if letter in hand:
            inHand = True
        else:
            return False
    #test 2
    if word in wordList:
        return True
    else:
        return False

###############################################################
#
# Problem #4: Playing a hand

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    hand: dictionary (string-> int)
    returns: integer
    """
    handLength = 0
    
    for letter in hand:
        handLength += hand[letter]
    
    return handLength

#

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE -- Remove this comment when you code this function;
    #   do your coding within the pseudocode (leaving those comments in-place!)
    '''
        # Do not assume that there will always be 7 letters in a hand!
        # The parameter n represents the size of the hand.
        # Test Cases, see -- .../courses/MITx/6.00.1x_5/1T2015/courseware/Week_4/Problem_Set_4/#
        # Additional Testing -- Be sure that, in addition to the listed tests, you test the same 
        basic test conditions with varying values of n.
        # n will never be smaller than the number of letters in the hand.
    '''
    # getWordScore(word, n)  --  Returns  score,  a non-negative integer representing the score for a word of n (HAND_SIZE) letters.
    # displayHand(hand)  --  Displays a string of letters currently in the hand.
    # dealHand(n):  --  Returns  hand,  a random dict containing a total of  n  lowercase letters.
    # updateHand(hand, word) --  Returns a new hand dict without the letters from the word.
    # isValidWord(word, hand, wordList)  --  Returns True if word is in wordList & its letters are all in hand; otherwise False.
    # calculateHandlen(hand) --  Returns the number of letters (an int) in the current hand.
    #
    #   The pseudocode is provided to help guide you in writing your function.  (REMOVE COMMENTS TILL HERE)

    # Keep track of the total score
    word = ""
    totalScore = 0
    
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
        # Display the hand
        print( "Current Hand:  " + str(displayHand(hand)) )
        # Ask user for input
        word = raw_input( "Enter word, or a "." to indicate that you are finished: " )
        # If the input is a single period:
        if word == ".":
            # End the game (break out of the loop)
            break
        # Otherwise (the input is not a single period):
        elif isValidWord(word, hand, wordList) == False:
            # If the word is not valid:            
            # Reject invalid word (print a message followed by a blank line)
            return( "That is not a valid word. Please choose another word" )
            #return playHand(hand, wordList, n)
        # Otherwise (the word is valid):
        else:
            # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
            print( word + " earned " + str(getWordScore(word, n)) + " points. Total: " + str() + " points. \n" )
                # Update the hand 
            return calculateHandlen(updateHand(hand, word))
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if word == ".":
        return "Total score: " + str() + " points."
    else:
        return "Run out of letters. Total score: " + str() + " points."

###############################################################

# Problem #5: Playing a game
# 
# (Calls the Helper Code we`ve already written for you):
# loadWords() -- Returns `wordList`, a list of valid words.
# getFrequencyDict(sequence) -- returns `freq`, a dict, w/keys set to the 
# elements of the sequence argument and whose values are integer counts of the 
# number of times an element is repeated in the sequence.

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    # TO DO ... <-- Remove this comment when you code this function
    print "playGame not yet implemented." # <-- Remove this line when you code the function
   



#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
