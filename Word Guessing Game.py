import random

word_collection = [
  "ADVENTURE",
  "TELEPHONE",
  "WONDERFUL",
  "EXCELLENT",
  "NEIGHBOR",
  "KITCHEN",
  "COMPUTER",
  "HOLIDAY",
  "ELEVATOR",
  "SCISSORS",
  "CHOCOLATE",
  "PROBABLY",
  "DIFFERENT",
  "RESTAURANT",
  "MAGNETIC",
  "SUFFICIENT",
  "CHAMPION",
  "CABINET",
  "GUARANTEE",
  "IMAGINE"
]

word = random.choice(word_collection)

guessed_word = ['_'] * len(word)
attempts = 10

while attempts > 0:
  print('\nCurrent word: ' + ' '.join(guessed_word))
  guess = char(input("Enter a letter: ").upper()

  if guess in word:
  for i in range(len(word)):
    if word[i] == guess:
      guessedWord[i] = guess
      print('Great guess!')
    else:
      attempts -= 1
      print('Wrong guess! Attempts left: ' + str(attempts))

    if '_' not in guessedWord:
          print('\nCongratulations!! You guessed the word: ' + word)
          break
      
  if attempts == 0 and '_' in guessedWord::
    print('\nYou\'ve run out of attempts! The word was: ' + word)
