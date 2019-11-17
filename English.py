from textblob import TextBlob

f = open("EngCheck.txt", "r+")
a = f.read()

print("Original Text : ", str(a))

b = TextBlob(a)

print("Corrected Text : ", str(b.correct()))
f.close()

d = open("EngCheck.txt", "w")
d.write(str(b.correct()))
d.close()
