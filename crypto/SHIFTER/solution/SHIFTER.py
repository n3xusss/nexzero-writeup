import math


def choose_sequence_length(text):
    sequence = []
    phi = (1 + math.sqrt(5)) / 2
    n = 0
    fibonacci_number = int((math.pow(phi, n) - math.pow(-phi, -n)) / math.sqrt(5))

    while fibonacci_number < len(text):
        sequence.append(fibonacci_number)
        n += 1
        fibonacci_number = int((math.pow(phi, n) - math.pow(-phi, -n)) / math.sqrt(5))

    return sequence


def decrypt_text(text, key_sequence):
    decrypted_text = ""
    key_length = len(key_sequence)
	
    for i, char in enumerate(text):
        if char.isalpha():	
	        shift = key_sequence[i % key_length] 
	        decrypted_char = chr((ord(char) - shift - 97) % 26 + 97)
	        decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text
    
	    
	    
flag_enc='sijhwnvt_wjuj_lwyy_gjdrsipxijjk'

fibonacci_sequence =choose_sequence_length(flag_enc)
print(decrypt_text(flag_enc,fibonacci_sequence))



