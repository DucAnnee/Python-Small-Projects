alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    new_text = ''
    for letter in text:
        temp = ord(letter)
        temp += shift
        new_letter = chr(temp)
        new_text += new_letter
    print(new_text) 

def decrypt(text, shift):
    new_text = ''
    for letter in text:
        temp = ord(letter)
        temp -= shift
        new_letter = chr(temp)
        new_text += new_letter
    print(new_text) 

if direction == "encode":
    encrypt(text, shift)
else:
    decrypt(text, shift)