

def calculate_statistics(numbers):
    if not numbers:  
        print("The list is empty. Please enter some numbers.")
        return

   
    num_elements = len(numbers)
    largest = max(numbers)
    smallest = min(numbers)
    average = sum(numbers) / num_elements

    positive_count = sum(1 for num in numbers if num > 0)
    negative_count = sum(1 for num in numbers if num < 0)

   
    print(f"Number of elements: {num_elements}")
    print(f"Largest number: {largest}")
    print(f"Smallest number: {smallest}")
    print(f"Average: {average}")
    print(f"Positive numbers: {positive_count}")
    print(f"Negative numbers: {negative_count}")

def main():
    try:
        numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
        calculate_statistics(numbers)
    except ValueError:
        print("Invalid input. Please enter only integers separated by spaces.")

if __name__ == "__main__":
    main()