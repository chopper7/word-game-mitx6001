# PS4.1
# WORD SCORES

"""
The first step is to implement code that allows us to calculate the score for a
single word. The function getWordScore should accept as input a string of lower
case letters (a word) and return the integer score for that word, using the 
game's scoring rules.

HINTs
You may assume that the input word is always either a string of lowercase 
letters, or the empty string: "" .
You will want to use the SCRABBLE_LETTER_VALUES dictionary defined at the top 
of `ps4a.py`. You should not change its value.
Do not assume that there are always 7 letters in a hand -- the parameter `n` is
the number of letters required for a Bonus Score (the maximum number of letters
in the hand). Our goal is to keep the code modular - if you want to try playing
your word game with n=10 or n=4, you will be able to do it by simply changing 
the value of HAND_SIZE.
"""

def getWordScore(word, n):
    '''
    Returns score for the letters in a word. Assumes `word` is a valid word.

    The score for a word is the sum of the points for letters in the word,
    multiplied by the length of the word, PLUS 50 points if all n letters are
    used on the first turn.

    Letters are scored as in Scrabble (see SCRABBLE_LETTER_VALUES).

    word:    string (lowercase)
    n:       integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    '''
    score = 0
    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter]
    score *= len(word)
    if len(word) == n: score += 50     
    return score