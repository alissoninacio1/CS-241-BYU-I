file_name = input("Enter file:") #to enter a file name

num_lines = 0
num_words = 0

with open(file_name, 'r') as f:  #to read a file name
    for line in f:
      words = line.split(" ")
      num_words += len(words)
      num_lines += 1


print(f"The file contains {num_lines} lines and {num_words} words.")