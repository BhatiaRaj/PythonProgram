# Create a program that asks the user to enter their name and their age. Printout a message addressed to them that tells them the year that they will turn 100 years old.
name = input("Enter your name: ")  # user input
current_age = int(input("Enter your age: "))  # user input
# calculating the 100th year, considering 2020 as the current year
hundredth_year = 2020 + (100 - current_age)
print(f'{name} will become 100 years old in the year {hundredth_year}.')
