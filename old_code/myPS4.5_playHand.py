# ps 4.5 Play a Hand
#
# This coding of playHand got me  12.8571428571  points! (out of 15)

"""
PLAYING A HAND  (12.86/15 points)

In ps4a.py, note that in the function playHand, there is a bunch of pseudocode.
The pseudocode is provided to help guide you in writing your function.
 
Check out the Why Pseudocode? resource -- 
https://courses.edx.org/c4x/MITx/6.00.1x_5/asset/files_ps04_files_WhyPseudocode.pdf
-- to learn more about the "What?" and "Why?" of Pseudocode.

Note: Do not assume that there will always be 7 letters in a hand! 
The parameter n represents the size of the hand.
"""

def playHand(hand, wordList, n):
    '''
    Allows user to play the given hand, as follows:
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
    '''
    # Keep track of total score
    word = ''
    score = 0
    display = ''
    
    # As long as there are letters left in the hand:
    while calculateHandlen(hand) != 0:
        # Display the hand
        for letter in hand:
            ltrCnt = hand[letter]
            display += (ltrCnt*(letter + ' '))
        print 'Current Hand: ' + display
        
        # Ask user for input
        word = raw_input('Enter word, or a "." to indicate that you are finished: ')
        
        # If input is a single period:
        if word == '.':
            # End the game (break out of the loop)
            return 'Goodbye! Total score: ' + str(score) + ' points.'
        
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if isValidWord(word, hand, wordList) == False:
                # Reject invalid word (print a message followed by a blank line)
                print 'Invalid word, please try again.'
                print
                return playHand(hand, wordList, n)

            # Otherwise (the word is valid):
            else:
                score += getWordScore(word, n)
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                print '"' + word + '"' + ' earned ' + str(getWordScore(word, n)) + ' points. Total: ' + str(score) + ' points.'
                # Update the hand
                hand = updateHand(hand, word)
            
            #return playHand(hand, wordList, n)
    return 'Run out of letters. Total score: ' + str(score) + ' points.'

'''
HERE'S THE GRADER TEST MY CODE GOT INCORRECT:

Function call: playHand({'a': 2, 'p': 2, 'r': 1, 'z': 1, 'e': 1}, '<edX internal wordList>', 7)
Test 6: Full hand transcript - can't use every letter

Your output:
    Current Hand: a a p p r z e 
    Enter word, or a "." to indicate that you are finished: pear
    "pear" earned 24 points. Total: 24 points.
    Current Hand: a a p p r z e a p z 
    Enter word, or a "." to indicate that you are finished: za
    "za" earned 22 points. Total: 46 points.
    Current Hand: a a p p r z e a p z p 
    Enter word, or a "." to indicate that you are finished: p
    Invalid word, please try again.

    Current Hand: p 
    Enter word, or a "." to indicate that you are finished: .
    'Goodbye! Total score: 0 points.'

    *** ERROR: Failing on final score.
    Expected 'Goodbye! Total score: 46 points.'
    Got ''Goodbye! Total score: 0 points.'' ***


Correct output:
    Current Hand: a a p p r z e
    Enter word, or a "." to indicate that you are finished: pear
    "pear" earned 24 points. Total: 24 points

    Current Hand: a p z
    Enter word, or a "." to indicate that you are finished: za
    "za" earned 22 points. Total: 46 points

    Current Hand: p
    Enter word, or a "." to indicate that you are finished: p
    Invalid word, please try again.

    Current Hand: p
    Enter word, or a "." to indicate that you are finished: .
    Goodbye! Total score: 46 points.
    None

------------------------------

THE TESTS IT PASSED WERE:
Test 1: Using all the letters in the hand on the first guess
Test 2: Guessing incorrectly, then correctly
Test 3: Guessing word, then quitting
Test 4: Can't make a word :(
Test 5: Full hand transcript - using all letters
Test 7: Randomized Test
    
'''
