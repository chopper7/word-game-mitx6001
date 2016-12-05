# PS 4,4

"""
 Hand Length
(5 points possible)

We are now ready to begin writing the code that interacts with the player. 
We'll be implementing the playHand function. This function allows the user to 
play out a single hand. First, though, you'll need to implement the helper 
function `calculateHandlen`, which can be done in under five lines of code.
"""

def calculateHandlen(hand):
    ''' 
    Returns the length (number of letters) in the current hand.
    hand: dictionary (string int)
    returns: integer
    '''
    total = 0
    for letter in hand:
        total += hand[letter]
    return total
