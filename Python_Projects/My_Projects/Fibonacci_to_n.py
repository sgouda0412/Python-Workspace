def fib(n):
    '''
    Generate fibonacci sequence to inputted N range,
    while failing silently if any issues occur
    '''
    a = 1
    b = 1
    fib_seq = []
    try:
        for i in range(n):
            fib_seq.append(a)
            a, b = b, a + b
    except:
        print("Please enter a number...")
    else:
        return fib_seq

def to_n():
    '''
    Ask User for a number to generate fibonacci sequence
    to, if user inputs something that's not a number
    it handles the error
    '''
    try:
        user = int(input("Please enter a number for Fibonacci Sequence: "))
    except:
        print("That's not a number!")
    else:
        return user
    
def start():
    '''
    If user enters quit it returns false, otherwise it
    will return True
    '''
    ready = input("Are you ready? Type 'quit' to finish: ")
    if ready == 'quit':
        return False
    else: 
        return True

while start():
    num = to_n()
    fibonacci = fib(num)
    print(fibonacci)
