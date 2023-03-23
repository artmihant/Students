from random import randint

def guessing_game():
    answer = randint(0, 100)

    while True:
        guess = int(input('Ваша догадка: '))
        if answer == guess:
            print('You win!')
            break
        elif answer < guess:
            print('lower!')
        else:
            print('greater!')

guessing_game()