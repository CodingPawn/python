import random

mylist = ("secret", "fridge", "programmer", "bank", "money", "music", "security")
word = random.choice(mylist)
print("Player 1 - Pick a word; Player 2 - Guess it!")
print("I choose this one:")
allowed_errors = 6
guesses = []
done = False
while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")
    guess = input(f"Allowed errors left {allowed_errors}, next guess:\n ")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        allowed_errors -= 1
        if allowed_errors == 0:
            break

    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

if done:
    print({word})
    print(f"You guessed correctly! It was '{word}'.")
else:
    print(f"Game Over! The word was '{word}'.")
