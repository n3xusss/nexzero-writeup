morse_code_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9'
}

def morse_to_text(morse_code):
    text = ''
    morse_words = morse_code.split('_')
    for morse_word in morse_words:
        morse_chars = morse_word.split(' ')
        for morse_char in morse_chars:
            if morse_char in morse_code_dict:
                text += morse_code_dict[morse_char]
            else:
                text += morse_char
        text += '_'
    return text.strip()

if __name__ == "__main__":
    morse_code = input("Enter Morse code to decode: ")
    morse_code = morse_code.replace('l', '-').replace('o', '.')
    print(morse_code)
    text = morse_to_text(morse_code)
    print("Decoded text:", text.lower())
