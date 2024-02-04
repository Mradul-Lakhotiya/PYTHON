import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
choice_to_continue = 'y'

while (choice_to_continue == 'y'):
    player_cards = []
    player_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))

    computer_cards = []
    computer_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))

    print(f"The player cards are: {player_cards} sum: {sum(player_cards)}")
    print(f"The Computer card is: {computer_cards[0]} sum: {computer_cards[0]}")

    print("1. Pick another card")
    print("0. Show cards")
    choice = int(input("Choice: "))

    if choice == 1:
        player_cards.append(random.choice(cards))
        print(f"The player cards are: {player_cards} sum: {sum(player_cards)}")
        print(f"The Computer card is: {computer_cards} sum: {sum(computer_cards)}")
    else:
        print(f"The Computer card is: {computer_cards} sum: {sum(computer_cards)}")

    if 11 in player_cards and sum(player_cards) > 21:
        player_cards[player_cards.index(11)] = 1

    if sum(player_cards) > 21:
        print("YOU LOSE")

    while sum(computer_cards) < 17:
        computer_cards.append(random.choice(cards))
        if 11 in computer_cards and sum(computer_cards) > 21:
            computer_cards[computer_cards.index(11)] = 1

        print(f"The Computer cards are: {computer_cards} sum: {sum(computer_cards)}")

    if sum(computer_cards) == sum(player_cards):
        print("DRAW")
    elif sum(computer_cards) > 21:
        print("YOU WIN")
    elif sum(computer_cards) > sum(player_cards):
        print("YOU LOSE")
    else:
        print("YOU WIN")
    
    print("DO YOU WANT TO CONTINUE")
    choice_to_continue = input("y for Yes any other key for no : ")[0]
