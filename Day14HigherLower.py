import random

game_over = False
score = 0

items_to_compare = [
    {
        "label": "Ethereum",
        "followers": 4_000_000,
    },
    {
        "label": "Bitcoin",
        "followers": 8_590_000,
    },
    {
        "label": "Tether",
        "followers": 569_000,
    },
    {
        "label": "Binance",
        "followers": 16_000_000,
    },
    {
        "label": "Solana",
        "followers": 3_840_000,
    },
    {
        "label": "Ripple",
        "followers": 3_200_000,
    }
]


# initial thing
item_to_compare_1 = random.choice(items_to_compare)
items_to_compare = [x for x in items_to_compare if x["label"] != item_to_compare_1["label"]]

# main loop
while not game_over:

    if len(items_to_compare) == 0:
        game_over = True
        break

    item_to_compare_2 = random.choice(items_to_compare)
    items_to_compare = [x for x in items_to_compare if x["label"] != item_to_compare_2["label"]]

    print(f"Who has more followers? A.{item_to_compare_1['label']} or B.{item_to_compare_2['label']}")
    user_choice = input()

    if str.lower(user_choice) == 'a' and item_to_compare_1["followers"] > item_to_compare_2["followers"]:
        score += 1
        print(f"Correct!")
        print(f"Current score is: {score}!")
    elif str.lower(user_choice) == 'b' and item_to_compare_1["followers"] < item_to_compare_2["followers"]:
        score += 1
        print(f"Correct!")
        print(f"Current score is: {score}!")
        item_to_compare_1 = item_to_compare_2
    else: 
        game_over = True
        print(f"Wrong!")
        break

print(f"Final Score is: {score}")
    