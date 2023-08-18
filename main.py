# Import the logo from the art.py file for display
from art import logo
print(logo)

# Define the alphabet list with both lowercase and wrapped-around characters
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Define the Caesar cipher function
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    
    # If decoding, reverse the shift by making it negative
    if cipher_direction == "decode":
        shift_amount *= -1
        
    # Iterate through each character in the input text
    for char in start_text:
        # Check if the character is a letter in the alphabet
        if char in alphabet:
            position = alphabet.index(char)
            
            # Calculate the new position with the shift
            new_position = position + shift_amount
            
            # Append the shifted character to the end_text
            end_text += alphabet[new_position]
        else:
            # If the character is not a letter, keep it unchanged
            end_text += char
    
    # Print the encrypted/decrypted result
    print(f"Here's the {cipher_direction}d result: {end_text}")

# Initialize a loop for the program to run repeatedly
should_end = False
while not should_end:
    # Get user inputs for cipher direction, text, and shift
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    # Ensure the shift value stays within the alphabet range
    shift = shift % 26

    # Call the caesar function to perform encryption/decryption
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    # Ask the user if they want to restart the program
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")


#                    *****SAMPLE OUTPUT******


#  ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
# a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
# 8b         ,adPPPPP88 8PP"  `"Y8ba,  ,adPPPPP88 88
# "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
#  `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
#             88             88
#            ""             88
#                           88
#  ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
# a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
# 8b         88 88       d8 88       88 8PP" 88
# "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
#  `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
#               88
#               88

# Type 'encode' to encrypt, type 'decode' to decrypt:
# encode
# Type your message:
# hello world
# Type the shift number:
# 9
# Here's the encoded result: qnuux fxaum
# Type 'yes' if you want to go again. Otherwise type 'no'.
# no
# Goodbye