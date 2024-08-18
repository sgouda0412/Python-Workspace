import random

start = input("Would you like to start? Y/N: ").lower()
    
responses = ['Maybe', 'YES!!', 'DO IT!', 'Get it done!', 'Perfect!', 'Hopefully!', 'Maybe Not', "If you're lucky",
           "You're not that lucky", 'Exciting!', 'Do it.', 'Shia LaBeouf it', 'Just do it', 'Why Not?']

while start.startswith('y'):
    question = input("Please enter a question: ")
    choice = random.choices(responses)
    print(f"{choice}\n")
    start = input("Would you like to restart? Y/N: ").lower()
    if start.lower() == 'y':
        continue
    else:
        break
