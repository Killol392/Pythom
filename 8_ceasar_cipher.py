import string


logo = """        
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88           
""";

alphabets = list(string.ascii_lowercase)

# def encrypt(original_text,shift_amount):
#     cipher_text=""
#     for i in original_text:
#         new=alphabets.index(i)+shift_amount
#         new%=len(alphabets)
#         cipher_text+=alphabets[new]
#     print(cipher_text)

# def decrypt(original_text,shift_amount):
#     decipher_text=""
#     for i in original_text:
#         new=alphabets.index(i)-shift_amount
#         new%=len(alphabets)
#         decipher_text+=alphabets[new]
#     print(decipher_text)

def ceasar(original_text,shift_amount,choice):
    output_text=""
    if choice==0:
        shift_amount*=1 
        selected="encoded"
    elif choice==1:
        shift_amount*=-1
        selected="decoded"
    else:
        print("Wrong Choice!")
        exit
    for i in original_text:
        if i in alphabets:
            new=alphabets.index(i)+shift_amount
            new%=len(alphabets)
            output_text+=alphabets[new]
        else:
            output_text+=i
    print(f"\nHere is your {selected} text - ",output_text)
        
# def start():
    # text=input("\nWhat is the Text?\n- ").lower()
    # shift=int(input("What is the Shift Amount?\n- "))
    # choice=int(input("Encrypt[0] or Decrypt?[1]\n- "))
    # ceasar(text,shift,choice)
    # again=input("\nDo you want to go again (yes/no)? ").lower()
    # if again=="yes":
    #     start()
    # elif again=="no":
    #     exit

print(logo,"\n")
start=True
while start==True:
    text=input("\nWhat is the Text?\n- ").lower()
    shift=int(input("What is the Shift Amount?\n- "))
    choice=int(input("Encrypt[0] or Decrypt?[1]\n- "))
    ceasar(text,shift,choice)
    again=input("\nDo you want to go again (yes/no)? ").lower()
    if again=="no":
        start==False
        print("BYE BYE!\n")



