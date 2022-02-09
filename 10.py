file = "D:text.txt"
f = open(file)
chars=[]
startbins=[]
fourbits=[]
while True:
    c = f.read(1)
    if not c:
      break
    chars.append(c)

for char in chars:
    startbins.append(char.join(format(ord(x), 'b') for x in char))
print(len(startbins))
print(len(chars))  
for x in startbins:
    fourbits.append(x[0]+x[1]+x[len(x)-2]+x[len(x)-1])
print(startbins)    
print(fourbits) 
sixteenbits=[]   
for i in range(3,len(fourbits),4):
    sixteenbits.append(fourbits[i-3]+fourbits[i-2]+fourbits[i-1]+fourbits[i])
print(sixteenbits)
endints=[]    
for y in sixteenbits:
    endints.append(int(y, 2))
divbytwo=0
divbythree=0
divbyfive=0
divbyseven=0    
for num in endints:
    if num%2 == 0:
        divbytwo = divbytwo+1
    if num%3 == 0:
        divbythree = divbythree+1
    if num%5 == 0:
        divbyfive = divbyfive+1
    if num%7 == 0:
        divbyseven = divbyseven+1       
print("% divisible by two: ",(divbytwo/len(endints)*100),"%")  
print("% divisible by three: ",(divbythree/len(endints)*100),"%")
print("% divisible by five: ",(divbyfive/len(endints)*100),"%")
print("% divisible by seven: ",(divbyseven/len(endints)*100),"%")
