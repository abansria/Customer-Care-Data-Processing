#Amit Bansria
#BS Computer Science Assignment Project
#Data Processing
#June 4, 2024

# importing the os module (Downey, 2015, p. 139)
import os

# function that logs error to a file 
# Reference my Discussion Assignment 8_Part_2
def log_err_inFile(error_message):
    # (Schafer, 2016)
    with open("error.log", "a") as log_file:
        log_file.write('\nError Code 0\n')

# A function that returns a dictionary from a file
def readfileDictionary(fileDictionary):

    # initializing an empty dictionary (Downey, 2015, p. 105)
    emptyDictionary1 = {}

    # tries to open the file (Schafer, 2016)
    with open(fileDictionary, 'r') as file:
        # once open iterates through each line, and prints them
        for line in file:
            # line.strip() would produce "ticket001: inquiry_type = "New Account Setup"; resolution_time = "17m"; customer_satisfaction = "5/5"".
            # ("Python string strip() method," n.d.)
            # line.strip().split(': ') would produce ["ticket001", "inquiry_type = "New Account Setup"; resolution_time = "17m"; customer_satisfaction = "5/5""]
            # ("Python string split() method," n.d.)
            # key, value = line.strip().split(': ') 
            #               would assign key = "ticket001" and value = "inquiry_type = "New Account Setup"; resolution_time = "17m"; customer_satisfaction = "5/5"".
            # (Downey, 2015, p. 120)
            key, value = line.strip().split(': ')
            # writes to the new dictionary
            emptyDictionary1[key] = value
    return emptyDictionary1 # returns the dictionary with function call

# A function that returns a reversed dictionary from a dictionary
# This function is similar to my function used for Assignment 7
# invertDictionary(dictionary) - reference to my assignment 7
def reversefileDictionary(dictionary):
    # initializing an empty dictionary (Downey, 2015, p. 105)
    emptyDictionary2 = {}   
    
    # traversing for the keys within this dictionary one by one
    # (Downey, 2015, pp. 107-108)
    for keys, values in dictionary.items():        
        # Suppose values are "inquiry_type = "New Account Setup"; resolution_time = "17m"; customer_satisfaction = "5/5"".
        # values.split(', ') converts it into the list ["inquiry_type = "New Account Setup"; resolution_time = "17m"; customer_satisfaction = "5/5""]
        # traversing the list one item at a time
        for individualvalue in values.split(', '):

            # if the item is not found in the new dictionary
            # that we declared above in line 43
            if individualvalue not in emptyDictionary2:
                # then the inverse dictionary current key is initialized to empty   #
                # this is done to avoid a KeyError; (Downey, 2015, p.197)           #
                # if the key is not initialized in the dictionary we get an         # 
                # exception, when we try to append (Downey, 2015, p.104)            #
                emptyDictionary2[individualvalue]=[]
            
            # now we can add the key (ticket number) as a value 
            # (Downey, 2015, pp. 107-108)
            emptyDictionary2[individualvalue].append(keys)

    return emptyDictionary2 #returns the new reversed dictionary

# A function that writes the dictionary to a file
def writefileDictionary(dictionary, outputfile):

    # tries to create the file (Schafer, 2016)
    with open(outputfile, 'w') as file:
        # once the file is initialized we iterate through
        # the dictionary, writing line by line the key, value pairs
        for key, value in dictionary.items():
            # Create a string from the list of values
            # ("Python string join()," n.d.)
            value_string = ', '.join(value)
            # Write the key and the joined string values to the file
            # (Schafer, 2016), ("Python file write," n.d.)
            file.write(key + ": " + value_string + "\n")


# the body of the main function
def main():
    
    # catching exceptions (Downey, 2015, pp. 140-141)
    try:
        # captures the path information from the user for this file
        folder = input('Enter the path of the file: ')   

        # asks the user to enter the name of the file
        enter_file = input('Enter file name to read: ')

        #joining the directory and the filename to build the full path
        #(Downey, 2015, p. 140)
        full_path = os.path.join(folder, enter_file) 
        
        # storing the contents of the 'customer_care_raw_data.txt' file in a dictionary
        fileDictionary = readfileDictionary(full_path)

        # reversing the contents of the dictionary 
        # (Keys become values; and vice versa)
        reverseDictionary = reversefileDictionary(fileDictionary)

        # writing out the contents of this 
        # reversed dictionary to a file as specified
        output_file = input('Enter output file name: ')

        #joining the directory and the filename to build the full path
        #(Downey, 2015, p. 140)       
        full_path2 = os.path.join(folder, output_file)
        writefileDictionary(reverseDictionary, full_path2)

    except FileNotFoundError: # ("Built-in exceptions," n.d.)
        # if the file is not found it prints an error on the screen
        error_message = 'File not found, try again!'
        print(error_message)

        # calls this function to write the error code to a log file
        log_err_inFile(error_message)

# running the main function
main()
