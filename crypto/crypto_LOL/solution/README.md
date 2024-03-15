# LOL

**Difficulty:** Easy
**Category:** Crypto
**Source Code:** Not Available
**Author:** 0utc4st
**Description:** Come, i'll take you back to World War 1

​         PS: convert the result to lowercase.

## Solution

we were given a text file that contains this :

```plaintext
lo o lool ool ooo { oloo lllll oloo _ l oooo ooool l _ oll ooool ooo _ ll lll olo ooo oooll _ ooool oolo l oooll olo _ ooool oloo oloo }
```

we already see the structure of the flag `blabla{bla_bla_bla}`, but it's somehow encoded.

we see that we only have 2 characters, `l` and `o`, the first thaught here would be to convert those to binary like ones and zeroes then decode it , but that didn't work.

if we search on other encoding that only have 2 different values, and combining that with the description where it mentioned `WW1`, we reach the conclusion that this might be Morse code, where we replace `l` with `-`, and `o` with `.`

so our strategy here is to split that string based on the space character ` `, every element represents a character, we'll obviously ignore the `{}` and `_` characters and leave them the same since Morse code only deals with alphabet letters and numbers, and we replace `l` and `o` with `-` and `.`

we can script that, here is the python script that solves this challenge :

```python
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
```

let's run it :

```plaintext
└─$ python3 decode.py
Enter Morse code to decode: lo o lool ool ooo { oloo lllll oloo _ l oooo ooool l _ oll ooool ooo _ ll lll olo ooo oooll _ ooool oolo l oooll olo _ ooool oloo oloo }
-. . -..- ..- ... { .-.. ----- .-.. _ - .... ....- - _ .-- ....- ... _ -- --- .-. ... ...-- _ ....- ..-. - ...-- .-. _ ....- .-.. .-.. }
Decoded text: nexus{l0l_th4t_w4s_mors3_4ft3r_4ll}_
```

and we have the flag

## Flag

`nexus{l0l_th4t_w4s_mors3_4ft3r_4ll}`