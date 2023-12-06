import random


def game():
    start = True
    game_continues = True
    while game_continues is True and start is True:
        player_response = input("Do you want to play it on easy or hard?\n")
        if player_response == 'easy':
            num_range = (1, 50)
            player_health = 8
            rand_num = random.randint(1, 50)
        elif player_response == 'hard':
            num_range = (1, 100)
            player_health = 5
            rand_num = random.randint(1, 100)

        while player_health != 0:
            player_choice = int(input("Guess your number\n"))
            if player_choice > rand_num:
                if player_health - 1 == 0:
                    print(f"You've lost, the number was {rand_num}")
                else:
                    print("Too high")
                player_health -= 1
                print(f"Your health is {player_health}")
            elif player_choice < rand_num:
                if player_health - 1 == 0:
                    print(f"You've lost, the number was {rand_num}")
                else:
                    print("Too low")
                player_health -= 1
                print(f"Your health is {player_health}")
            else:
                print("You've guessed right")
                break
        game_cont = input("Do you want to go on playing(Y/N)?\n")
        if game_cont == 'Y':
            game_continues = True
        elif game_cont == 'N':
            break


game()
