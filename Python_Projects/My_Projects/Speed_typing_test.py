import datetime

# Answer + ready check
answer = "The quick brown fox jumps over the lazy dog."
go = input("Please type in 'The quick brown fox jumps over the lazy dog'. Are you ready? Press y to start: ")

# Start time
start = datetime.datetime.now()
print(start)

# User input
user = input("")

# End time
end = datetime.datetime.now()
print(end)


if go.lower() == 'y':
    if user == answer:
        diff = end.second - start.second
        print(f"This took you {diff} seconds!")
    else:
        print("Incorrect Input...")
        print("Please match 'The quick brown fox jumps over the lazy dog.'")
        print("Please remember case sensitivity and punctuation!")


