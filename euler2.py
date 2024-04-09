
def fibonaci(n): 
    fib = [1,2]
    i = 2
    while True : 
        if fib[i-1] + fib[i-2] < n :
            fib.append(fib[i-1] + fib[i-2])
        else : 
            break
        i= i + 1
    return(fib)

fib = fibonaci(4000000)
t = 0
for i in fib: 
    if i%2 == 0 : 
        t = t + i
print (t)
