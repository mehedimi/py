#!/usr/bin/env python3
import string


def decrypt_caesar_cypher(text: str, distance: int):
    output = ''
    alphabet = string.ascii_letters

    for character in text:
        if character in alphabet:
            start = 65 if character.isupper() else 97
            output += chr((ord(character) - distance - start) % 26 + start)
        else:
            output += character
    return output


txt = input('Enter your text: ').strip()
dis = int(input('Enter distance value: ').strip())

print('Output: %s' % decrypt_caesar_cypher(txt, dis))
