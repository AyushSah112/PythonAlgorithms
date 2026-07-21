'''
factorial calculator
'''

def intro():
    print("Welcome to Factorial Series")
    
def body():
    n = input("Enter your number or 'quit': ")
    if n.lower() == 'quit':
        print("quiting....")
        return False
    try:
        n = int(n)
        if n < 0:
            print("Factorial is not defined for negative numbers.")
            return True
        elif n == 0:
            print("0! = 1")
            return True
        else:
            fac = 1
            for i in range(1, n+1):
                fac *= i
            print(f"{n}! = {fac}")
            return True
    except ValueError:
            print("Please enter a valid number.")
            return True
            
def main():
    while True:
        if not body():
            break
    
if __name__=='__main__':
    intro()
    main()