'''
factorial calculator
'''

def intro():
    print("Welcome to Factorial Series")
    
def facGen(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*facGen(n-1)
        
def body():
    n = input("Enter a number or 'quit': ")
    if n.lower() == 'quit':
        print("quiting...")
        return False
        
    try:
        n = int(n)
        if n < 0:
            print("Factorial is not defined for negative numbers.")
            return True
        else: 
            print(facGen(n))
            return True
        
    except ValueError:
        print("Please enter a valid integer.")
        return True
        
def main():
    while True:
        if not body():
            break
            
if __name__=='__main__':
    intro()
    main()