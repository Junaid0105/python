# this is one method to open the file and write the content in it
# in this method we need to close the file after work
file = open("error_handling/test.txt","w")
try:
    file.write("This file is used for testing purpose")
finally:
    file.close()

# This is the second method to open the file
with open("error_handling/secon_test.txt", "w") as file:
    file.write("This is second method to open and write the file")