n = int(input("enter the number: "))
t = 0
for i in range(1,n):
    if i % 3 == 0 or i% 5 == 0: 
        t = t + i
    
print(t)
