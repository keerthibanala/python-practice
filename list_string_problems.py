# #Find longest word
# sentence = "I am learning Python programming"
# #output = "programming"
sentence = "I am learning Python programming"
words = sentence.split()
print(words)
max_length = 0
longest_word = ""   
for word in words:
    if len(word) > max_length:
        max_length = len(word)
        longest_word = word

print(longest_word + " is the longest word with length " + str(max_length))




# Remove duplicates from list
# numbers = [1, 2, 2, 3, 4, 4, 5]
# [1, 2, 3, 4, 5]
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)




# Count frequency of words
# sentence = "python is fun and python is easy"   
# {'python': 2, 'is': 2, 'fun': 1, 'and': 1, 'easy': 1} 
sentence = "python is fun and python is easy"       
list_of_words = sentence.split()
final_list_of_words = []
list_of_count = []
index = 0
for word in list_of_words:
    if word not in final_list_of_words:
        final_list_of_words.append(word)
        list_of_count.append(1)
    else:
        word_index = final_list_of_words.index(word)
        list_of_count[word_index] = list_of_count[word_index]+1
    index = index + 1

for i in range(len(final_list_of_words)):
    print("\'" + final_list_of_words[i] + "\":", list_of_count[i])
    




# Sum of list
# nums = [10, 20, 30, 40] 
# 100
nums = [10, 20, 30, 40] 
sum = 0
for num in nums:
    sum = sum + num
print("Sum of list:", sum)
