decreasing_nos = []
for i in range(100,1000): 
    decreasing_nos.insert(0,i)

def is_pal(num): 
    numstring = str(num)
    newnumstring = ""
    temp = []
    for i in numstring: 
        temp.insert(0,i)
    for j in temp:
        newnumstring = newnumstring + j
    if numstring == newnumstring:
        return True 

palindromes = []
t = 0
for j in decreasing_nos: 
    for k in decreasing_nos: 
        if is_pal(j*k) == True: 
            palindromes.append(k*j)

def bubble_sort(array):
    n = len(array)   
    pointer = n
    while pointer >0 :  
        for i in range(0,pointer -1):
            if palindromes [i] < palindromes[i+1]:
                a = array[i]
                b = array[i+1]
                array[i] = b 
                array[i+1] = a
        pointer = pointer -1 
    return(array)

newpal = bubble_sort(palindromes)
print(newpal[0])