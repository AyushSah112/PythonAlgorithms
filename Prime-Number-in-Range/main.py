'''
prime number in a range
'''

def intro() :
    print("Welcome to Prime Number in a Range")
    
def body() :
    a = input("Enter your lower range(or 'quit') :  ")
    if a.lower() == "quit":
        return False
    b = input("Enter your higher range(or 'quit') : ")
    if b.lower() == "quit":
        return False
    try:
        a = int(a)
        b = int(b)
    except Exception :
        print("Enter valid number")
        return True
    c = []
    for i in range(a, b+1) :
        if i < 2 :
            continue
        prime = True
        for j in range(2, i) :
            if i%j == 0 :
                prime = False
                break
        if prime :
            c.append(i)
    print(f"Prime number: {c}")
    return True
    
def main() :
    while True :
        if not body() :
            break
    
if __name__ == '__main__' :
    intro()
    main()