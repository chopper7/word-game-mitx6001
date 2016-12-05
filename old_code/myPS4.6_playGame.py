# Problem Set, #5: Playing a game

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

---------------------------------------------------------------

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
    # TO DO ... <-- Remove this comment when you code this function
    
    # Calls:  playHand(),  dealHand() -- * so, maybe  dealHand(HAND_SIZE) ?
    #
    # The only lines printed directly from this function are:
    #       "Enter n to deal a new hand, r to replay the last hand, or e to end game: "
    #       "You have not played a hand yet. Please play a new hand first!"
    #       "Invalid command."
# --------------------------------
# LAST TRY BEFORE DEADLINE CUTOFF:
    playing = 1
    userChoice = ''
    dealt = 0
    while playing == 1:
        userChoice = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if userChoice == 'n':
            hand = dealHand(HAND_SIZE)
            dealt = 1
            print playHand(hand, wordList, HAND_SIZE)
            playing = 1
        elif userChoice == 'r':
            if dealt == 1:
                print playHand(hand, wordList, HAND_SIZE)
                playing = 1
            else:
                print 'You have not played a hand yet. Please play a new hand first!'
                playing = 1
        elif userChoice == 'e':
            playing = 0
        else:
            print 'Invalid command.'
            playing = 1  
    else:
        print

