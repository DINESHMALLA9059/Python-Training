#factorial of the number
a=int(input("enter the number:"))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


result = factorial(a)
print(result) 
