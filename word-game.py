# 6.00x Problem Set 4A Template
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
# Modified by: Sarina Canelake <sarina>

# Modified by: (me) Jeff Hartl

###############################################################
'''THE ORDER IN WHICH WE`RE PRESENTED WITH THE FUNCTIONS:
    getWordScore
    dealHand
    updateHand
    isValidWord
    calculateHandlen
    playHand
    playGame
    ----[this is as far as I got in prob set 4 when taking the course]
    compChooseWord
    compPlayHand
    playGame [with option for computer to play too]
'''

# getWordScore(word, n): Returns score, a nonnegative int, for a word of n letters
# displayHand(hand): Displays a string of letters currently in the hand.
# dealHand(n): Returns hand, a random dict containing n lowercase letters.
# updateHand(hand, word): Returns new hand dict w/lower counts for letter from word
# isValidWord(word, hand, wordList): Returns True if word is in wordList & its
#                                    letters are all in hand; otherwise False.
# calculateHandlen(hand): Returns the number of letters <int> in the current hand.

###############################################################

'''
MY TEST VALUES:
hand = {'a':1, 'x':1, 'l':3, 'e':1, 's': 2, 'n': 1}
word = "sale"
wordList = ['shovel', 'ate', 'over', 'rich', 'hide', 'rule', \
            'bun', 'lover', 'ought', 'nor', 'sad', 'sale']
'''

###############################################################

# Set up game parameters, list of valid words, & letter frequency 

import random
import string


VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
SCRABBLE_LETTER_VALUES = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4,\
                        'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3,\
                        'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1,\
                        't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}
WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words (strings of lowercase letters).
    Depending on size of word list, function may take a while to finish.
    """
    print("Loading word list from file...")
    # PYTHON 2.x
##    inFile = open(WORDLIST_FILENAME, 'r', 0)
##    wordList = []
##    for line in inFile:
##        wordList.append(line.strip().lower())
    # PYTHON 3.x
    wordList = []
    with open(WORDLIST_FILENAME, 'r') as inFile:
        for line in inFile:
            wordList.append(line.strip().lower())
    print("{} words loaded. Ready to play. \n".format(len(wordList)))
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary with keys set to the elements of the sequence arg,
    and values are the number of times an element occurs in the sequence.
    sequence:   string or list
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
    

#-----------------------------------------------------------------------

# Word Score

def getWordScore(word, n):
    """
    Returns the score <int> for a word. Assumes the word is a valid word.
    Score: sum of points for letters in word, multiplied by word's length,
           PLUS 50 points IF `n` letters are used in the word. Score is >= 0.
    Letters are scored as in Scrabble (see SCRABBLE_LETTER_VALUES).
    word:  string (lowercase)
    n:     integer (size of a player's hand of letters)
    """
    score = 0
    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter]
    score *= len(word)
    if len(word) == n: score += 50     
    return score


#-----------------------------------------------------------------------

# displayHand: Make sure you understand how this function works & what it does
# (predefined by MITx grader; I refactored print statement for Python 3.x)

def displayHand(hand):
    """
    Displays letters currently in the hand, followed by blank line.
    hand: letter frequency dictionary (string->int)
    For example:
    >>>  displayHand({'a':1, 'x':2, 'l':3, 'e':1}), should print something like
    >>>  a x x l l l e
    """
    for letter in hand:
        # print letter the number of times indicated by its frequency value
        for num in range(hand[letter]):
            print(letter, end=' ')  # PYTHON 3 syntax: print all on same line
            #print letter,          # PTYHON 2 syntax: print all on same line
    print('')


#-----------------------------------------------------------------------

# dealHand:
# (predefined by MITx grader; I refactored numVowels calculation for Python 3.x)

def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS. [about one third]
    Hands are represented as dictionaries. The keys are letters and the values
    are the number of times the particular letter is repeated in that hand.
    n:  int >= 0
    returns:  dictionary (string->int)
    """
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand


#-----------------------------------------------------------------------

# Update a hand
# It MUST NOT MUTATE the hand passed in; instead, return a COPY of hand. 
#
# (All that this function does is decrement values of keys in a dict;
# displayHand() will show the player the letters that still have >= 1)

def updateHand(hand, word):
    """
    - Update hand: use letters to make the word and return a different hand
      with letter counts decremented.
    - Assumes hand has all the letters in word: however many times a letter
      occurs in word, hand has enough of the letter in it. (isValidWord = TRUE)
    hand:  dictionary (string->int)    
    word:  string
    returns:  dictionary (string->int)
    """
    updHand = hand.copy()
    for letter in word:
        updHand[letter] = updHand.get(letter, 0) - 1
    return updHand


#-----------------------------------------------------------------------

# Check validity of a word submitted by a player

def isValidWord(word, hand, wordList):
    """
    Return True if word is in wordList & is composed entirely of letters in hand
    Otherwise return False.
    Does not mutate hand or wordList.
    word:       string
    hand:       dictionary (string->int)
    wordList:   list of lowercase strings
    """
    inHand = False
    inList = False

    # Is word in the word list?
    if word not in wordList:
        return False
    else:
        inList = True

    # Does player have enough letters in hand to make the word?
    # (only need unique, alphabetized letters of word)
    for ltr in set(word):
        if word.count(ltr) > hand.get(ltr, 0):
            # tried to use more of the letter than player has
            return False
        else:
            inHand = True

    return inHand and inList


########################################################################

# Playing a Hand
# pseudocode provided by MITx course grader.

def playHand(hand, wordList, n):
    """
    Allows the user to play their given hand, as follows:

    1* The hand is displayed.
    2* The user may input a word or a single period (the string ".") 
       to indicate they're done playing.
    3* Invalid words are rejected, and a message is displayed asking the
       user to choose another word until they enter a valid word or "."
    4* When a valid word is entered, it uses up letters from the hand.
    5* After every valid word, the score for that word is displayed,
       the remaining letters in the hand are displayed, and the user
       is asked to input another word.
    6* The sum of the word scores is displayed when the hand finishes.
    7* The hand finishes when there are no more unused letters or the user
       inputs a "."

    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    
    # Keep track of score
    score = 0
    
    # As long as there are enough letters left in the hand...
    while True:
        if sum(hand.values()) <= 1:
            print("Ran out of letters! \nTotal score: {} points".format(score))
            break

        # Display the hand
        print("Current hand: ")
        displayHand(hand)
        
        # Ask user for input
        word = input('Enter word, or a "." if you are finished:\n') #raw_
        
        # If input is a single period, end the game. Otherwise, check the word.
        if word == '.':
            print("Goodbye! Total score: {} points.".format(score))
            break
        else:
            # If the word is not valid:
            if not isValidWord(word, hand, wordList):
                # Reject invalid word (print a message followed by a blank line)
                print("Invalid word, please try again. Score: {}\n".format(score))
            # Otherwise (word IS valid):
            else:
                score += getWordScore(word, n)
                # Show word points and total score followed by a blank line
                print(""""{}" earned {} points.Total Score is: {}\n""".format(
                    word, getWordScore(word, n), score))
                # Update the hand
                hand = updateHand(hand, word)
            

########################################################################

## TO DO

"""
PLAYING A GAME  (10 points possible)
A game consists of playing multiple hands. We need to implement one final 
function to complete our word-game program. Write the code that implements the 
`playGame` function.

You should remove the code that is currently uncommented in the `playGame` 
body. Read through the specification and make sure you understand what this 
function accomplishes.

Use the `HAND_SIZE` constant to determine the number of cards in a hand.

Testing: Try out this implementation as if you were playing the game. Try 
out different values for HAND_SIZE with your program, and be sure that you 
can play the wordgame with different hand sizes by modifying only HAND_SIZE.

SEE ALSO: "A Cool Trick about `print`", below.

----------------------------------------------

SAMPLE OUTPUT
Here is how the game output should look: ( see my file 
"PS4-playGame - EXPECTED OUTPUT.txt" )

HINT ABOUT THE OUTPUT
Be sure to inspect the sample output carefully - very little is actually 
printed out in this function specifically. Most of the printed output actually 
comes from the code you wrote in `playHand` - be sure that your code is modular
and uses function calls to the `playHand` helper function.
You should also make calls to the `dealHand` helper function. You shouldn't 
make calls to any other helper function that we've written so far - in fact, 
this function can be written in about 15-20 lines of code.


# The only lines printed directly from this function are:
#   "Enter n to deal a new hand, r to replay the last hand, or e to end game: "
#   "You have not played a hand yet. Please play a new hand first!"
#   "Invalid command."

"""


def playGame(wordList):
    '''
    This function allows the user to play an arbitrary number of hands.
    1) Asks the user to input 'n' or 'r' or 'e'.
          * If the user inputs 'n', let the user play a new (random) hand.
          * If the user inputs 'r', let the user play the last hand again.
          * If the user inputs 'e', exit the game.
          * If the user inputs anything else, tell them their input was invalid.
    2) When done playing the hand, repeat from step 1
    '''
    pass



# Build data structures used for entire session and play game

if __name__ == '__main__':
    wordList = loadWords()
    hand = dealHand(HAND_SIZE)
    playHand(hand, wordList, HAND_SIZE)
    # TO DO: implement the playGame function; discard the previous two lines.
    #playGame(wordList)
