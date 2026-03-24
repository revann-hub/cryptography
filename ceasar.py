import random
def binary(a):
    m=''
    for i in a:
        x=ord(i)
        s=""
        while x!=0:
            b=x%2
            x=x//2
            s+=str(b)
        while len(s)!=8:
            s="0"+s  
        m+=s
    return m

def key_generator(a):
    z=[0,1]
    s=""
    for i in range(0,a):
        b=random.choice(z)
        s+=str(b)
    return s

def encrypt(s,k):
    x=""
    a=""
    b=""
    for i in range(0,len(s)):
        if s[i]==k[i]:
            x+="0"
        else:
            x+="1"
    for z in x:
        a+=z
        if len(a)==8:
            b+=chr(int(a,2))
            a=""
    return x