
message = "My name is Keerthi and I am learning Python programming."
# String indexing
print("First character:", message[0])
print("Tenth character:", message[9])
print("Last character:", message[-1])   

#String length 
print("Length of the string:", len(message))

# String slicing
print("First 10 characters:", message[:10])
print("Characters from index 11 to 20:", message[11:21])
print("Last 10 characters:", message[-10:])

# String methods
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())
print("Title Case:", message.title())
print("Replace 'Python' with 'programming':", message.replace("Python", "programming"))
print("Split into words:", message.split())
print("Find index of 'Keerthi':", message.find("Keerthi"))
print("Count occurrences of 'a':", message.count("a"))
#stripping whitespace
string_with_whitespace = "   Hello, World!   "
print("Original string with whitespace:", string_with_whitespace)
print("Stripped string:", string_with_whitespace.strip())    

#String concatenation
greeting = "Hello"
name = "Keerthi"
full_greeting = greeting + ", " + name + "!"
print(full_greeting)    

# String formatting
age = 20
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string) 

# String formatting with format() method
formatted_string2 = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string2)    

# String formatting with % operator
formatted_string3 = "My name is %s and I am %d years old." % (name, age)
print(formatted_string3)     

# Number formatting in strings
pi = 3.14159
formatted_pi = f"Pi is approximately {pi:.2f}"
print(formatted_pi)

#   String escape characters
print("This is a new line.\nThis is another line.")
print("This is a tab:\tThis is after the tab.")
print("This is a backslash: \\")
print("This is a double quote: \"")
print("This is a single quote: \'")

#Triple quotes for multi-line strings
multi_line_string = """This is a multi-line string.
It can span multiple lines.
It preserves the formatting."""
print(multi_line_string)

