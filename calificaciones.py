math = int(input("Enter the qualification of math"))
spanish = int(input("Enter the qualification of spanish"))
sociology = int(input("Enter the qualification of sociology"))
english = int(input("Enter the qualification of sociology"))
philosophy = int(input("Enter the qualification of philosophy"))

subjects = [math, spanish, sociology, english, philosophy]      
average = sum(subjects)//len(subjects)

print("The qualification of the subjects is: ", average)

if average < 6:
    print("The studen failed the class")
else:
    print("The student passed the class")


    
