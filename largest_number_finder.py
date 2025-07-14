# Largest Number Finder

numbers_str = input("Enter up to 10 numbers separated by spaces: ")
numbers = [int(number) for number in numbers_str.split()]

def largest_number(numbers):

    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number
    return largest
    

largest = largest_number(numbers)

print(f"The largest number in the list is {largest}.")
