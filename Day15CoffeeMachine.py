# coin operated
# penny     = .01 $
# nickel    = .05 $
# dime      = .10 $
# quarter   = .25 $

# requirements:
# print a report
# how much resources left

# example:
# > report
# Water:    300ml
# Milk:     200ml
# Coffee:   100g
# Money:    0 $

# check if the resources are sufficient 
import time

machine_state = {
    "water": {
        "value": 300,
        "unit": "ml"
    },
    "milk": {
        "value": 300,
        "unit": "ml"
    },
    "coffee": {
        "value": 100,
        "unit": "g"
    },
    "money": {
        "value": 0,
        "unit": "$"
    },
}

machine_items = {
    "espresso": {
        "index": "1",
        "label": "Espresso",
        "water": 50,
        "milk": 0,
        "coffee": 15,
        "money": 1.5,
    },
    "latte": {
        "index": "2",
        "label": "Latte",
        "water": 200,
        "milk": 150,
        "coffee": 24,
        "money": 2.5,
    },
    "cappuccino": {
        "index": "3",
        "label": "Cappuccino",
        "water": 250,
        "milk": 100,
        "coffee": 24,
        "money": 2.5,
    }
}

def print_machine_report():
    for item_key in machine_state:
        item_value = machine_state[item_key]["value"]
        item_unit = machine_state[item_key]["unit"]
        print(f"{item_key}: {item_value} {item_unit}")
    print("===============")


def program_prompt():
    print("Welcome to Coffee Machine Inc.")
    for item_key in machine_items:
        print(f"{machine_items[item_key]['index']}. {machine_items[item_key]['label']}")

    return input("What would you like? (enter item number) / or type report \n> ")


def accept_money_and_return_total():
    pennies     = float(input("How many pennies\n> "))
    dimes       = float(input("How many dimes\n> "))
    quarters    = float(input("How many quarters\n> "))
    nickels     = float(input("How many nickels\n> "))
    return (pennies * .01) + (nickels * .05) + (quarters * .25) + (dimes * .1)

def print_invalid_choice():
    print("Invalid Choice.")
    print("===============")

def print_not_enough_money():
    print("Not enough money. Money refunded.")
    print("===============")

def machine_has_enough_resources(choice):
    if choice['coffee'] > 0 and machine_state["coffee"]["value"] - choice['coffee'] < 0:
        print("not enough coffee")
        print("===============")
        return False
    elif choice['water'] > 0 and machine_state["water"]["value"] - choice['water'] < 0:
        print("not enough water")
        print("===============")
        return False
    elif choice['milk'] > 0 and machine_state["milk"]["value"] - choice['milk'] < 0:
        print("not enough milk")
        print("===============")
        return False
    else:
        return True

def create_machine_item(choice):
    machine_state["coffee"] = machine_state["coffee"]["value"] - choice['coffee']
    machine_state["water"] = machine_state["water"]["value"] - choice['water']
    machine_state["milk"] = machine_state["milk"]["value"] - choice['milk']
    print('Preparing your drink.', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('Pouring.', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.', end='')

def item_ready(choice):
    print(f"Your {choice['label']} is ready! Enjoy!")
    print("===============")

def print_not_enough_resources():
    print("Sorry the machine does not have enough resources at the moment.")
    print("===============")


def get_selected_item(user_choice_string):
    for item_key in machine_items:
        if machine_items[item_key]['index'] == user_choice_string:
            
            return machine_items[item_key]


while True:
    user_choice_string = program_prompt()

    if user_choice_string == 'report':
        print_machine_report()
        continue

    selected_machine_item = get_selected_item(user_choice_string)

    if selected_machine_item == None:
        print_invalid_choice()
        continue

    if not machine_has_enough_resources(selected_machine_item):
        print_not_enough_resources()
        continue

    total_money_in_dollars = accept_money_and_return_total()

    if total_money_in_dollars < selected_machine_item['money']:
        print_not_enough_money()
        continue

    change = total_money_in_dollars - selected_machine_item['money']

    create_machine_item(selected_machine_item)
    item_ready(selected_machine_item)

    print(f"Your change is: {change} $")
    print("===============")