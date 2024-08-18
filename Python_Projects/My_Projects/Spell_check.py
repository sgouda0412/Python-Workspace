from textblob import TextBlob

a = "choclte"
print("Original text: " +str(a))

b = TextBlob(a)
print("Corrected text: " +str(b.correct()))
