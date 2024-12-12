def main():
  odd = []
  even = []
  
  print("\nWelcome in odd/even calculator.")
  numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
  
  for number in numbers:
    if number % 2 == 0:
      even.append(number)
    else:
      odd.append(number)
  
  sum_even = sum(even)
  sum_odd = sum(odd)
  
  print("All Numbers: ", ", ".join(map(str, numbers)))  
  print("Even numbers: ", *even)  
  print("Odd numbers: ", ", ".join(map(str,odd)))  
  print("Sum of even numbers: ", sum_even)  
  print("Sum of odd numbers: ", sum_odd)  


if __name__ == "__main__":
  main()
