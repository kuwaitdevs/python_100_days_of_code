import random

possible_moves = ['Rock', 'Paper', 'Scissors']
winning_moves = [[0,2], [1,0], [2,1]]

print("Welcome to Rock Paper Scissors!")
print("Select:")
print("1- Rock")
print("2- Paper")
print("3- Scissors")

human_move_index = input("> ")

try:
    human_move_index = int(human_move_index)
    human_move_index = human_move_index - 1

    if human_move_index > 2 or human_move_index < 0:
        print("invalid choice")
    
    human_move = possible_moves[human_move_index]

    computer_move_index = random.randint(0, 2)
    computer_move = possible_moves[computer_move_index]

    print(f'You played: \t\t{human_move}')
    print(f'Computer played: \t{computer_move}')

    if human_move_index == computer_move_index:
        print('Tie!')
    else:
        human_won = False
        for move in winning_moves:
            if move[0] == human_move_index and move[1] == computer_move_index:
                human_won = True
                break;
        
        if human_won:
            print('You Win!')
        else:
            print('You Lose!')

except:
    print("invalid choice")
