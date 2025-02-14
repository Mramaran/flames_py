from collections import Counter
def difference(name1,name2):
    name1=name1.lower()
    name2=name2.lower()
    name1=Counter(name1)
    name2=Counter(name2)
    n=0
    hash1=name1-name2
    hash2=name2-name1
    for i in hash1:
        n+=hash1[i]
    for i in hash2:
        n+=hash2[i]
    return n

def flames(n):
    flames=['f','l','a','m','e','s']
    remo=0
    for i in range(6,1,-1):
        remo=((remo+n)%i)-1
        del flames[remo]
        if remo==-1:
            remo=0
    return(flames[0])



name1=input("Enter Person_1 name:")
name2=input("Enter Person_2 name:")
n=difference(name1,name2)
definition={'f':"friends",'l':"Lovers",'a':"Affection",'m':"Marrage",'e':"Enemy",'s':"Sister"}
print(definition[flames(n)])
