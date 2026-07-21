while True:
    n = input("Enter a numher or 'quit': ")
    if n.lower() == 'quit':
        print("quiting....")
        break
        
    else:
        try:
            n = int(n)
            if n == 1 or n == 0:
                print(f"{n}! = 1")
                continue
                
            elif n < 0:
                print("Factorial is not defined for negative number")
                continue
            else:
                fac = 1
                for i in range(1, n+1):
                    fac *= i
                print(f"{n}! = {fac}")
                continue
                
        except ValueError:
            print("Please enter a valid integer.")
            continue