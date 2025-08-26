import re

def main():

    num = input("Enter a number/numerals to convert: ")

    if num.isdigit():
        print(number_to_roman(num))
    else:
        print(roman_to_number(num))

def number_to_roman(num):

    number = int(num)

    if not (1 <= number <= 3999):
        raise ValueError("Input number must be between 1 and 3999.")

    roman = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    result = []
    for value, symbol in roman:
        while number >= value:
            result.append(symbol)
            number -= value
    roman_result = "".join(result)
    return roman_result

def roman_to_number(num):

    numeral = num.upper()

    valid_roman_pattern = re.compile(
        r"^M{0,3}"          
        r"(CM|CD|D?C{0,3})"    
        r"(XC|XL|L?X{0,3})"    
        r"(IX|IV|V?I{0,3})$"   
    )

    if not valid_roman_pattern.match(numeral):
        raise ValueError(f"Invalid Roman numeral: {numeral}")

    roman = {
        'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
        'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
        'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
    }

    i = 0
    result = 0
    while i < len(numeral):
        # Check for two-character matches first
        if i+1 < len(numeral) and numeral[i:i+2] in roman:
            result += roman[numeral[i:i+2]]
            i += 2
        else:
            result += roman[numeral[i]]
            i += 1
    return result

main()
