#fibonocci series
a=int(input("enter the number:"))
def fibonacci_iterative(n):
    
    fib_sequence = [0, 1]

    
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)

    return fib_sequence[:n]

result = fibonacci_iterative(a)
print(result)
