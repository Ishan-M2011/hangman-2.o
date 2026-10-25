import random

words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]
print("Welcome to Hangman! You have to type the whole word to be marked correct. If not, then you will be told which letter inside your input is inside the word.")
random_word = random.choice(words)
while True:
    j = 0
    guessed = str(input("Type in your guess!")).lower().strip()
    

    if guessed == random_word:
        print("WORD GUESSED!")
        break
    while len(guessed) != 1:
        guessed = input("Please type only 1 letter (or the exact full word)! ").lower().strip()
        if guessed == random_word:
            print("WORD GUESSED!")
            break
    if guessed == random_word:
        break
    if guessed in random_word:
        print(f"The letter '{guessed}' is correct!")
    else:
        print(f"The letter '{guessed}' is NOT correct!")
