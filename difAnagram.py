#get minimum number to make two strings as anagram.

from collections import Counter

a = "aaaaaaaabdcd"
b = "aaaaaaaacaaa"


def anagram(a: str, b: str):
    a_hash = Counter(a) #hash key: char, value: number of char
    b_hash = Counter(b)
    res = 0
    
    if len(a) != len(b):
        return -1
 
    print(a_hash.values())
    print(b_hash.values())
    return sum(( a_hash - b_hash ).values()) #num of minimum changes


print(anagram(a,b))
