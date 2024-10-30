# Cooper Lilly
# UWYO COSC 1010
# Submission Date 10/29/24
# HW 02
# Lab Section: 13
# Sources, people worked with, help given to: 
# your
# comments
# here


morse_code_dict = {
    'A': '.-','N': '-.', 'B': '-...', 'O': '---', 'C': '-.-.', 'P': '.--.', 'D': '-..',
    'Q': '--.-', 'E': '.', 'R': '.-.', 'F': '..-.', 'S': '...', 'G': '--.', 'T': '-', 
    'H': '....', 'U': '..-', 'I': '..', 'V': '...-', 'J': '.---', 'W': '.--','K': '-.-', 
    'X': '-..-', 'L': '.-..', 'Y': '-.--', 'M': '--','Z': '--..'}

user_input = input("Enter message to translate into morse code:").upper()

morse_code_output = ""
for char in user_input:
    if char in morse_code_dict.keys():
        morse_code_output = morse_code_output + morse_code_dict[char] + ""
    elif char == "":
        morse_code_output = morse_code_output + ""
print(morse_code_output)