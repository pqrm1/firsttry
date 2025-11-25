import string
import random

chars=" "+string.ascii_letters+string.punctuation+string.digits
chars=list(chars)
key=chars.copy()
random.shuffle(key)

#print(f"characters={chars}")
#print(f"keys={key}")




def encrypt(plain_text):
    cyper=""
    for letter in plain_text:
        index=chars.index(letter)
        cyper+=key[index]
    
    return cyper

def decrypt(cyper_text):
    plain=""
    for letter in cyper_text:
        index=key.index(letter)
        plain+=chars[index]
    
    return plain

def main():
    print("-"*10 +" "+"MESSAGE ENCRYPTION"+" "+"-"*10)
    plain=input("Enter your message: ")
    encrypt(plain)
    print(f"The encrypted text is: {encrypt(plain)}")
    de=input("Would you like to decrypt?:(y/n) ").lower()
    if de=="n":
        print("-"*10+" "+"GOODBYE"+" "+"-*10")
        return 0
    else:
        decrypt(encrypt(plain))
        print(f"The decrypted text is: {decrypt(encrypt(plain))}")
        print("-"*10+" "+"GOODBYE"+" "+"-"*10)

if __name__=="__main__":
    main()