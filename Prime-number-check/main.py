'''
prime number check
'''

def intro() :
    print("Welcome to prime number check")
    
    
def body() :
    n = input("Type a number or 'quit' :  ")
    if n == "1" :
        print("It is not a prime")
        return True
    elif n == "2" :
        print("it is prime")
        return True
    elif n == "quit" :
        return False
    else :
        p = int(n)
        prime = True 
        for i in range(2, p):
            
            if p%i == 0 :
                prime = False
        if prime:
            print("It is prime")
            return True
        else:
            print("its not prime")
            return True
    
def main() :
    while True :
        if not body() :
            break
    
if __name__ == '__main__' :
    intro()
    main()