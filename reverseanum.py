#reverse a number
num=int(input("enter the number:"))
def reverse_number(num):
    reversed_str = str(num)[::-1]

    reversed_number = int(reversed_str)

    return reversed_number

result = reverse_number(num)
print(f"Reversed number is: {result}")
