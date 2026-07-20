'''
prime number check
'''

def intro() :
    print("Welcome to prime number check")
    
    
def body() :
    n = input("Type a number or 'quit' :  ")
    if n.lower() == "quit" :
        return False
        
    try:
        p = int(n)
        if p <= 0 :
            print("It is not a prime")
            return True
        elif p == 1 :
            print("It is not a prime")
            return True
        elif p == 2 :
            print("It is a prime")
            return True
        
        else :
            
            prime = True 
            for i in range(2, int(p**0.5) + 1):
                
                if p%i == 0 :
                    prime = False
                    break
            if prime:
                print("It is a prime")
                return True
            else:
                print("It is not a prime")
                return True
                
    except ValueError :
        print("Please enter a valid integer")
        return True
    
def main() :
    while True :
        if not body() :
            break
    
if __name__ == '__main__' :
    intro()
    main()
