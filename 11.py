import math
sets = [ "0710166acf892781818a456e3f4723b9aeae2760ec8f53db53d5dc36dddc6049",

"864fd4b70711e4d713ec525892a7492ea6ae0fc35776ed535c9fa232dbcb7205",

"2d9496367b70cde4b12d8219ad966eb34f036242956a54fbb005f25ff93f9340",

"cfd1dcb1e4e681d26ec3fd9ede16eb7a19bf31df9f9641c5d70d0ed15d3fd2cf",

"611f856da3e5d0005c53087bdbe59a4078cc5369895504a9091c5b803795d07f",

"008637bf6ca0df8e3fdcd12600917da850bea401aa836d1d84f7e78fa438ff8c",

"9cb540903ca2c5ccde121c350d9b4bbce8003929e24dc30a486ceaf9dc774927",

"5b00a7db71e7f89c95aee3f99ceea289c54afdb9558ead1b2694183e3a96074c",

"b02ca2fa012316cef574474cdef203a20d8efed707082a05160cf20b36b6587b",

"310e634a4ef0181f7699c49c920f4d4dac106d77651916c198d19dc5aa05134d",

"a1edcdc5393c7d42b64a964c7c4c329f343ab2aa7c99d3066b9549f22475038a",

 "b4e2ad365a55b98aed980a6e86f8c2c2fd195d01d51d99a38402e586fbc377d9",

"34286d750a3c857bb71afe3daab5d13d0faa6f107fb6f623e24e0edd827fcee1",

"1b17aa463132f49f0964ec20a8564c0d078359726171f30a0b8da82aa68393d8",

"cac5e8f6e9e23acb9d8f3afb4fa9e148bd56c44093b4a7e99d14ae47f13770bd",

"bf79a587c6d96be89f9acf5bd172b7ed935ce96b26c6aba1f37c5a56c159b7a0",

"874e04828185ed5791daf48f3a26860b6b1e5c81058c92cd7e330ee720514c93",

"844257e5620387e2d0ff6f5268de64eb744aa773f002e4064b8aca1b1d794b6f",

"75632bc26a53cc49a7cd963f73cd3c33d3c38e52b341da4b94892adada7d1d0c",

"13225adaf0877d9bdddfcba0b008e023bca13dd98f6b6d706407b4cef9da4687"

]
print(len(sets))
word=""
for x in sets:
    word+=x

print(word)  
possiblevalues = [ "0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"] 
counters=[]
for symbol in possiblevalues:
    counter=0
    for letter in word:
        if symbol==letter:
            counter+=1       
    counters.append(counter)      
print(counters)   
sum=0
for num in counters:
    sum+=num   
# print(sum)   
probabilities=[]
for c in counters:
    probabilities.append(c/sum) 

print(probabilities)    
H=0
Hsum=0
for p in probabilities:
    Hsum+= (p*(math.log(p,16)))
H= -1*Hsum
print(H)
