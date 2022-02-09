import random
def print_cube(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")

def win(values):
    positions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for x in positions:
        first=x[0]-1
        second=x[1]-1
        third=x[2]-1
        if (values[first]%2)==1 and (values[second]%2)==1 and (values[third]%2)==1:
            # print_cube(values)
            # print("WIN0")
            return 1
        if values[first] in [10,11,110,111] and values[second] in [10,11,110,111] and values[third] in [10,11,110,111]:
            # print_cube(values)
            # print("WIN1")
            return 1
        if values[first] in [101,100,110,111] and values[second] in [101,100,110,111] and values[third] in [101,100,110,111]:
            # print_cube(values)
            # print("WIN2")
            return 1    
    # print("LOSS")               
    return 0
def main():
    # cube=["-","-","-","-","-","-","-","-","-"]
    totalmoves=0
    for i in range(100): 
        moves=0 
        cube=[0,0,0,0,0,0,0,0,0]
        while(win(cube)==0):
            randposition = random.randint(0,8)
            randcapaki= random.randint(0,2)
            if(randcapaki==0):
                if(cube[randposition] not in [1,11,111]):
                    cube[randposition] = cube[randposition] + 1
            elif(randcapaki==1):
                if(cube[randposition] not in [10,11,110,111]):
                    cube[randposition] = cube[randposition] + 10
            else:
                if(cube[randposition] not in [101,100,110,111]):
                    cube[randposition] = cube[randposition] + 100  
            moves = moves+1
        totalmoves = totalmoves + moves

    print("MOVES IT TOOK:   ",totalmoves/100)
main()
