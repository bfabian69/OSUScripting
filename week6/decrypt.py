

def decrypt_caesar(encrypted_text, distance):
    decrypted_text = ''
    
    for ch in encrypted_text:
        ordValue = ord(ch)
        cipherValue = ordValue - distance
              
        if cipherValue < 32: 
            cipherValue = 127 - (32 - cipherValue) 
       
        decrypted_text += chr(cipherValue)    
    return decrypted_text


encrypted_text = input("Enter the encrypted text: ")
distance = int(input("Enter the distance value: "))

decrypted_text = decrypt_caesar(encrypted_text, distance)
print("Decrypted text:", decrypted_text)
