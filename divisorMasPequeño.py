n = int(input("Enter the value"))
list = []

for i in range(2, n+1):
    if n%i==0:
        list.append(i)


list.sort()
print("Smal lest divisor is: ", list[0])

print("Hola mundo")
