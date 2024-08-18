def palindrome(word):
    if word == word[::-1]:
        print(f"{word} is a palindrome!")
    else: 
        print(f"{word} is not a palindrome, try again!")
        
def ready():
    start = input("Would you like to start? Type 'quit' to end: ")
    if start == 'quit':
        return False
    else:
        return True
    
while ready():
    go = input("Please enter a word: ")
    palindrome(go)
