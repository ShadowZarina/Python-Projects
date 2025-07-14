# Palindrome Checker

word = input("Enter a word: ")
first = 0
last = len(word) - 1

def palindrome_check(word, first, last):
    for letter in word:
        while first < last:
           if word[first] == word[last]:
              first += 1
              last -= 1
           else:
               print(f"The word {word} is not a palindrome.")
               return
        
    print(f"The word {word} is a palindrome.")
    
palindrome_check(word, first, last)
