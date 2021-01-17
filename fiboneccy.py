
def dynamicFibo(n,table = []):
   while len(table) < n+1: table.append(0) #this does the same thing except it doesn't change the reference to `table`
   #base case
   if n <= 1:
       return n
   #recursive case
   else:
       if table[n-1] ==  0:
           table[n-1] = dynamicFibo(n-1)

       if table[n-2] ==  0:
           table[n-2] = dynamicFibo(n-2)

       table[n] = table[n-2] + table[n-1]

   return table[n]



def fib(n):
    table = []
    table.append(0)
    table.append(1)
    for i in range(2, n+1):
        table.append(table[i-1] + table[i-2])
    return(table[n])





print(str(dynamicFibo(300)))

print(str(fib(0)))


