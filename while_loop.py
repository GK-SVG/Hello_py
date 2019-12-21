guess_count = 0
guess_limit = 3
secret_number = 9
while guess_count<guess_limit:
    guess_number = input('Guess: ')
    if int(guess_number) == secret_number:
        print('YOU WIN!')
        guess_count = 3
    else:
        guess_count += 1
        if guess_count == 3:
            print('YOU LOSE!')
