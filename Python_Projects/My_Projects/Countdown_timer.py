import time

t = input("Please enter how long would you like to start a timer for in seconds: ")

def countdown(timer):
    while timer > 0:
        print(timer)
        timer -= 1
        time.sleep(1)
    print("You have run out of time!")
    
while not t.isdigit():
    print("Please enter a valid integer to countdown from: ")
    t = input("Please enter how long would you like to start a timer for in seconds: ")
timer = int(t)
    
    
countdown(timer)
