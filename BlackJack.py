import random
import time

cards_dict = {
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'king': 10,
    'jack': 10,
    'queen': 10,
    'ace': 1,
}


def calc_points(card_list: list) -> int:
    points = 0
    for card in card_list:
        points += cards_dict[card]
    return points


def draw_card(card_list: list):
    key, val = (random.choice(list(cards_dict.items())))
    card_list.append(key)


def player_choice(choice: list):
    choice.clear()
    response = input("Do you want to stand or hit?\n")
    choice.append(response)


def show_hand(card_list: list) -> list:
    return card_list


def talk1():
    print("Let's draw the first hand...")
    print("Cheers everyone")
    time.sleep(2)


def talk2():
    print("The second hand it's coming")
    print("Watch out, they are comin.")
    time.sleep(1)


def talk3():
    print("Let's the battle begin ->{Nah I'd win}")


def talk4():
    print("Bot turn")


def talk5():
    print("Bot drew all the cards let's see who wins")


def game():
    misc_dict = {
        'p': [],
        'c': [],
        'b': [],
        'talk1': talk1,
        'talk2': talk2,
        'talk3': talk3,
        'talk4': talk4,
        'talk5': talk5,
    }
    continue_game = True
    while (continue_game):
        player_cards = misc_dict['p']
        choice = misc_dict['c']
        bot_cards = misc_dict['b']
        player_points = 0
        bot_points = 0
        player_cards.clear()
        choice.clear()
        bot_cards.clear()
        misc_dict['talk1']()
        draw_card(player_cards)
        draw_card(bot_cards)
        print(f"Player has {show_hand(player_cards)}")
        time.sleep(1)
        print(f"Bot has {show_hand(bot_cards)}")
        time.sleep(1)

        misc_dict['talk2']()
        draw_card(player_cards)
        draw_card(bot_cards)
        print(f"Player has {show_hand(player_cards)}")
        time.sleep(1)
        print(f"Bot has {show_hand(bot_cards[:1])} and x")

        misc_dict['talk3']()
        # game_is_finished = False

        enter = True
        player_choice(choice)
        while enter is True or choice[0] == 'Hit' or choice[0] == 'Stand':
            if choice[0] == 'Stand':
                if 'ace' in player_cards:
                    player_points = calc_points(player_cards)
                    print(f"Your points {player_points + 10}")
                else:
                    player_points = calc_points(player_cards)
                    print(f"Your points {player_points}")
                misc_dict['talk4']()
                time.sleep(1)

                bot_points = calc_points(bot_cards)
                ind = 2
                while bot_points < 17:
                    draw_card(bot_cards)
                    n_p = calc_points(bot_cards[ind:ind + 1])
                    ind += 1
                    bot_points += n_p

                misc_dict['talk5']()
                time.sleep(1)

                if bot_points < player_points <= 21:
                    print(f"Player has won with {player_points}")
                elif player_points < bot_points <= 21:
                    print(f"Bot has won with {bot_points}")
                elif bot_points == player_points > 21:
                    print("You both lose")
                elif player_points > 21 >= bot_points:
                    print(f"Bot has won with {bot_points}")
                elif bot_points > 21 >= player_points:
                    print(f"Player has won with {player_points}")

                rasp = input("Do you want to play another game (Y/N)?\n")
                if rasp == 'Y':
                    continue_game = True
                    break
                else:
                    continue_game = False
                    break

            elif choice[0] == "Hit":
                print("Player: hit")
                time.sleep(1)
                draw_card(player_cards)
                print(f"You drew a new card, your hand is {player_cards}")
                enter = False

            player_choice(choice)


game()
