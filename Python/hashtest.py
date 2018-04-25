def testhash(s):
    multi = 1
    hashvalue = 0 
    for ch in s:
        hashvalue += multi * ord(ch)
        multi += 1
    return hashvalue

for item in ("My hash example", "Another hash example", "My last  hash example"):
    print("{}: {}".format(item, testhash(item)))
