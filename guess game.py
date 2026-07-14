#number guessing game
import random
lowest_num=1
highest_num=1000
answer=random.randint(lowest_num,highest_num)
guesses=[]
print(f"select a number between {lowest_num} and {highest_num}")
while True:
    guess=input("enter the guessing element:")
    if guess.isdigit():
        guesses.append(guess)
        print(guesses)
    else:
        print("Incorrect")
        print(f"select a number between {lowest_num} and {highest_num}")
print()
