chars=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","-",",","."," ","?","<",">","=","&","$","!","/",";",":","*","+","^","-","`","§","'","à","ç","ò","@","(",")","{","}","[","]","#","°","ì","£","%","€","~"]
s=open("encrypt.txt","r")
secret=s.readlines()
s.close()

message=[]
encryption_level=int(secret[len(secret)-1])

for i in range(len(secret)-1):
    l=""
    for char in secret[i]:
        if char=="\n":
            continue
        for i in range(encryption_level):
            pos=(chars.index(char)-encryption_level+len(chars))%len(chars)
            char=chars[pos]
        l+=char
    message.append(l)

d=open("decrypt.txt","w+")
for i in range(len(secret)-1):
    d.write(message[i]+"\n")
d.close()