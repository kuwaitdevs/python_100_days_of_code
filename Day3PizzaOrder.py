print("Welcome to python pizza Deliveries!")

size = ''
while size not in ['S', 'M', 'L']:
    size =  input("What is your pizza size? \nS, M or L: ").upper()

pepperoni = ''
while pepperoni not in ['Y', 'N']:
    pepperoni = input("Do you want pepperoni on your pizza?\n Y or N: ").upper()

extra_cheese = ''
while extra_cheese not in ['Y', 'N']:
    extra_cheese = input("Do you want extra cheese?\n Y or N: ").upper()

total = 0
bill_breakdown = '------------\n'

if size == 'S':
    total += 5
    bill_breakdown += 'small size \t\tKWD 5'
elif size == 'M':
    total += 10
    bill_breakdown += 'medium size \t\tKWD 10'
else:
    total += 15
    bill_breakdown += 'large size \t\tKWD 15'

bill_breakdown += '\n'

if pepperoni == 'Y':
    if size == 'S':
        total += 5
        bill_breakdown += 'with pepperoni \t\tKWD 5'
    elif size == 'M':
        total += 7
        bill_breakdown += 'with pepperoni \t\tKWD 7'
    else:
        total += 9
        bill_breakdown += 'with pepperoni \t\tKWD 9'
else:
    bill_breakdown += 'no pepperoni \t\tKWD 0'
    total += 0

bill_breakdown += '\n'

if extra_cheese == 'Y':
    if size == 'S':
        total += 5
        bill_breakdown += 'with extra cheese \tKWD 5'
    elif size == 'M':
        total += 7
        bill_breakdown += 'with extra cheese \tKWD 7'
    else:
        total += 9
        bill_breakdown += 'with extra cheese \tKWD 7'
else:
    bill_breakdown += 'no extra cheese \tKWD 0'
    total += 0

print(bill_breakdown)
print(f'total: \t\t\tKWD {total}')

