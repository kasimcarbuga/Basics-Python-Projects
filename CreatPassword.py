import random 

import string 

def generate_password(lenght,level,output=[]):
    
    chars = string.ascii_letters
    
    if level > 1 :
        chars = "{}{}".format(chars,string.digits)
    if level > 2 :
        chars = "{}{}".format(chars,string.punctuation)
    
    for i in range(lenght) :
        output.append(random.choice(chars))
        
    return "".join(output)

print(("-"*10)+"\n ŞİFRE BELİRLEME \n"+("-"*10))

password_lenght = int(input("Uzunluk: "))
password_level  = int(input("Seviye: "))

password = generate_password(password_lenght,password_level)

print("\n Şifreniz : {}".format(password))
