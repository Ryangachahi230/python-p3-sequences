def print_fibonacci(n):
    if n <= 0:
        print([])
        return []
    
    fib_sequence = [0, 1]
    
    if n == 1:
        print([0])
        return [0]
    
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    print(fib_sequence[:n])
    return fib_sequence[:n]