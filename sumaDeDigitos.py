n = int(input("Enter the value: "))

container  = 0
while n >0:
    dig = n%10
    container = container + dig
    n=n//10

print("The total sum of digits is: ", container)
