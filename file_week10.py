import os
#Prompt user for a directory
directory = input("Please provide a directory to save a new file: ")

#Use try and except to display an error message if given a bad directory
try:
    os.path.isdir(directory)
    
except:
    print("Sorry, that directory does not exist.")
    quit()


file = input("What would you like to name your new file? ")
filepath = os.path.join(directory, file)

#Prompt user for personal information to be saved as the "info" variable
name = input("Please enter your name. ")
address = input("Please enter your address. ")
number = input("Please enter your phone number. ")

#Create file object to write specified file to a directory
try:    
    with open(filepath, 'w') as file_object: #Used to create a new file in write mode ('w')
        info = (name + ", " + address + ", " + number)
        file_object.write(info) #Write to the new file using the personal information provided by the user
except:
    print("Sorry, there was an error when creating your file.")
    quit()
try:
    with open(filepath) as file_object:
        print("You have created a new file called " + file + ". The following information has been added to the file: ")
        print(file_object.read())
except:
    print("Sorry, there was an error when attempting to read your file.")
    quit()