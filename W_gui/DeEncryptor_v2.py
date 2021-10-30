## De/Encryptor
## Rob Ponder
## 5 January 2017
## 29 October 2021


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
    key2=[]
    for kdx,letter in enumerate(word):
        loc=1000
        for idx,value in enumerate(key1):
            if value==letter:
                loc=idx
            if idx % (loc+1) == len(word)-kdx:
                key2.append(value)
                del key1[idx]
    key2.extend(key1)
    key1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0',',','.',' ']
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

