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
        if n <= 0:
            print("please enter a positive integer.")
            return True
        fib = []
        a, b = 0, 1
        for i in range(n):
            fib.append(a)
            a, b = b, a+b
        try:
            choice = int(input('''Print as:
1. line by line
2. list 
3. seperated by comma\n'''))
            if choice == 1:
                print()
                for item in fib:
                    print(item)
                print("-"*15)
            elif choice == 2:
                print()
                print(fib)
                print("-"*15)
            elif choice == 3:
                print()
                print(", ".join(map(str, fib)))
                print("-"*15)
            else:
                print("Please use 1, 2, or 3.")
        except ValueError:
            print("Please choose the given option only.")
            
        return True
    except ValueError:
        print("Please enter a valid integer.")
        return True
    
def main():
    while True:
        if not body():
            break
    
if __name__ == '__main__':
    intro()
    main()