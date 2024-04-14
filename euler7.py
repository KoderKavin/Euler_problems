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

        
n = 10001
counter = 0
i = 1
while True: 
    if is_prime(i) == True: 
        counter += 1
    if counter == n: 
        print(i)
        break 
    i +=2