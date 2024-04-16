def is_prime(num):
    border = num
    if num ==2 : 
        return True
    divident = 2
    while True:
        if num % divident ==0 : 
            return False
        border = num/divident
        if divident > border:
            return True
        divident +=1

t = 0
for i in range(2,2000000):
    if is_prime(i) == True:
        t += i

print(t)