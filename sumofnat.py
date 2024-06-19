#sum of n natural numbers
a=int(input("enter the number:"))
def sum_of_natural_numbers(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


result = sum_of_natural_numbers(a)
print(result) 
