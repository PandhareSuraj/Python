n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    num = int(input(f"Enter element : "))
    arr.append(num)

total = sum(arr)
print("Sum of array elements:", total)


#second logic with uing list inpiut method

user_input = input("Enter the numbers :")

numbers = list(map(int , user_input.split()))

array_sum = sum(numbers)

print("The sum of the array is :", array_sum)
