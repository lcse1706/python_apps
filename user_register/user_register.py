def add_user():
  name = input('\nEnter new user: ')
  with open('users.txt', 'a') as file:
    file.write(name + "\n")
  print("User Added")

def show_users():
  try:
    with open("users.txt", "r") as file:
      users = file.readlines()
    if users:
      print("\nUsers:")
      for i, user in enumerate(users, start=1):
        print(f"{i}. {user.strip()}")
  except FileNotFoundError:
    print("No users file found. Add user first")

def main():  
  while True: 
    print("\nWelcome to User Register App.")
    print("1. Add User")
    print("2. Show Users List")
    print("3. Exit")
    choice = input("\nChoose an option: ")
    
    if choice == "1":
      add_user()
    elif choice == "2":
      show_users()
    elif choice == "3":
      print("\nExiting program. Bye !")
      break
    else:
      print("\nInvalid choice, please try again.")



if __name__ == "__main__":
  main()
