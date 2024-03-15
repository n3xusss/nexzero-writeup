def encrypt_text(text, key):

    encrypted_text = ""
    key_length = len(key)

    for i, char in enumerate(text):
        if char.isalpha():	
	        shift = key[i % key_length] 
	        encrypted_char = chr((ord(char) + shift - 97) % 26 + 97)
	        encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text
    
    

    
    

	


	


