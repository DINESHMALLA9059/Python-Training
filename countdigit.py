#countdigits in a number
num=int(input("enter the number:"))
def count_digits(num):
    
    return len(str(num))

result = count_digits(num)
print(f"Number of digits is: {result}") 
