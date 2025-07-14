# Vowel Checker

word = input("Please enter a word: ")


def vowel_check(word):
    letter = 0
    vowels = 0

    for letter in word.lower():
        if letter in "aeiou":
            vowels += 1
    
    print(f"The word {word} has {vowels} vowel(s).")

vowel_check(word)
