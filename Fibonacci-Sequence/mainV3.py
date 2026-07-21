'''
fibonacci sequence
'''

def intro():
    print("Welcome to Fibonacci sequence")
    
def body():
    n = input("Enter terms or 'quit': ")
    if n.lower() == 'quit':
        print("Quitting...")
        return False
    try:
        n = int(n)
        choice = int(input('''What do you want?
1. nth term
2. sum till nth term
3. list first n term'''))
        if n <= 0:
            print("Please use a positive number.")
            return True
        elif choice == 1:
            print(fibGen(n))
            return True
        elif choice == 2:
            total = 0
            for i in range(1, n+1):
                total += fibGen(i)
            print(total)
            return True
        elif choice == 3:
            fib = []
            for i in range(1, n+1):
                fib.append(fibGen(i))
            print(", ".join(map(str, fib)))
            return True
        else:
            print("Please use 1, 2, or 3 only")
            return True
    except ValueError:
        print("Enter a valid integer.")
        return True
        
def fibGen(n):
    if n == 1:
        return 0
    elif n ==  2:
        return 1
    else:
        return fibGen(n-1) + fibGen(n-2)
    
def main():
    while True:
        if not body():
            break
            
if __name__ == '__main__':
    intro()
    main()