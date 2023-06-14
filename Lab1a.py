def helloWorld():
	print(‘Hello World’)


helloWorld()

import datetime

def calculate_age():
    try:
        current_year = datetime.datetime.now().year
        birth_year = int(input("Enter your birth year: "))
        age = current_year - birth_year
        return age
    except TypeError:
        print("Please enter an integer for the birth year.")
        return None

