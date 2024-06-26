import os
import string
import random
import json

# File for storing data
FILENAME = 'urls.json'

# Loading previously saved data
if os.path.exists(FILENAME):
    with open(FILENAME, 'r') as file:
        url_dict = json.load(file)
else:
    url_dict = {}

# Function to generate a unique identifier
def generate_short_id(length=6):
    characters = string.ascii_letters + string.digits
    while True:
        short_id = ''.join(random.choice(characters) for _ in range(length))
        if short_id not in url_dict:
            return short_id

# Function to save data to file
def save_urls():
    with open(FILENAME, 'w') as file:
        json.dump(url_dict, file)

# Main function of the program
def main():
    while True:
        print("1. Add new URL")
        print("2. Retrieve original URL")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            original_url = input("Enter the full URL: ")
            short_id = generate_short_id()
            url_dict[short_id] = original_url
            save_urls()
            print(f"Shortened URL: {short_id}")

        elif choice == '2':
            short_id = input("Enter the shortened URL: ")
            if short_id in url_dict:
                print(f"Original URL: {url_dict[short_id]}")
            else:
                print("No URL found for the given identifier.")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
