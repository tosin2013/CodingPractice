import os
import sys 

def getwordcount(filename):
    print(filename)
    try:
        fhead = open(filename,"r")

        count = dict()

        for line in fhead.readlines():
            #print(line)
            words = line.split()
            for word in words:
                if word not in count:
                    count[word]=1
                else: 
                    count[word]+=1
        fhead.close()
        return count
    except:
        print(filename+'not Found')
        exit



count=getwordcount("test.txt")
print(count)
