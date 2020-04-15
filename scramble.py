import random  

charbase=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","-",",","."," ","?","<",">","=","&","$","!","/",";",":","*","+","^","-","`","§","'","à","ç","ò","@","(",")","{","}","[","]","#","°","ì","£","%","€","~","%"]

charnums=[]

for i in range(101):
    charnums.append(i)

newlist1=[]

for i in range(101):
    charpos=random.randrange(0,len(charnums))
    newlist1.append(charbase[charnums[charpos]])
    charnums.remove(charnums[charpos])

print(newlist1)
print(len(newlist1))