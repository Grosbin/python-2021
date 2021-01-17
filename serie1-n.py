n = int(input("Enter the value"))

sums = [] 

for i in range(1, n+1):
    print(i, sep=" ", end=" ")
    if i < n:
        print("+", sep=" ", end=" ")
    sums.append(i) 
   

print("=", sum(sums))
