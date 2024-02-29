#Step 1
import random, requests

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosend_word = random.choice(requests.get('https://random-word-api.herokuapp.com/all').json())
placeholder = ''.join(['_' for i in chosend_word])
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
count_mistakes = 0
count_right_answers = 0
while (count_mistakes < 6 and\
      placeholder.count('_') != 0):
    guess = \
    input(f"{placeholder}\nGuess a letter: ").lower()
    #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    if guess in chosend_word and guess not in placeholder:
        for i in range(0, len(chosend_word)):
            if chosend_word[i] == guess:
                arr = list(placeholder)
                arr[i] = guess
                placeholder = ''.join(arr)
        print(placeholder)
        count_right_answers += 1
    elif count_mistakes == 0:
        print("""
    +_____________+
    |             |
    |             |
    |             |
    |             |
    |             O
    |
    |
    |
    |
    |
    |
    |
    |
    |
  ======================================
    """)
        count_mistakes += 1
    elif count_mistakes == 1:
        print("""
      +_____________+
      |             |
      |             |
      |             |
      |             |
      |             O
      |             |
      |
      |
      |
      |
      |
      |
      |
      |
    ======================================
      """)
        count_mistakes += 1
    elif count_mistakes == 2:
        print("""
      +_____________+
      |             |
      |             |
      |             |
      |             |
      |             O
      |            /|
      |
      |
      |
      |
      |
      |
      |
      |
    ======================================
      """)
        count_mistakes += 1
    elif count_mistakes == 3:
        print("""
      +_____________+
      |             |
      |             |
      |             |
      |             |
      |             O
      |            /|\\
      |
      |
      |
      |
      |
      |
      |
      |
    ======================================
      """)
        count_mistakes += 1
    elif count_mistakes == 4:
        print("""
      +_____________+
      |             |
      |             |
      |             |
      |             |
      |             O
      |            /|\\
      |            /
      |
      |
      |
      |
      |
      |
      |
    ======================================
      """)
        count_mistakes += 1
    elif count_mistakes == 5:
        print("""
      +_____________+
      |             |
      |             |
      |             |
      |             |
      |             O
      |            /|\\
      |            / \\
      |
      |
      |
      |
      |
      |
      |
    ======================================
      """)
        count_mistakes += 1
# Result
if count_mistakes < 6:
    print('You win!')
else:
    print(f'You loose! Secret word: {chosend_word}')
