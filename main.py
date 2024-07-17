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
    print(f"The {cipher_direction}d text is {end_text}")


caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

#TODO-3: What happens if the user enters a number/symbol/space?
#Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
#e.g. start_text = "meet me at 3"
#end_text = "•••• •• •• 3"

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.