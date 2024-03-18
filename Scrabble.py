import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # in_file: file
    in_file = open(WORDLIST_FILENAME, 'r')
    # word_list: list of strings
    word_list = []
    for line in in_file:
        word_list.append(line.strip().lower())
    print("  ", len(word_list), "words loaded.")
    return word_list


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word: str, n: int) -> int:
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    
    # pre-condition
    assert isinstance(word, str), "word must be a string"
    if len(word) > 0:
        word = word.lower()
        assert word.islower(), "lower conversion fail"
    assert isinstance(n, int)
    assert n > 0, "hand length m must not be 0"
    
    #magic code
    """The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn."""
    word_score = 0
    """
    for each letter in word
        get letter score from dict SCRABBLE_LETTER_VALUES
        add up all the letters score
        
    multiply by length of word
    then bonus calculation
    """
    for letter in word:
        word_score += SCRABBLE_LETTER_VALUES[letter]
    word_score *= len(word)
    if len(word) == n:
        word_score += 50
    
    #post-condition
    assert word_score >= 0, "score calc fail"
    assert isinstance(word_score, int), "score must be int"
    return word_score

# test case
# get_word_score(1233, 7)
# get_word_score("", 7)
# print(get_word_score("weed", 7))
# print(get_word_score("waybill", 7))
# get_word_score("blabla", 0)

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
     Displays the letters currently in the hand.

    For example:
    >>> display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    assert isinstance(hand, dict), "hand must be a dict"
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=" ")       # print all on the same line
    print()                             # print an empty line

display_hand({'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1})
#
# Problem #2: Make sure you understand how this function works and what it does!
#


def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    assert isinstance(n, int), "n is a integer"
    
    hand = {}
    num_vowels = n // 3

    for i in range(num_vowels):
        x = VOWELS[random.randrange(0, len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand


#
# Problem #2: Update a hand by removing letters
#


def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    
    """
    make a hand.copy()
    for every letter in word
        use the letter to look up the handcopy val
        subtract one from handcopy val
    return handcopy
    """
    assert isinstance(hand, dict), "hand must be a dict"
    assert isinstance(word, str), "word must be a string"
    
    handcopy = hand.copy()
    assert isinstance(handcopy, dict), "handcopy must be a dict"
    for letter in word:
        
        print(handcopy[letter])
        if handcopy[letter] > 0: 
            handcopy[letter] -= 1
        else:
            del(handcopy[letter])
        
    print([val >= 0 for val in handcopy.values()])
    assert all([val >= 0 for val in handcopy.values()]) , "the letter cannot be negative"
    
    print(f'{handcopy=}')
    return handcopy
                
l = {'a': 0, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1}
print(update_hand(l, 'quail'))

#
# Problem #3: Test word validity
#
def is_valid_word(word:str, hand:dict, word_list:list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    #pre condition
    """for each letter in word
        if letter in hand
            find the count of letter in word
            and make sure that count is in hand
    """
    assert isinstance(word, str), "word is a string"
    assert isinstance(word_list, list), "word is a list"
    assert isinstance(hand, dict), "hand is a dictionary"
       
    hand_copy = hand.copy()
    for letter in word:
        count = word.count(letter)
        if letter not in hand_copy:
            return False
        elif hand_copy[letter] - count < 0:
            return False
    
    if word not in word_list:
        return False
    assert isinstance(letter, str), "letter is a string"  
    assert isinstance(hand_copy[letter], int), "this is a int"
    return True

#
# Problem #4: Playing a hand
#

def calculate_hand_len(hand):
    """ 
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """
    
    assert isinstance(hand, dict), "hand must be a dictionary"
    count = 0
    for letter in hand:
        count += hand[letter]
    return count

def play_hand(hand, word_list, n):
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
      word_list: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)

    """
    """
    a
    """
    # Keep track of the total score

    # As long as there are still letters left in the hand:

    # Display the hand

    # Ask user for input

    # If the input is a single period:

    # End the game (break out of the loop)

    # Otherwise (the input is not a single period):

    # If the word is not valid:

    # Reject invalid word (print a message followed by a blank line)

    # Otherwise (the word is valid):

    # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line

    # Update the hand

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score

    score = 0
    while calculate_hand_len(hand) > 0:
        player_input = input("please input a word: ")
        print(display_hand(hand))
        if player_input == ".":
            break
        else:
            if is_valid_word(player_input, hand, word_list) == False:
                player_input = 0
                print("word invalid, please input a correct word")
                print("")
            else:
                score += get_word_score(player_input, n)
                print(f"you earn {get_word_score(player_input, n)} points!")
        update_hand(hand, player_input)
    print(f"you earn a total of {score} points!")
    
#
# Problem #5: Playing a game
#

def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.

    2) When done playing the hand, repeat from step 1    
    """
    
    user_input = input("please enter 'n', 'r' or 'e'")
    if user_input == 'n':
        deal_hand(7)
    if user_input == 'r':
        g
    
    print("play_game not yet implemented.")


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
