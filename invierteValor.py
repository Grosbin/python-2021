value = int(input("Enter the value"))

reverse = 0

while value > 0:
    dig = value % 10
    print(dig)
    reverse = reverse*10+dig
    print("Reverse: ", reverse)
    value=value//10

print("Reverse of the number: ", reverse)

