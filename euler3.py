n = int(input("enter the number: "))
def is_prime(num): 
    if num == 2: 
        return True 
    else : 
        for i in range(2,num):
            if num%i == 0 : 
                break
            elif i == num-1: 
                return True

prime_factors = []
for i in range(1,n+1):
    if n % i==0 and is_prime(i) == True: 
        prime_factors.insert(0,i)

if len(prime_factors) != 0 : 
    print("the greatest prime factor of ",n ," is " ,prime_factors[0])