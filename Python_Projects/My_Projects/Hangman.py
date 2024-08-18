import random

words = ['settle', 'funnel', 'extend', 'optimal', 'match', 'multiple', 'captive', 
         'weaver', 'dinner', 'plateau', 'mutation', 'snob', 'market', 'foreman', 
         'allergen', 'expert', 'thinking', 'throw', 'dream', 'excite', 'strain', 
         'refinery', 'funded', 'marching', 'condone', 'wares', 'born', 'flipping', 
         'dent', 'mount', 'backpack', 'quaker', 'manic', 'there', 'seed', 'kickoff', 
         'pruning', 'wick', 'affirm', 'rabbit', 'plague', 'strict', 'schema', 'coin', 
         'prolong', 'coherent', 'mend', 'suffer', 'rage', 'knock', 'crust', 'aloof', 
         'brown', 'soup', 'smite', 'lying', 'climb', 'film', 'reusable', 'downfall', 
         'emerald', 'tired', 'emigrate', 'coral', 'silence', 'sailing', 'humidity', 
         'bluff', 'shampoo', 'endanger', 'mystic', 'guide', 'bishop', 'coat', 'chill', 
         'main', 'medley', 'square', 'figure', 'windy']

def get_word():
    word = random.choice(words)
    return word.upper()

def game_play(word):
    full_word = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    attempts = 6
    print("Lets play Hangman!")
    print(display_hangman(attempts))
    print(full_word)
    print("\n")
    while not guessed and attempts > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You have already guessed {guess}")
            elif guess not in word: 
                print(f"{guess} is not in the word")
                attempts -= 1
                guessed_letters.append(guess)
            else:
                print(f"Well done! {guess} is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(full_word)
                indexed = [i for i, letter in enumerate(word) if letter == guess]
                for index in indexed:
                    word_as_list[index] = guess
                full_word = "".join(word_as_list)
                if "_" not in full_word:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed the word {guess}")
            elif guess != word:
                print(f"{guess} is not the word!")
                attempts -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("That is not a valid guess")
        print(display_hangman(attempts))
        print(full_word)
        print("\n")
    if guessed: 
        print("Congrats, you guessed the word!")
    else:
        print("Sorry, you ran out of tries!")
        print(f"The word was {word}")
    
def display_hangman(attempts):
    stages = [
        """
        _______
        |      |
        |      0
        |     \|/
        |     / \\
        |
        |
        """,
                """
        _______
        |      |
        |      0
        |     \\|/
        |     / 
        |
        |
        """,
                """
        _______
        |      |
        |      0
        |     \\|/
        |     
        |
        |
        """,
                """
        _______
        |      |
        |      0
        |     \|
        |     
        |
        |
        """,
                """
        _______
        |      |
        |      0
        |      |
        |   
        |
        |
        """,
                """
        _______
        |      |
        |      0
        |     
        |      
        |
        |
        """,
                """
        _______
        |      |
        |      
        |     
        |      
        |
        |
        """
    ]
    return stages[attempts]


def main():
    word = get_word()
    game_play(word)
    while input("Would you like to play again? Type Y or N: ").upper() == "Y":
        word = get_word()
        game_play(word)
        
        
        
main()
    
