import sys
import random

# Retrieve input from PHP
if len(sys.argv) < 3:
    print("Invalid input")
    sys.exit(1)

number = int(sys.argv[1])
text = sys.argv[2]

# Task 1: Number Puzzle
if number % 2 == 0:
    number_result = f"The number {number} is even. Its square root is {number ** 0.5:.2f}."
else:
    number_result = f"The number {number} is odd. Its cube is {number ** 3}."

# Task 2: Text Puzzle
binary_text = ' '.join(format(ord(char), '08b') for char in text)
vowel_count = sum(1 for char in text.lower() if char in "aeiou")

text_result = f"Binary: {binary_text}\nVowel Count: {vowel_count}"

# Task 3: Treasure Hunt
secret_number = random.randint(1, 100)
attempts = 0
guess = 0
guesses = []

while attempts < 5:
    guess = random.randint(1, 100)  # Simulating user guesses
    guesses.append(guess)
    attempts += 1
    if guess == secret_number:
        break

if guess == secret_number:
    treasure_result = f"You found the treasure in {attempts} attempts!"
else:
    treasure_result = "You failed to find the treasure."

# Output results
print(f"{number_result}\n\n{text_result}\n\nTreasure Hunt:\nSecret Number: {secret_number}\nAttempts: {guesses}\n{treasure_result}")
