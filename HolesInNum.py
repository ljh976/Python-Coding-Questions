
num = 2537312
def holesInNum(num: int):
    myHash = {}
    vals = {0:	1,
            1:	0,
            2:	0,
            3:	0,
            4:	1,
            5:	0,
            6:	1,
            7:	0,
            8:	2,
            9:	1}
    myHash.update(vals)
    res = 0
    while(num > 1):
        #last digit
        d = num % 10
        #apply on each digits
        res += myHash.get(d) #get value by key from the hash table
        num //= 10
    return res
 
print(holesInNum(num))
