import random

#A while true loop to prompt the user for a level which determines the range at which the random number should be in
while True:
    try:
        level = int(input("Level: "))
        if level < 1:
            continue
        ran_num = random.randint(1, level)
        break
    except ValueError:
        continue
#A while true loop to prompt the user to guess the number and depending on the guess will lead to printing the appropriate text
while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1:
            continue
        if guess < ran_num:
            print("Too small!")
            continue
        elif guess > ran_num:
            print("Too large!")
            continue
        elif guess == ran_num:
            print("Just right!")
            break
    except ValueError:
        continue