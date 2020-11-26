import random
import hangman_art
import hangman_words

print(hangman_art.logo)

lives = len(hangman_art.stages)

chosen_word = random.choice(hangman_words.word_list)
len_word = len(chosen_word)

blank = "_"

display = []
for i in range(0,len_word):
  display += blank

count_guessed = 0
while count_guessed != len_word and lives > 0:
  initial_count = count_guessed
  guess = input("Guess a letter: ").lower()
  for i in range(0,len_word):
    if chosen_word[i] == guess:
      if display[i] == blank:
        display[i] = chosen_word[i]
        count_guessed += 1
      else:
        print("You have already guessed it")
        initial_count = -1
        break
  if count_guessed != initial_count:
    print(f"{' '.join(display)}")
  else:
    lives -= 1
    print(hangman_art.stages[lives])


if count_guessed == len_word:
  print("You Won")
else:
  print("He is DEAD!")
