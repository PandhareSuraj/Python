user_input = input("Enter the numbers: ")
numbers = list(map(int, user_input.split()))
even_numbers = [num for num in numbers if num % 2 == 0]

print("Even numbers in the array are:", even_numbers)

