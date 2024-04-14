
def sum(num):
    t = 0 
    for i in range(1,num+1):
        t = t+i 
    return(t)

def sq_num(num):
    t = 0
    for i in range(1,num+1):
        t = t +(i**2) 
    return(t)
n = 100
a = sum(n)
b = sq_num(n)
print((a**2)- b)