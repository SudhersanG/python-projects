#CIEASER CIPHER PROJECT
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text,shift_key):#hello,3
    encrypt_text=""
    for char in plain_text:
        indexPosition=alphabet_list.index(char)
        newIndex=(indexPosition+shift_key)%26
        encrypt_text+=alphabet_list[newIndex]
        
    print(f"your encrypted message is {encrypt_text}")
    
        
def decrypt(plain_text,shift_key):#hello,3
    decrypt_text=""
    for char in plain_text:
        indexPosition=alphabet_list.index(char)
        newIndex=(indexPosition-shift_key)%26
        decrypt_text+=alphabet_list[newIndex]
        
    print(f"your decrypted message is {decrypt_text}")
        


gameOver=False
while not gameOver:
    
    choice=input("enter your choice-(encrypt/decrypt):").lower()
    text=input("enter your text:")
    shiftkey=int(input("enter shift key:"))

    if choice=="encrypt":
        encrypt(plain_text=text,shift_key=shiftkey)
        
    elif choice=="decrypt":
        decrypt(plain_text=text,shift_key=shiftkey)

    gameEnd=input("you want to end game:(yes/no)").lower()
    if gameEnd=="yes":
        gameOver=True
    elif gameEnd=="no":
        gameOver=False

