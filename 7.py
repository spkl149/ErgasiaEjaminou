import ast
from collections import Counter 
file = "D:temptext.txt"
f = open(file)
dicts=[]
for x in f:
    d = ast.literal_eval(x)
    dicts.append(d)

keys=[]
for di in dicts:
    for key in di:
        if key not in keys:
            keys.append(key)     
for key in keys:
    print(key)       
searchkey = input("Please give the search key:")       
results=[]   
if searchkey in keys:
    for di in dicts:
        if searchkey in di:
            results.append(di[searchkey])
    print("MAX: ",max(results))
    print("MIN: ",min(results))
    value, count = Counter(results).most_common(1)[0]  
    print("MOST POPULAR: ",value," APPEARS: ",count," TIMES") 
else:
    print("search key not in available keys")
