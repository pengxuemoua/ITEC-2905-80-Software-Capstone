print('Welcome to the camelCase program!')

camel_case = input('Please enter a sentence and our program will turn it into camelCase: ').lower()

list_camel_case = camel_case.split(' ') #store input in a list

#loop through list and camel case each word, then update the list
for index in range(0, len(list_camel_case)):
    if index == 0:
        list_camel_case[index] = list_camel_case[index].lower()
    else:
        list_camel_case[index] = list_camel_case[index].title()

# turn list back into a string and remove space
camel_case_sentence = ''.join(list_camel_case)

print(f"This is your camelCase sentence: {camel_case_sentence}. Thank you for using our program!")
