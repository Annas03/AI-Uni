# Open the file "demofile2.txt" and append content to the file:
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
f.close()

# Open the file "demofile3.txt" and overwrite the content
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())
f.close()

# Create a file called "myfile.txt"
f = open("myfile.txt", "x")
f.close()

# Create a new file if it does not exist
f = open("myfile.txt", "w")
f.close()