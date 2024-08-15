import wikipedia

def search(question):
    answer = wikipedia.summary(question).split(".")
    for line in answer:
        print(line)

if __name__ == "__main__":
    question = "Chelsea f.c"
    search(question)

