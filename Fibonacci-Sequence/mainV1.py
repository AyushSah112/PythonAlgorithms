'''
fibonacci sequence
'''
while True:
    n = input("Enter terms or 'quit': ")
    if n.lower() == 'quit':
        print("Quitting...")
        break
    try:
        n = int(n)
        if n <= 0:
            print("please enter a positive integer.")
            continue
        fib = []
        a, b = 0, 1
        for i in range(n):
            fib.append(a)
            a, b = b, a+b
        print(f"Fibonacci sequence: {fib}")
    except ValueError:
        print("Please enter a valid integer.")