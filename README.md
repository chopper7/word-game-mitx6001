## word-game-mitx6001
####Simple word-making game based on "Scrabble" scoring.

_From edX MITx 6.001x, "Introduction to Computer Science With Python"_

[ Instructions were: ]

### Problem Set 4... **A Word Game**

In this problem set, you'll implement... the 6.00 wordgame!...

This game is a lot like _Scrabble_ or _Words With Friends_, if you've played those. Letters are dealt to players, who then construct one or more words out of their letters. Each valid word receives a score, based on the length of the word and the letters in that word.

The rules of the game are as follows:

_Dealing_
- A player is dealt a hand of n letters chosen at random (assume ```n=7``` for now).
- The player arranges the hand into as many words as they want out of the letters, using each letter at most once.
- Some letters may remain unused (these won't be scored).

_Scoring_
- The score for the hand is the sum of the scores for each word formed.
- The score for a word is the sum of the points for letters in the word, multiplied by the length of the word, plus 50 points if all n letters are used on the first word created.
- Letters are scored as in _Scrabble_; A is worth 1, B is worth 3, C is worth 3, D is worth 2, E is worth 1, and so on. We have defined the dictionary ```SCRABBLE_LETTER_VALUES``` that maps each lowercase letter to its _Scrabble_ letter value.
- For example, "weed" would be worth 32 points ```((4+1+1+2)``` for the four letters, then multiply by ```len('weed')``` to get ```(4+1+1+2)*4 = 32)```. Be sure to check that the hand actually has 1 "w", 2 "e"s, and 1 "d" before scoring the word!
- As another example, if ```n=7``` and you make the word "waybill" on the first try, it would be worth 155 points (the base score for "waybill" is ```(4+1+4+3+1+1+1)*7=105```, plus an additional 50 point bonus for using all n letters).

_Sample Output_
Here is how the game output will look!

```
Loading word list from file...
   83667 words loaded.
Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: p z u t t t o
Enter word, or a "." to indicate that you are finished: tot
"tot" earned 9 points. Total: 9 points
Current Hand: p z u t
Enter word, or a "." to indicate that you are finished: .
Total score: 9 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: r
Current Hand: p z u t t t o
Enter word, or a "." to indicate that you are finished: top
"top" earned 15 points. Total: 15 points
Current Hand: z u t t
Enter word, or a "." to indicate that you are finished: tu
That is not a valid word. Please choose another word
Current Hand: z u t t
Enter word, or a "." to indicate that you are finished: .
Total score: 15 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: a q w f f i p
Enter word, or a "." to indicate that you are finished: paw
"paw" earned 24 points. Total: 24 points
Current Hand: q f f i
Enter word, or a "." to indicate that you are finished: qi
"qi" earned 22 points. Total: 46 points
Current Hand: f f
Enter word, or a "." to indicate that you are finished: .
Total score: 46 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: a r e t i i n
Enter word, or a "." to indicate that you are finished: inertia
"inertia" earned 99 points. Total: 99 points
Run out of letters. Total score: 99 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: e
```

.... [ The file ```words.txt```, a list of valid words for the game, was provided in the course materials ] ....  

The file ```ps4a.py``` has a number of already implemented functions you can use while writing up your solution. You can ignore the code between the following comments, though you should read and understand how to use each helper function...

This problem set is structured so that you will write a number of modular functions and then glue them together to form the complete word playing game. Instead of waiting until the entire game is ready, you should test each function you write, individually, before moving on. This approach is known as unit testing, and it will help you debug your code.

We have provided several test functions to get you started. After you've written each new function, unit test by running the file ```test_ps4a.py``` to check your work.

If your code passes the unit tests you will see a SUCCESS message; otherwise you will see a FAILURE message. These tests aren't exhaustive. You will want to test your code in other ways too....
 
These are the provided test functions:

```test_getWordScore()``` : Test the getWordScore() implementation.

```test_updateHand()``` : Test the updateHand() implementation.

```test_isValidWord()``` : Test the isValidWord() implementation.

