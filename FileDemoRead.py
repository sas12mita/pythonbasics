# Accessing a text file to read the data from it.
# Change the path relevant to where you have saved the files.
fr = open("sample.txt", "r")

# Read all the data from the text file and display it on the terminal/console
print(fr.read())

# Close the text file after reading the data from it
fr.close()
