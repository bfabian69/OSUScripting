

def encrypt_caesar(plaintext, distance):
    encrypted_text = ''
    
    for ch in plaintext:
        ordValue = ord(ch)
        cipherValue = ordValue + distance
              
        if cipherValue > 126:  
            cipherValue = 32 + (cipherValue - 127)  
        
        encrypted_text += chr(cipherValue)
    
    return encrypted_text

plaintext = input("Enter the plaintext: ")
distance = int(input("Enter the distance value: "))

encrypted_text = encrypt_caesar(plaintext, distance)
print("Encrypted text:", encrypted_text)


    
