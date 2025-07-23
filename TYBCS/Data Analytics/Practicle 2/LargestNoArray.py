n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    num = int(input(f"Enter element {i + 1}: "))
    arr.append(num)

largest = max(arr)
print("Largest number in the array is:", largest)


#second logic with uing list inpiut method

user_input = input("Enter the numbers :")

numbers = list(map(int , user_input.split()))

array_sum = sum(numbers)

print("The sum of the array is :", array_sum)
largest = max(numbers)
print("Largest number in the array is:", largest)

