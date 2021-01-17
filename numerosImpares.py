upper = int(input("Enter the upper range value"))
lower = int(input("Enter the lower range value"))

for i in range(lower, upper+1):
    if i % 2 ==1:
        print(i," The value is odd number")
