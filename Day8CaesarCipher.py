original_alphabet   = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
                     'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'u', 'z']
shift_alphabet      = []
original_alphabet_length = len(original_alphabet)

continue_answer = 'yes'
encoded_message = ""
decoded_message = ""

def create_shift_alphabet(shift_number):
    temp_shift_alphabet = []

    for index, char in enumerate(original_alphabet):
        if index + shift_number >= original_alphabet_length:
            excess = index + shift_number
            new_shift_number = excess - original_alphabet_length
            temp_shift_alphabet.append(original_alphabet[new_shift_number])
        else:
            temp_shift_alphabet.append(original_alphabet[index + shift_number])
    return temp_shift_alphabet

def encode(shift_alphabet, user_message):
    temp_encoded_message = []
    
    for plain_text_char in user_message:
        if plain_text_char not in shift_alphabet:
            temp_encoded_message.append(plain_text_char)
        else: 
            original_alphabet_char_index = original_alphabet.index(plain_text_char)
            temp_encoded_message.append(shift_alphabet[original_alphabet_char_index])

    return temp_encoded_message

def decode(shift_alphabet, user_message):
    temp_decoded_message = []
    
    for encoded_text_char in user_message:
        if encoded_text_char not in original_alphabet:
            temp_decoded_message.append(encoded_text_char)
        else: 
            shift_alphabet_char_index = shift_alphabet.index(encoded_text_char)
            temp_decoded_message.append(original_alphabet[shift_alphabet_char_index])

    return temp_decoded_message

# main loop
while continue_answer != 'no':
    user_choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if user_choice == 'encode':
        user_message = str.lower(input("Type your message:\n"))
        shift_number = int(input("Type your shift number:\n"))
        shift_alphabet = create_shift_alphabet(shift_number)
        encoded_message = encode(shift_alphabet, user_message)
        print("Here is the encoded result: ", "".join(encoded_message))
    else:
        user_message = str.lower(input("Type your message:\n"))
        shift_number = int(input("Type your shift number:\n"))
        shift_alphabet = create_shift_alphabet(shift_number)
        decoded_message = decode(shift_alphabet, user_message)
        print("Here is the decoded result: ", "".join(decoded_message))
    
    continue_answer = input("Type yes if you want to go again. Otherwise type 'no'.")

