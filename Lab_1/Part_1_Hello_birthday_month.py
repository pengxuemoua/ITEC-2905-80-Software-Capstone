print('Welcome to the birthday program!')

name = input('Please enter your name: ').title() # user's name
birth_month = input('Please enter the month you were born: ').title() # user's month of birth 

parse_name = len(name.replace(" ", "")) #remove space from name and calculate the length of the name

# greet user using their name and the number of letters in their name.
print(f'Welcome {name}! There are {parse_name} letters in your name.')

if birth_month == "August": #check if user was born in August
    print("Looks like it's your birthday! Happy birthday {name}!")
else:
    print("Looks like it's not your birthday yet. It was nice to meet you! Have a good day!")

