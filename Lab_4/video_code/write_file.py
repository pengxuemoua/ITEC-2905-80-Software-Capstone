"""How to write to a file in python. This code will overwrite the file. 
To prevent overwriting, use append, which is 'a' instead of 'w'."""

numbers = ['one','two','three']

try:

    #use a content manager, with open('file name', 'w' which means write) and as "enter variable name"
    with open('numbers.txt', 'w') as numbers_file:
        #numbers_file.writelines(numbers) will write into file with numbers list, will be concat
        for number in numbers:
            numbers_file.writelines(number + '\n') # new line will be added
except OSError: # OS error.
    print('Error, writing to file.')