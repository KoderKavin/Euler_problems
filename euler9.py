def is_py(triplet):
    if triplet[0]**2 + triplet[1]**2 == triplet[2]**2:
        return True


for a in range(1,1000):
    for b in range(a+1,1000):
        c = 1000-a -b 
        if c>0 and is_py([a,b,c]) == True:
            print([a,b,c])
            print(a*b*c)