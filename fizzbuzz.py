# FizzBuzz

start = int(input("Enter the starting value: "))
end = int(input("Enter the ending value: "))

def fizzbuzz(start, end):
    if start > end:
        print("Start should be less than or equal to end.")
        return
    
    for number in range(start, end + 1):
        if number % 15 == 0:
            print("FizzBuzz")
        elif number % 5 == 0:
            print("Buzz")
        elif number % 3 == 0:
            print("Fizz")
        else:
            print(number)

fizzbuzz(start, end)
