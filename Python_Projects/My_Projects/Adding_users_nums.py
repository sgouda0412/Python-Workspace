nums = int(input("How many numbers would you like to add? "))

list_of_nums = []

while len(list_of_nums) < nums:
    for n in range(nums):
        num = int(input("Please enter a number: "))
        list_of_nums.append(num)
        
print(f"The sum of your numbers is {sum(list_of_nums)}")