# Test results
# INCORRECT  <Hide output><Show output>
'''
Function call: playGame(<edX internal wordList>)
Test 1: Playing a single game, then quitting.

Your output:
    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
    Hand passed to playHand:  a c b
    <playHand execution not shown for grading brevity>
    None
    Enter n to deal a new hand, r to replay the last hand, or e to end game: e

    None

    *** ERROR: Failed to ask for input!
    Expected 'Enter n to deal a new hand, r to replay the last hand, or e to end game: e'
     Got 'None' ***

Correct output:
    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
    Hand passed to playHand:  a c b
    <playHand execution not shown for grading brevity>

    Enter n to deal a new hand, r to replay the last hand, or e to end game: e
    None
-------------------------

Function call: playGame(<edX internal wordList>)
Test 2: Playing three games, then quitting.

Your output:
    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
    Hand passed to playHand:  a z
    <playHand execution not shown for grading brevity>
    None
    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
    Hand passed to playHand:  q i
    <playHand execution not shown for grading brevity>
    None
    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
    Hand passed to playHand:  d o
    <playHand execution not shown for grading brevity>
    None
    Enter n to deal a new hand, r to replay the last hand, or e to end game: e

    None

    *** ERROR: Failed to ask for input!
    Expected 'Enter n to deal a new hand, r to replay the last hand, or e to end game: n'
     Got 'None' ***

Correct output:
    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
    Hand passed to playHand:  a z
    <playHand execution not shown for grading brevity>

    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
    Hand passed to playHand:  q i
    <playHand execution not shown for grading brevity>

    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
    Hand passed to playHand:  d o
    <playHand execution not shown for grading brevity>

    Enter n to deal a new hand, r to replay the last hand, or e to end game: e
    None
-------------------------

Function call: playGame(<edX internal wordList>)
Test 3: Replaying a hand.

Your output:
    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
    Hand passed to playHand:  a b t o
    <playHand execution not shown for grading brevity>
    None
    Enter n to deal a new hand, r to replay the last hand, or e to end game: r
    Hand passed to playHand:  a b t o
    <playHand execution not shown for grading brevity>
    None
    Enter n to deal a new hand, r to replay the last hand, or e to end game: e

    None

    *** ERROR: Failed to ask for input!
    Expected 'Enter n to deal a new hand, r to replay the last hand, or e to end game: r'
     Got 'None' ***

Correct output:
    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
    Hand passed to playHand:  a b t o
    <playHand execution not shown for grading brevity>

    Enter n to deal a new hand, r to replay the last hand, or e to end game: r
    Hand passed to playHand:  a b t o
    <playHand execution not shown for grading brevity>

    Enter n to deal a new hand, r to replay the last hand, or e to end game: e
    None
-------------------------

Function call: playGame(<edX internal wordList>)
Test 4: Replaying a hand.

Your output:
    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
    Hand passed to playHand:  b e e f l o t t z
    <playHand execution not shown for grading brevity>
    None
    Enter n to deal a new hand, r to replay the last hand, or e to end game: r
    Hand passed to playHand:  b e e f l o t t z
    <playHand execution not shown for grading brevity>
    None
    Enter n to deal a new hand, r to replay the last hand, or e to end game: r
    Hand passed to playHand:  b e e f l o t t z
    <playHand execution not shown for grading brevity>
    None
    Enter n to deal a new hand, r to replay the last hand, or e to end game: r
    Hand passed to playHand:  b e e f l o t t z
    <playHand execution not shown for grading brevity>
    None
    Enter n to deal a new hand, r to replay the last hand, or e to end game: e

    None

    *** ERROR: Failed to ask for input!
    Expected 'Enter n to deal a new hand, r to replay the last hand, or e to end game: r'
     Got 'None' ***

Correct output:
    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
    Hand passed to playHand:  b e e t t f z l o
    <playHand execution not shown for grading brevity>

    Enter n to deal a new hand, r to replay the last hand, or e to end game: r
    Hand passed to playHand:  b e e t t f z l o
    <playHand execution not shown for grading brevity>

    Enter n to deal a new hand, r to replay the last hand, or e to end game: r
    Hand passed to playHand:  b e e t t f z l o
    <playHand execution not shown for grading brevity>

    Enter n to deal a new hand, r to replay the last hand, or e to end game: r
    Hand passed to playHand:  b e e t t f z l o
    <playHand execution not shown for grading brevity>

    Enter n to deal a new hand, r to replay the last hand, or e to end game: e
    None
-------------------------

Function call: playGame(<edX internal wordList>)
Test 5: Nothing should break if I call 'r' first -
    you should just print a message to the user if they do this. User should 
    be able to enter 'r' endlessly and the message should always display.
    (Hint: use a loop for this!)

Your output:
    Enter n to deal a new hand, r to replay the last hand, or e to end game: r
    You have not played a hand yet. Please play a new hand first!
    Enter n to deal a new hand, r to replay the last hand, or e to end game: r
    You have not played a hand yet. Please play a new hand first!
    Enter n to deal a new hand, r to replay the last hand, or e to end game: r
    You have not played a hand yet. Please play a new hand first!
    Enter n to deal a new hand, r to replay the last hand, or e to end game: r
    You have not played a hand yet. Please play a new hand first!
    Enter n to deal a new hand, r to replay the last hand, or e to end game: r
    You have not played a hand yet. Please play a new hand first!
    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
    Hand passed to playHand:  a a p r e e t
    <playHand execution not shown for grading brevity>
    None
    Enter n to deal a new hand, r to replay the last hand, or e to end game: e

    None

    *** ERROR: Failed to ask for input!
    Expected 'Enter n to deal a new hand, r to replay the last hand, or e to end game: e'
     Got 'None' ***

Correct output:
    Enter n to deal a new hand, r to replay the last hand, or e to end game: r
    You have not played a hand yet. Please play a new hand first!

    Enter n to deal a new hand, r to replay the last hand, or e to end game: r
    You have not played a hand yet. Please play a new hand first!

    Enter n to deal a new hand, r to replay the last hand, or e to end game: r
    You have not played a hand yet. Please play a new hand first!

    Enter n to deal a new hand, r to replay the last hand, or e to end game: r
    You have not played a hand yet. Please play a new hand first!

    Enter n to deal a new hand, r to replay the last hand, or e to end game: r
    You have not played a hand yet. Please play a new hand first!

    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
    Hand passed to playHand:  a a p r e e t
    <playHand execution not shown for grading brevity>

    Enter n to deal a new hand, r to replay the last hand, or e to end game: e
    None
-------------------------

Function call: playGame(<edX internal wordList>)
Test 6: Invalid input test. If the input is invalid, a message - 'Invalid command.' - should print out.

Your output:
    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
    Hand passed to playHand:  a a a i i j q s t v
    <playHand execution not shown for grading brevity>
    None
    Enter n to deal a new hand, r to replay the last hand, or e to end game: x
    Invalid command.
    Enter n to deal a new hand, r to replay the last hand, or e to end game: y
    Invalid command.
    Enter n to deal a new hand, r to replay the last hand, or e to end game: z
    Invalid command.
    Enter n to deal a new hand, r to replay the last hand, or e to end game: k
    Invalid command.
    Enter n to deal a new hand, r to replay the last hand, or e to end game: s
    Invalid command.
    Enter n to deal a new hand, r to replay the last hand, or e to end game: w
    Invalid command.
    Enter n to deal a new hand, r to replay the last hand, or e to end game: e

    None

    *** ERROR: Failed to ask for input!
    Expected 'Enter n to deal a new hand, r to replay the last hand, or e to end game: x'
     Got 'None' ***

Correct output:
    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
    Hand passed to playHand:  a a a q s t v i i j
    <playHand execution not shown for grading brevity>

    Enter n to deal a new hand, r to replay the last hand, or e to end game: x
    Invalid command.
    Enter n to deal a new hand, r to replay the last hand, or e to end game: y
    Invalid command.
    Enter n to deal a new hand, r to replay the last hand, or e to end game: z
    Invalid command.
    Enter n to deal a new hand, r to replay the last hand, or e to end game: k
    Invalid command.
    Enter n to deal a new hand, r to replay the last hand, or e to end game: s
    Invalid command.
    Enter n to deal a new hand, r to replay the last hand, or e to end game: w
    Invalid command.
    Enter n to deal a new hand, r to replay the last hand, or e to end game: e
    None
'''

