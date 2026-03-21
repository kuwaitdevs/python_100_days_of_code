true_array = ['t', 'r', 'u', 'e']
love_array = ['l', 'o', 'v', 'e']

def calculate_love_score(name1, name2):
    first_number = 0
    second_number = 0

    for person_char in name1:
        for true_char in true_array:
            if(person_char == true_char):
                first_number += 1
        for love_char in love_array:
            if(person_char == love_char):
                second_number += 1

    
    for person_char in name2:
        for true_char in true_array:
            if(person_char == true_char):
                first_number += 1
        for love_char in love_array:
            if(person_char == love_char):
                second_number += 1

    print(f"{first_number}{second_number}")

calculate_love_score("Kanye West", "Kim Kardashian")
