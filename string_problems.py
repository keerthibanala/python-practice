# Generate initials from a full name
full_name = "Keerthi Banala"
print(full_name.split())
initials = ".".join((name[0].upper() for name in full_name.split()))                             
print("Intials:", initials)

# Word Counter
sentence = "I am learning Python programming"
count = 0
for word in sentence.split():
    count = count +1 
print("Number of words:", count)

# Reverse a Sentence
original_sentence = "Python is fun"
words = original_sentence.split()
reversed_words = []
for word in words[::-1]:
    reversed_words.append(word)
# print(reversed_words)
print("Reversed Sentence:", " ".join(reversed_words))