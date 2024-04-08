
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#text = input("Type your message:\n").lower()
#shift = int(input("Type the shift number:\n"))
#shift = shift % 26


# def encrypt(plain_text, shift_amount):
# cipher_text = ""
# for letter in plain_text:
# position = alphabet.index(letter)
# new_position = position+shift_amount
# new_letter = alphabet[new_position]
# cipher_text += new_letter
# print(f"The encoded text is {cipher_text}")
# def decrypt(cipher_text, shift_amount):
# plain_text = ""
# for letter in cipher_text:
# position = alphabet.index(letter)
# new_position = position-shift_amount
# new_letter = alphabet[new_position]
# plain_text += new_letter
# print(f"The decoded text is {plain_text}")


# if direction == 'encode':
# encrypt(text, shift)
# else:
# decrypt(text, shift)


# def ceaser(plain_text,shift_amount):
# for letter in plain_text:
# plain_text=" "
# position=alphabet.index(letter)
# if direction=='encode':
# new_position=position+shift_amount
# print(f"The encode is{plain_text}")
# elif direction=='decode':
# new_position=position-shift_amount
# print(f"The decode is{plain_text}")
# else:
# print("Wrong Input")
# new_letter=alphabet[new_position]
# plain_text += new_letter
# print(f"The code is{plain_text}")
# ceaser(text,shift)

def ceaser(start_text, cipher_direction, shift_amount):
    end_text = ""
    if cipher_direction=='decode':
        shift_amount*=-1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position=position+shift_amount 
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}")
from art import logo
print(logo)
code_continue=False
while not code_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    ceaser(start_text=text, cipher_direction=direction, shift_amount=shift)

    result=input("Type 'Yes' if you want to continue and 'No' if you want to stop")
    if result=='No':
        code_continue=True
        print("Goodbye")

