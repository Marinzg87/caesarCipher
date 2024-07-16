alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# Main function
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        shifted_position = position + shift_amount
        if shifted_position > len(alphabet):
            shifted_position -= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"The encoded text is {cipher_text}")


def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        shifted_position = position - shift_amount
        if shifted_position < 0:
            shifted_position += len(alphabet)
        plain_text += alphabet[shifted_position]
    print(f"The decoded text is {plain_text}")


if direction == "encode":
    encrypt(text, shift)
else:
    decrypt(text, shift)
