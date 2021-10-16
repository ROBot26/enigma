## De/Encryptor
## Rob Ponder
## 5 January 2017


import time

##---------------------------- Functions for partitioning and combining strings and arrays


def parse(val):
    var=list(val)
    return var


def combine(val):
    var=''
    for i in range(0, len(val)):
        var+= val[i]
    return var


##---------------------------- Functions for decrypting and encrypting

def encode(msg,key1,key2):
    parse(msg)
    nmsg=[]
    for i in range(0,len(msg)):

        for j in range(0,len(key1)):
            if key1[j]==msg[i]:
                nmsg.append(key2[j])
    nmsg=combine(nmsg)
    return nmsg

def decode(msg,key1,key2):
    parse(msg)
    nmsg=[]
    for i in range(0,len(msg)):

        for j in range(0,len(key1)):
            if key2[j]==msg[i]:
                nmsg.append(key1[j])
    nmsg=combine(nmsg)
    return nmsg

##---------------------------- Create key


## get word for key

def create_key(word):
## two columns of key
    key1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0',',','.',' ']
    key2=parse(word)



    err=0
    err_f=0

    for i in range(0,len(key1)):#step through adding each letter
        for j in range(0,len(word)): #search through word for letter
             if key1[i]==word[j]:
                       err_f=1
        if err_f == 1:  ##if letter shows up in word, grab letter at end of key 1 list to place in key 2
            k=len(key1)-len(word)+err
            key2.append(key1[k])
            err=err+1
        else:   ## place letter in key 2
            key2.append(key1[i])
        err_f=0

    z=len(key1)+1
    key2=key2[0:z]
    print('Key created')
    return(key1,key2)


##---------------------------- Main code

def encrypt(msg,word):
    print(msg)
    key1,key2=create_key(word)
    nmsg=encode(msg,key1,key2)
    print(nmsg)
    return(nmsg)


def deencrypt(msg,word):
    key1,key2=create_key(word)
    nmsg=decode(msg,key1,key2)
    print(nmsg)
    return(nmsg)

