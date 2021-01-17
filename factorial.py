

def factorial(n):

    resultado = 0
    if n == 0 | n == 1:
        return 1
    elif n > 1:
        resultado = n * factorial(n-1)
        return resultado

def factorial2(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f


print(str(factorial(30)))
print(str(factorial2(30)))

def f(x, y):
    return x * 2, y * 2
a, b= f(1, 2)

print(str(a))

print(str(b))
 

