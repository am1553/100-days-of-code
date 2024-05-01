ascii_art = r"""
                                                             
           88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88                                             
"""

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']


def encode(text, shift):
    text_arr = list(text)
    encoded_text = []
    for letter in text_arr:
        lower_letter = letter.lower()
        if lower_letter in alphabets:
            letter_index = alphabets.index(lower_letter)
            new_letter_index = letter_index + shift
            if new_letter_index < len(alphabets):
                new_letter = alphabets[new_letter_index]
                encoded_text.append(new_letter)
            else:
                difference = new_letter_index - len(alphabets)
                encoded_text.append(alphabets[difference])
        else:
            encoded_text.append(lower_letter)

    return str.join('', encoded_text)


def decode(text, shift):
    decoded_text = encode(text, shift * -1)
    return decoded_text


def caesar_cipher():
    redo = 'yes'

    while redo == 'yes':
        cipher_type = input("Type 'encode' to encrypt or 'decode' to decrypt: \n")
        message = input("Type message to encrypt: \n")
        shift = int(input("Type shift value to encrypt: \n"))

        if cipher_type == 'encode':
            result = encode(message, shift)
        else:
            result = decode(message, shift)
        print("Here's the encoded result: ", result)
        redo = input("Type 'yes' if you want to go again. Otherwise type 'no'.")


if __name__ == '__main__':
    caesar_cipher()