# ------------------------------------------------

    playerInput = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')

    # Based on what playerInput equals . . .
    # 4 possible inputs from player:  'n' , 'r' ,  'e' , '[anything else]'
        
    if playerInput == 'n':
        #call dealHand, then call playHand(dealHand as its arg)
        hand = dealHand(HAND_SIZE)
        return playHand(hand, wordList, HAND_SIZE)
        
    elif playerInput == 'r':
        #If a hand exists currently, call playHand with it
        if hand != []:
            return playHand(hand, wordList, HAND_SIZE)
        #Otherwise there's no hand to replay
        else:
            return 'You have not played a hand yet. Please play a new hand first!'
        
    elif playerInput == 'e' :
        #exit, quit, whatever the command is
        # raise SystemExit
        print

    else:
        # Invalid, recall playGame.
        return 'Invalid command.'
   
# ----------------------------------------------

    playing = 1
    userChoice = ''
    dealt = 0

    if playing == 1:
        userChoice = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        while userChoice != 'e':
            if userChoice == 'n':
                hand = dealHand(HAND_SIZE)
                dealt = 1
                playHand(hand, wordList, HAND_SIZE)
                # go back to userChoice=raw_input
            elif userChoice == 'r':
                #if there's a hand:
                if dealt == 1:
                    playHand(hand, wordList, HAND_SIZE)
                    # go back to userChoice=raw_input
                else:
                    print 'You have not played a hand yet. Please play a new hand first!'
                    # go back to userChoice=raw_input
            else:
                print 'Invalid command.'
                # go back to userChoice=raw_input
        #when != e becomes == e,
        playing = 0
    else:
        #game over, man!
        return


# ------------------------------------------------------
    playerInput = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
    while playerInput != 'e':        
        if playerInput == 'n':
            #call dealHand, then call playHand(dealHand as its arg)
            hand = dealHand(HAND_SIZE)
            print playHand(hand, wordList, HAND_SIZE)
            return playGame(wordList)
        elif playerInput == 'r':
            #If a hand exists currently, call playHand with it
            if hand != []:
                print playHand(hand, wordList, HAND_SIZE)
                return playGame(wordList)
            #Otherwise there's no hand to replay
            else:
                print 'You have not played a hand yet. Please play a new hand first!'
                return playGame(wordList)
        else:
            # Invalid, recall playGame.
            return 'Invalid command.'
    return

###############################################################

'''
A Cool Trick about 'print':
You can make two or more print statements print to the same line if you separate them with a comma!
Try out the following code:
    print 'Hello ',
    print 'world',
    print '!'
'''
        
