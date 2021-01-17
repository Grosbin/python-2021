
elements = int(input("Enter the number of elements you want to calculate the average: "))
sumElements = []

for i in  range(0 , elements):
    number = int(input("Enter the number"))
    sumElements.append(number)

average = sum(sumElements)/elements
print("The average is: ", round(average))

sumElements2 = 0

elements2 = int(input("Enter the number of elements you want to calculate the average: "))

for i in range(0, elements2):
    number2 = int(input("Enter the number"))
    sumElements2 += number2

average2 = sumElements2/elements2
print("The average is: " + str(average2))

 
