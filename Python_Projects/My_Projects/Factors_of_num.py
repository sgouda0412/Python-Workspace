def print_factors(x):
    '''
    Iterate through a range of numbers, if x % iteration == 0 then it's a factor! 
    '''
    print(f"The Factors of {x} are: ")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)
            
def retry():
    ready = input("Would you like to start? Type 'quit' to end: ")
    if ready == 'quit':
        return False
    else:
        return True
    
while retry():
    num = int(input("Enter a number to find factors for: "))
    print_factors(num)
