#table of a number
n=int(input("enter the number:"))
def multiplication_table(number):
        for i in range(1, 11):
            product = number * i
            print(f"{number} x {i} = {product}")
multiplication_table(n)
