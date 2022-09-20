import re

with open("text4ent.txt", "r") as f:
    text = f.read()
lst = list(text)
encoding = ''
prev_char =''
count = 0
for char in text:
    if char != prev_char :
        if prev_char:
            encoding+= str(count)+prev_char    
        count=1
        prev_char = char
    else: 
        count+=1
else:
    encoding+=str(count)+prev_char
        
    print(encoding)    
with open("text4out.txt", "w") as f:
    text = f.write(encoding)

with open("text4out.txt", "r") as f:
    text2 = f.read()
alf=[]    
#print(text2)
nums = re.findall(r'\d+', text2) 
preobr=[int(x) for x in nums]
for char in text2: 
    if char.isalpha():
       alf.append(char)
alf1 = list(alf)
deshif = list(map(lambda x,y: x*y,alf1,preobr))
with open("text4out_rash.txt", "w") as f:
    text2 = f.write(str("".join(deshif)))
print(alf1)
print(preobr)
print("".join(deshif)) 



