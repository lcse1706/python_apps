def show_menu():
  print("\nShopping List Menu:")
  print("1. Add Item")
  print("2. Remove Item")
  print("3. Show List")
  print("4. Exit")

def add_item(shopping_list):
  item = input('Enter Item to add: ')
  shopping_list.append(item)
  print(f"'{item}' has been added to the list.")

def remove_item(shopping_list):
  item = input('Enter the item to remove: ')
  if item in shopping_list:
    shopping_list.remove(item)
    print(f"'{item}' removed from the list.")
  else:
    print(f"'{item} is not on the list.'")

def show_list(shopping_list):
  if shopping_list:
    print('\nCurrent Shopping List: ')
    for index, item in enumerate(shopping_list, start=1):
      print(f"'{index}. {item}'")
    else:
      print('Shopping list is empty.')

def main():
  shopping_list = []
  while True:
    show_menu()
    choice = input('Choose an option (1-4): ')


    if choice == '1':
      add_item(shopping_list)
    elif choice == '2':
      remove_item(shopping_list)
    elif choice == '3':
      show_list(shopping_list)
    elif choice == '4':
      print("Exiting the shopping list app. Bye !")
      break
    else:
      print("Invalid choice. Please choose valid option (1-4).")

if __name__ == "__main__":
  main()