import collections

born={}
born["matt"]=2000
born["phillp"]=1975
born["greg"]=1975
born["Will"]=1803
born["john"]=1750
print(born)


death={}
death["matt"]=2050
death["phillp"]=2040
death["greg"]=1999
death["Will"]=1890
death["john"]=1803
print(death)

everything={}

for x in born:
    count = 0
    if born[x] is everything:
        print "born[x] is in arrray"
        everything.update(born[x],count)
    else:
        print "born[x] is not in arrray"
    print born[x]

for y in death:
    #everything[0]=born[y]
    print death[y]

print set(born)
