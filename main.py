from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number [from 1 to 25]:\n"))
while shift > 25:
    shift = int(input("Type the shift number [from 1 to 25]:\n"))

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    for letter in start_text:
        if letter.isalpha():
            position = alphabet.index(letter)
            if cipher_direction == "encode":
                shifted_position = position + shift_amount
                if shifted_position > len(alphabet):
                    shifted_position -= len(alphabet)
                end_text += alphabet[shifted_position]
            elif cipher_direction == "decode":
                shifted_position = position - shift_amount
                if shifted_position < 0:
                    shifted_position += len(alphabet)
                end_text += alphabet[shifted_position]
        else:
            end_text += letter
    print(f"The {cipher_direction}d text is {end_text}")


caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.