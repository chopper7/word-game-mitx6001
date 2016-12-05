# Problem #3:  Test word validity
# Implement the isValidWord function --
# At this point, we have written code to generate a random hand and display the hand to
# the user. We can also ask the user for a word (Python's raw_input) and score the word
# (using your getWordScore). However, we have not yet written any code to verify that a
# word given by a player obeys the rules of the game. A valid word is in the word list and 
# it is composed entirely of letters from the current hand.
#
# You should test your implementation by calling it multiple times on the *same* hand -
# what should the correct behavior be? Also, an empty string ("") is not a valid word - if you
# code the function correctly, you shouldn't need an additional check for this condition.
#
#------------------------------------
'''
MY TEST VALUES:
hand = {'a':1, 'x':1, 'l':3, 'e':1, 's': 2, 'n': 1}
word = "sale"
wordList = ['shovel', 'ate', 'over', 'rich', 'hide', 'rule', 'bun', 'lover', 'nor', 'sad', 'sale']
'''
#-------------------------------------------

def isValidWord(word, hand, wordList):
    """
    Returns True if: word is in wordList and is composed entirely of letters in the hand.
    Otherwise: returns False.  Does not mutate hand or wordList.
    word:       string
    hand:       dictionary (string -> int)
    wordList:   list of lowercase strings
    """
    # Testing "word" for two conditions:  if word in wordList | if each letter in word is in hand.
    #How to avoid mutation? -- count each letter in word and compare to corresponding values in hand
    #(if the key exists) to check whether each count >= the value.
    
    # CORRECT #
    inHand = False
    inList = False
    
    for ltr in word:
        if ltr not in hand.keys(): return False
        
    for ltr in word:
        if ( word.count(ltr, 0, len(word)+1) ) > hand[ltr]:
            return False
        else:
            inHand = True
            
    if word in wordList:
        inList = True
    else:
        inList = False

    return inHand and inList
    
    #PREVIOUSLY:
    '''
    inHand = False
    for letter in word:
        if letter in hand:
            inHand = True
        else:
            inHand = False
            
    inList = False
    if word in wordList:
        inList = True
    else:
        inList = False
        
    if inHand == True and inList == True:
        return True
    else:
        return False
    #OR, return inHand and inList ?
    '''
    #
    '''
    inHand = False
    for letter in word:
        if letter in hand:
            inHand = True
        else:
            return False
    if word in wordList:
        return True
    else:
        return False
    '''
#-------------------------------------------------
# edx Tests that Failed
#
# Test whether I'm "mutating the original hand" (?). What does it mean?
# -- what is the order in which the functions run?;  see playHand() notes
#
# Is it because I did rewrite the previous function, updateHand, to mutate the updated hand,
#       which maybe in effect DOES mutate the hand?
#       Okay, try restoring your first version of updateHand, then test isValidWord again.
#       RESULT: still partly INCORRECT. So, updateHand isn't the cause (or only a partial cause?).
#       Test 4, "rapture" still failed, as below;
#       And the mutate-the-original-hand retest still fails.
# Instead of bool testing for letter not being in hand, bool test for letter's key value being 0 ?
#

'''
Test 4
Function call: isValidWord(rapture, {'a': 3, 'e': 1, 'p': 2, 'r': 1, 'u': 1, 't': 1}, <edX internal wordList>)
Your output:
    True
Correct output:
    False
________________________________________________________________________

Random Test 1
Function call: isValidWord(teeth, {'b': 1, 'e': 2, 'd': 1, 'h': 1, 't': 3, 'y': 1}, <edX internal wordList>)
Output:
    True

Random Test 2
Re-testing last test to see if you mutate the original hand
Your output:
    True
Correct output:
    False
_________________________________________________________________________

Random Test 6
Function call: isValidWord(teeth, {'c': 1, 'e': 2, 'h': 1, 'l': 1, 'u': 1, 't': 2, 'w': 1}, <edX internal wordList>)
Output:
    True

Random Test 7
Re-testing last test to see if you mutate the original hand
Your output:
    True
Correct output:
    False
_________________________________________________________________________

Random Test 8
Function call: isValidWord(teeth, {'c': 1, 'e': 2, 'f': 1, 'h': 1, 'k': 1, 'u': 1, 't': 2}, <edX internal wordList>)
Output:
    True

Random Test 9
Re-testing last test to see if you mutate the original hand
Your output:
    True
_________________________________________________________________________

'''
