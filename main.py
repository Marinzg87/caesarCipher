alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# Main function
def encrypt(text, shift):
    shifted_index = []
    for char in text:
        shifted_index.append(alphabet.index(char) + shift)
    cipher_text = ""
    for element in shifted_index:
        cipher_text = cipher_text + alphabet[element]

    print(f"The encoded text is {cipher_text}")


encrypt(text, shift)
