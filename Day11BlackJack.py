import random

standard_cards_list = [
    {"value": 11, "label": "A"},
    {"value": 2,  "label": "2"},
    {"value": 3,  "label": "3"},
    {"value": 4,  "label": "4"},
    {"value": 5,  "label": "5"},
    {"value": 6,  "label": "6"},
    {"value": 7,  "label": "7"},
    {"value": 8,  "label": "8"},
    {"value": 9,  "label": "9"},
    {"value": 10, "label": "10"},
    {"value": 10, "label": "K"},
    {"value": 10, "label": "Q"},
    {"value": 10, "label": "J"},
]

standard_suits_list = ["♥", "♦", "♣", "♠"]

# Generate deck
def generate_deck():
    temp_deck = []
    for card in standard_cards_list:
        for suit in standard_suits_list:
            new_card = card.copy()
            new_card["suit"] = suit
            temp_deck.append(new_card)
    return temp_deck

def pick_card():
        selected_card_index = random.randrange(0, len(deck), 1)
        selected_card = deck[selected_card_index]
        deck.pop(selected_card_index)
        return selected_card

def show_player_hand():
    hand = ''

    for card in player_hand:
          hand += f"{card['suit']}{card['label']} "
    return hand

def show_computer_hand(show_all):
    hand = ''
    
    if show_all:
         for card in computer_hand:
            hand += f"{card['suit']}{card['label']} "
    else:
        hand += f"{computer_hand[0]['suit']}{computer_hand[0]['label']}"

    return hand

def calculate_hand(hand):
    total = 0
    ace_in_hand = False

    for card in hand:
        total += card['value']

    for card in hand:
        if card['label'] == 'A':
            ace_in_hand = True
            break

    if ace_in_hand and total > 21:
        total = 0
        # recalculate
        for card in hand:
            if card['label'] == 'A':
                total += 1
            else:
                total += card['value']

    return total

def is_blackjack(hand):
    total = 0
    for card in hand:
        total += card['value']

    if len(hand) == 2 and total == 21:
        return True
    else:
        return False

play_another_game = 'y'
player_chips = 10
bet = 0

while play_another_game == 'y':

    deck = []
    player_hand = []
    computer_hand = []
    game_over = False
    
    deck = generate_deck()

    if player_chips <= 0:
        game_over = True
        play_another_game = 'n'
        print("No more chips to bet! Game Over")
        continue

    play_another_game= input("Do you want to play BlackJack? y/n\n>")
    if play_another_game == 'n':
        continue

    player_hand.append(pick_card())
    player_hand.append(pick_card())

    computer_hand.append(pick_card())
    computer_hand.append(pick_card())

    while game_over == False:
        if player_chips <= 0:
            game_over = True
            print("No more chips to bet! Game Over")
            continue

        print(f"Your chips: {player_chips} $")
        if bet == 0:
            bet = int(input("How many chips do you want to bet?:\n>"))

            while bet > player_chips or bet <= 0:
                bet = int(input(f"Invalid value, you only have {player_chips} chips?:\n>"))

        print(f"Your chips {player_chips}")
        print(f"Your hand {show_player_hand()}")
        print(f"Computer's hand: {show_computer_hand(False)}")

        player_total = calculate_hand(player_hand)
        computer_total = calculate_hand(computer_hand)

        if player_total == 21:
            game_over = True
            print("You win! 21")
            player_chips += bet
            bet = 0
        elif player_total > 21:
            game_over = True
            print("Sorry, you lose! You passed 21")
            player_chips -= bet
            bet = 0
        elif is_blackjack(player_hand):
            game_over = True
            print("BackJack! you win.")
            player_chips += bet
            bet = 0
        else:
            hit = input("Type 'y' to get another card, type 'n' to pass:\n>")

            if hit == 'y':
                player_hand.append(pick_card())
            else:
                game_over = True

                while computer_total < 17:
                    computer_hand.append(pick_card())
                    computer_total = calculate_hand(computer_hand)

                print(f"Computer's hand: {show_computer_hand(True)}")
                
                if computer_total > 21:
                    print("You win! Computer passed 21")
                    player_chips += bet
                    bet = 0
                elif player_total == computer_total:
                    print("Draw!")
                    bet = 0
                elif is_blackjack(computer_hand):
                    print("You lose!, Computer got a BlackJack!")
                    player_chips -= bet
                    bet = 0
                elif player_total > computer_total:
                    print("You win! You are closer to 21 than Computer")
                    player_chips += bet
                    bet = 0
                else:
                    print("You lose! Computer is closer to 21 than you")
                    player_chips -= bet
                    bet = 0
                    