alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(user_text, shift_amount, user_direction):
    processed_text = ""
    for letter in user_text:
        position = alphabet.index(letter)
        if user_direction == "encode":
            shifted_position = position + shift_amount
            if shifted_position > len(alphabet):
                shifted_position -= len(alphabet)
            processed_text += alphabet[shifted_position]
        elif user_direction == "decode":
            shifted_position = position - shift_amount
            if shifted_position < 0:
                shifted_position += len(alphabet)
            processed_text += alphabet[shifted_position]
    if user_direction == "encode":
        print(f"The encoded text is {processed_text}")
    elif user_direction == "decode":
        print(f"The decoded text is {processed_text}")


caesar(user_text=text, shift_amount=shift, user_direction=direction)
