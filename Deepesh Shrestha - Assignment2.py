'''
Assignment - 2:

WAP that first gives 2 options: 
Sign up
Sign in

when 1 is pressed user needs to provide following information 
Username, 2. Password, 3. Mobile number
All this information is saved in a file everytime a new user signs up the same file is updated 
(hint Append over the same file)

when 2 is pressed 
User needs to provide username and password 
this username and password is checked with username and password in the database
if matched: 
welcome to the device and show their phone number 
else: 
terminate the program saying incorrect credentials 


Do it using json files, save everything to json and load from json 
'''

import json
import os

# File where user data will be saved
user_data_file = 'users.json'

# Function to load user data from the file
def load_user_data():
    if not os.path.exists(user_data_file):
        return {}
    with open(user_data_file, 'r') as file:
        return json.load(file)

# Function to save user data to the file
def save_user_data(user_data):
    with open(user_data_file, 'w') as file:
        json.dump(user_data, file, indent=4)

# Function to sign up a new user
def sign_up():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    mobile_number = input("Enter your mobile number: ")

    user_data = load_user_data()

    # Check if username already exists
    if username in user_data:
        print("Username already exists. Please choose a different username.")
        return

    # Add new user data
    user_data[username] = {
        'password': password,
        'mobile_number': mobile_number
    }

    save_user_data(user_data)
    print("Sign up successful!")

# Function to sign in an existing user
def sign_in():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    user_data = load_user_data()

    # Check if username and password match
    if username in user_data and user_data[username]['password'] == password:
        print(f"Welcome to the device! Your mobile number is {user_data[username]['mobile_number']}")
    else:
        print("Incorrect credentials!")

# Main function to handle user input
def main():
    while True:
        print("1) Sign up")
        print("2) Sign in")
        print("3) Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            sign_up()
        elif choice == '2':
            sign_in()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
import json
import os

# File where user data will be saved
user_data_file = 'users.json'

# Function to load user data from the file
def load_user_data():
    if not os.path.exists(user_data_file):
        return {}
    with open(user_data_file, 'r') as file:
        return json.load(file)

# Function to save user data to the file
def save_user_data(user_data):
    with open(user_data_file, 'w') as file:
        json.dump(user_data, file, indent=4)

# Function to sign up a new user
def sign_up():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    mobile_number = input("Enter your mobile number: ")

    user_data = load_user_data()

    # Check if username already exists
    if username in user_data:
        print("Username already exists. Please choose a different username.")
        return

    # Add new user data
    user_data[username] = {
        'password': password,
        'mobile_number': mobile_number
    }

    save_user_data(user_data)
    print("Sign up successful!")

# Function to sign in an existing user
def sign_in():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    user_data = load_user_data()

    # Check if username and password match
    if username in user_data and user_data[username]['password'] == password:
        print(f"Welcome to the device! Your mobile number is {user_data[username]['mobile_number']}")
    else:
        print("Incorrect credentials!")

# Main function to handle user input
def main():
    while True:
        print("1) Sign up")
        print("2) Sign in")
        print("3) Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            sign_up()
        elif choice == '2':
            sign_in()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()









