#code for try and except.
#while True:
    #try:
        #code you want to try
        #break if successful

        #if block: (this can be used to check a range for example)
            #raise "error"

    #except "enter error":
        #print a message, ask for user to enter correct input


""" code without content manager. 
try:
    data_file = open('data.txt')
    contents = data_file.read()
    print(contents)
    data_file.close()
except FileNotFoundError:
    print('Sorry, file not found.')"""

try:
    # content manager, use "with", this will close a file if there is a problem
    with open('data.txt') as data_file:
        contents = data_file.read()
        print(contents)

except FileNotFoundError:
    print('Sorry, file not found.')





