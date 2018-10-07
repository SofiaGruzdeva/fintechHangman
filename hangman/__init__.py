"""Have a nice evening playing this game"""
import random
GAME_DICT = ['circle', 'triangle', 'rectangle', 'square', 'trapezoid']


def input_check(guess, used):
    """Check input string whatever you can use it in current Hangman game"""
    guess = str.strip(guess)
    if len(guess) != 1:
        print('Only one symbol is allowed.\n')
        return False
    if not guess.isalpha():
        print('Only letters are allowed.\n')
        return False
    if guess in used:
        print('Enter letter you did not used\n')
        return False
    return guess.lower()


def try_guess(guess, current_game, game_word):
    """Test input letter"""
    result = False
    for i, value in enumerate(game_word):
        if value == guess:
            result = True
            current_game[i] = guess
    return current_game, result


def game(game_word, max_err=5):
    """The game itself"""
    current_game = ['*'] * len(game_word)
    counter = 0
    used = []
    while counter < max_err and '*' in current_game:
        guess = input_check(input('Guess a letter:\n'), used)
        if guess:
            used.append(guess)
            current_game, result = try_guess(guess, current_game, game_word)
            if not result:
                counter += 1
                print('Missed, mistake ', counter, ' out of ', max_err, '.\n')
            else:
                print('Hit!\n')
        print('The word: ', end='', flush=True)
        for i in current_game:
            print(i, sep=' ', end='', flush=True)
        print('\n')
    return counter


def main():
    """Enter and finish the game"""
    game_word = random.choice(GAME_DICT)
    max_errors = 5
    counter = game(game_word, max_errors)
    if counter >= max_errors:
        print('You lost!\n')
    else:
        print('You won!\n')


if __name__ == '__main__':
    main()
