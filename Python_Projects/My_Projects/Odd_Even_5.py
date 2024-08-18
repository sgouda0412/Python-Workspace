a = int(input("Please enter a number to start with: "))
b = int(input("Please enter a number to end with: "))
list_nums = list(range(a, b))

class Numbers():

    def __init__(self):
        print("Numbers object created")

    def odd_nums(self):
        '''
        If a number is odd, print odd
        '''
        for item in list_nums:
            if item % 2 == 1:
                print(f"This is odd {item}")

    def even_nums(self):
        '''
        If a number is divisible by 5, stated. Otherwise stated if Even
        '''
        for item in list_nums:
            if item % 5 == 0:
                print(f"Divisible by 5!: {item}")
            elif item % 2 == 0:
                print(f"This is EVEN: {item}")

even = Numbers
even.even_nums(list_nums)
even.odd_nums(list_nums)
print(f"{list_nums[-1]}")
