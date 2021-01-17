n = int(input("Enter the number palindrieme"))


tmp = n
reverse = 0

while n >0:
    dig = n % 10
    reverse = reverse*10+dig 
    n = n//10

if tmp == reverse:
    print("Values are palindrieme")
else:
    print("Values are not palindrieme")
