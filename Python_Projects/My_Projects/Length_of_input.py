user = input("Please enter a sentence: ")
length = len(user)

def userinput(user):
    if length < 10:
        print(f"That's an extremely small sentence using {length} characters...")
    elif length > 10 and length < 20:
        print(f"That's a very small sentence using {length} characters...")
    elif length > 20 and length < 30:
        print(f"That's still a small sentence using {length} characters")
    elif length > 30 and length < 40:
        print(f"That's a medium sized sentence using {length} characters")
    elif length > 40 and length < 50:
        print(f"That's a large sentence! You've used {length} characters")
    elif length > 50 and length < 60:
        print(f"Your sentence is getting big... There's {length} characters, make sure you're including punctuation!")
    elif length > 60 and length < 70:
        print(f"That's a very large sentence! You are using {length} characters")
    elif length > 70 and length < 80:
        print(f"That's an extremely large sentence... {length} characters were used")
    else:
        print(f"Sentence is too big for my small brain... I can't comprehend {length} characters")
        
userinput(user)
