print("This is the 'read' function, basically with what you can read the content of a file")
with open("example.txt", "r") as f:
      reading = f.read()
      print("Full content:\n", reading)

print("This is the 'write' function, with which you can write anything in a file")
with open("example.txt", "w") as f:
      f.write("So, this is my Codingal After Class Project about File Handling in Python.")

print("This is the 'append' function, with which you can add more content to an existing file")
with open("example.txt", "a") as f:
     f.write("\nI have appended this line to the file")

split_words = reading.split()
print("\nSplit words:", split_words)

print("This is the 'readline' function, with which you can read a single line of a file")
with open("example.txt", "r") as f:
    print("Reading the first line")
    print(f.readline())

print("This is the 'readline' function, with which you can read a single line of a file, but you can also read multiple lines")
with open("example.txt", "r") as f:
    print("Reading multiple lines")
    print(f.readline())
    print(f.readline())

print("This is the 'for loop' function, with which you can read all the lines of a file multiple times")
with open("example.txt", "r") as f:
    print("Looping through the lines...")
    for line in f:
          print(line)

f.close()
