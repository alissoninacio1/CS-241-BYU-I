#Homework- used in python 3

def prompt_filename():
  filename = input("Enter a file name: ")
  return filename
  
def parse_file(filename):
  count = 0
  with open(filename) as f:
    for line in f:
      words = line.split()
      for word in words:
        if word == "pride":
          count += 1
  return count
  
  
  
def main():
  filename = prompt_filename()
  print(f"Opening file {filename}") # f strings format
  
  count = parse_file(filename)
  print(f"The word pride occurs {count} times in this file.")
  

  
  

if __name__ == "__main__":
  main()
  
