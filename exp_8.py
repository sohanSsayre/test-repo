# Assignment8 Python Programs on File Handling
# Python Program to Read the Contents of the File
#1 Writing to a Text File
filename = "example.txt"
content_to_write = "Hello, Python file handling is easy with Python!"

try:
    # Open the file in write mode ('w')
    with open(filename, 'w') as file:
        file.write(content_to_write)
    print(f"Successfully wrote to {filename}")
except IOError as e:
    print(f"Error writing to file: {e}") 


#2. Reading from a Text File
filename = "example.txt"
try:
    # Open the file in read mode ('r')
    with open(filename, 'r') as file:
        content = file.read()
        print(f"Content of {filename}:")
        print(content)
except FileNotFoundError:
    print(f"Error: The file {filename} does not exist.")
except IOError as e:
    print(f"Error reading file: {e}") 

#3. Appending to a Text File
filename = "example.txt"
content_to_append = "\nThis line was appended later."

try:
    # Open the file in append mode ('a')
    with open(filename, 'a') as file:
        file.write(content_to_append)
    print(f"Successfully appended to {filename}")
except IOError as e:
    print(f"Error appending to file: {e}")

# 4. Counting Words in a File 
filename = "example.txt"
word_count = 0

try:
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()
        word_count = len(words)
    print(f"Total number of words in {filename}: {word_count}")
except FileNotFoundError:
    print(f"Error: The file {filename} does not exist.")
except IOError as e:
    print(f"Error reading file: {e}")

#4 Deleting a File

import os

filename_to_delete = " example.txt "

# Now attempt to delete the file
if os.path.exists(filename_to_delete):
    os.remove(filename_to_delete)
    print(f"{filename_to_delete} has been deleted.")
else:
    print(f"The file {filename_to_delete} does not exist.")