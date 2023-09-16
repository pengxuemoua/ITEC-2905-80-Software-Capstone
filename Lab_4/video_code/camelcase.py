"""camelCase converter program. """

def camel_case(sentence):
    list_camel_case = sentence.split(' ') #store input in a list.
    #loop through list and camel case each word, then update the list
    for index in range(0, len(list_camel_case)):
        if index == 0:
            list_camel_case[index] = list_camel_case[index].lower()
        else:
            list_camel_case[index] = list_camel_case[index].title()

    # turn list back into a string and remove space
    camel_case_sentence = ''.join(list_camel_case)
    return camel_case_sentence
    #display_message = f"This is your camelCase sentence: {camel_case_sentence}. Thank you for using our program!"
    #return display_message
def banner():
    """Display program name, using stars """
    message = "Awesome camelCase program!"
    stars = '*' * len(message)
    print(f"\n{stars} \n{message} \n{stars}")

def instructions():
    """Display instructions for how to user the program """
    print('Enter a sentence and this program will convert to camelCase')

def main():
    banner()
    instructions()
    sentence = input('Please enter a sentence please: ').lower()
    output = camel_case(sentence)
    print(output)

if __name__ == '__main__':
    main()
