upper = int(input("Enter the value of the upper range"))
lower = int(input("Enter the value of the lower range"))
n = int(input("Enter value to divide"))

for i in range(lower, upper+1):
    if i % n == 0:
        print("The value ", n ," if is divisible with", i) 

       

