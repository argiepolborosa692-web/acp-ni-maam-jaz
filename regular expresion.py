import re

regex_pattern = r'^[A-Za-z]{3}\d{2}[A-Za-z]{2}\d{4}$'

while True: 
    user_input = input("Enter a string to match the pattern (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    if re.match(regex_pattern, user_input):
        print("Match found!")
    else:
        print("No match.")
