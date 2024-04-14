def is_prime(num):
    for i in range(2,num):
        if num ==2 : 
            return True
            break
        if num% i ==0 : 
            break
        if i == num-1: 
            return True
            break
n = 20

base = 1
for i in range(2,n):
    if is_prime(i) == True:
        base = base*i

integer =2
while True: 
    number = base*integer
    t = 0
    for j in range(1,n+1):
        if number%j == 0:
            t = t + 1
    if t == n : 
        print(number)
        break
    integer = integer + 1 
        

