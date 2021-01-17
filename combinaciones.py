a = int(input("Enter the first digits"))
b = int(input("Enter the second digits"))
c = int(input("Enter the third digits"))

list = []
list.append(a)
list.append(b)
list.append(c) 

for i in range(0, len(list)):
    for j in range(0, len(list)):
        for k in range(0, len(list)):
            if i!=j & j!=k & k!=i:
                print(list[i], list[j], list[k])
