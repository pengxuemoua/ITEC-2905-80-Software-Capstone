print('Welcome to the list of classes program!')

classes = input('Please enter the classes you are taking this semester followed by a comma. (Ex: algebra,biology,pharmacy): ')

list_of_classes = classes.split(",") # split input and store input into a list data set

for index in range(0, len(list_of_classes)): # use for loop to print each value in list_of_classes based on index value
    print(list_of_classes[index])
