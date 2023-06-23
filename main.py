from morse_dictionary import morse_dict

text = input("Input some text: ")

[print(morse_dict[char.upper()], end="  ") for char in text]