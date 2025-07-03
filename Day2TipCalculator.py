print("Welcome to the tip calculator!")
print("What was the total bill? $")
total = float(input())
tip = 0

while tip == 0:
    print("How much tip would you like to give? 10, 12 or 15?")
    tip = int(input())

    if(tip != 10 and tip != 12 and tip != 15):
        tip = 0
        print("Invalid tip percentage")

print("How many people to split the bill?")
people_to_split = int(input())

total_per_person = total / people_to_split
total_per_person_with_tip = total_per_person + (total_per_person * (tip / 100))

print(f"Each person should pay: ${total_per_person_with_tip}")