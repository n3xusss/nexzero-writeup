import math
import random


FLAG="shifting_with_gold_fibonacciiii"

def encrypt_text(text, key_sequence):

    encrypted_text = ""
    key_length = len(key_sequence)

    for i, char in enumerate(text):
        if char.isalpha():	
	        shift = key_sequence[i % key_length] 
	        encrypted_char = chr((ord(char.lower()) + shift - 97) % 26 + 97)
	        encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text
    
    

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
    
    
    
Golden_Sequence = choose_sequence_length(FLAG)
cipher=encrypt_text(FLAG,Golden_Sequence)

try:	
    print(f'SHIFTER BY M0/MASSI')
    print(f'Welcome To SHIFTER here your flag encrypted :\n {cipher}')
    print('------------------------------------------------------------------------------------------------------')
    text = input("Give me Your Text to Encrypt it :")
	
    Golden_Sequence = choose_sequence_length(text)


    print('------------------------------------------------------------------------------------------------------')
    cipher=encrypt_text(text,Golden_Sequence)
    print(F'HERE IS YOUR ENCRYPTED DATA: {cipher}')
except:
    raise("Error ......")
	

	


	


