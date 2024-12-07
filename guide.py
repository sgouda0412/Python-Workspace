words_str = input("Enter words separated by spaces: ")
words = {word: len(word) for word in words_str.split()}
print(words)


x = [1, 2, 3, 4]
print(x)

lambda_add = lambda x, y: x + y
print(f"using lambda function: {lambda_add(3, 4)}")
