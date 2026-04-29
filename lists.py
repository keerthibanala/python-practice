my_list = [1,2,3,4,5]
print(my_list)
print(len(my_list))

# List can contain different data types
title = 'Fight Club'
year = 1999
genre = ['thriller', 'drama', 'crime']
duration = 139
rating = 8.644
movie_info = [title, year, genre, duration, rating]
print(movie_info)

# Indexing and slicing
print("First element:", movie_info[0])
print("Last element:", movie_info[-1])
print("Genre:", movie_info[2])
print("First 3 elements:", movie_info[:3])
print("Last 2 elements:", movie_info[-2:])
print("All elements except the first:", movie_info[1:])
print("All elements except the last:", movie_info[:-1])
print("Elements from index 1 to 3:", movie_info[1:4])

#accessing nested lists
print("First genre:", movie_info[2][0])
print("Second genre:", movie_info[2][1])

# Modifying lists
# lists can be modified after creation, unlike strings which are immutable

#Replacing/changing an element
movie_info[1] = 2000
print("Updated movie info:", movie_info)    
# Adding elements to a list
movie_info.append("David Fincher")
print("After appending director's name:", movie_info)
movie_info.pop()
movie_info.insert(2, "Brad Pitt")
print("After inserting Brad Pitt at index 2:", movie_info)  
# Removing elements from a list
movie_info.remove("Brad Pitt")
print("After removing Brad Pitt:", movie_info)
removed_genre = movie_info.pop(2)
print("After popping element at index 2:", movie_info)
print("Removed genre:", removed_genre)


#Sorting a list
#sorted() function returns a new sorted list without modifying the original list
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)
print("Original numbers:", numbers)
print("Sorted numbers:", sorted_numbers)
descending_numbers = sorted(numbers, reverse=True)
print("Descending sorted numbers:", descending_numbers)
#sort() method sorts the list in place and modifies the original list
numbers.sort()
print("Numbers after sort():", numbers)
numbers.sort(reverse=True)
print("Numbers after sort() in descending order:", numbers) 
#Sorted() and sort() can also be used to sort lists of strings - sorts in lexicographical order (alphabetical order for strings)
names = ["Charlie", "Alice", "Bob"]
sorted_names = sorted(names)
print("Original names:", names)
print("Sorted names:", sorted_names)
names.sort()
print("Names after sort():", names)
#sort a string.
string = "python"
sorted_string = sorted(string)
print("Original string:", string)
print("Sorted string:", sorted_string)

# processing strings with lists
# splitting a string into a list of words
sentence = "Python programming is fun"
words = sentence.split()
print("Words in the sentence:", words)
# splitting using a different delimiter
csv_data = "name,age,city"
data_list = csv_data.split(",")
print("Data list from CSV:", data_list)
# joining a list of strings into a single string. 
# This method is actually a string method, not a list method. 
# We call it on the string that we want to insert between each “word” in the list, then pass the list as input:
joined_sentence = " ".join(words)
print("Joined sentence:", joined_sentence)
csv_joined = ",".join(data_list)
print("Joined CSV data:", csv_joined)

#tuples are similar to lists but they are immutable, meaning they cannot be modified after creation.
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(len(my_tuple))
# Tuple can also contain different data types
person_info = ("Keerthi Banala", 20, "Python Developer")
print(person_info)
# Indexing and slicing work the same way as lists
print("First element:", person_info[0])
print("Last element:", person_info[-1])
print("First 2 elements:", person_info[:2])

# tuples and lists can be converted to each other using the tuple() and list() functions
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print("List:", my_list)
print("Converted to tuple:", my_tuple)
my_tuple2 = (4, 5, 6)
my_list2 = list(my_tuple2)
print("Tuple:", my_tuple2)
print("Converted to list:", my_list2)   

# strings can also be converted to lists or tuples, which will create a list or tuple of individual characters
print(list('abc'))
print(tuple('abc'))




