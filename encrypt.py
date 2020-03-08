import random
#All chars I could think of that would normally be written
chars=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","-",",","."," ","?","<",">","=","&","$","!","/",";",":","*","+","^","-","`","§","'","à","ç","ò","@","(",")","{","}","[","]","#","°","ì","£","%","€","~"]
print(len(chars))

m=open("message.txt","r")
message=m.readlines()
m.close()

secret=message

encryption_level=random.randint(5,10)
print("Encryption level: "+str(encryption_level))
for line in message:
    l=""
    for char in line:
        if char=="\n":
            continue
        for i in range(encryption_level):
            pos=(chars.index(char)+encryption_level)%len(chars)
            char=chars[pos]
        l+=char
    secret[message.index(line)]=l

e=open("encrypt.txt","w+")
for line in secret:
    e.write(line+"\n")
e.write(str(encryption_level))
e.close()
