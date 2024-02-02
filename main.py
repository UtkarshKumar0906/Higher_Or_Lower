import random
from gamedata import data
from art import logo
from art import vs
from replit import clear

def assign():
    return random.choice(data)

def compare(Account1, Account2, user_input):
    follower1 = Account1['follower_count']
    follower2 = Account2['follower_count']

    max_name = ""

    if follower1 > follower2:
        max_name = Account1['real_name']
    else:
        max_name = Account2['real_name']

    if max_name == user_input:
        return True
    else:
        return False

def higher_or_lower():
    playing_game = True
    while playing_game:
        score = 0
        still_guessing = True
        while still_guessing:
            clear()
            print(logo)

            person1 = assign()
            person2 = assign()

            if score > 0:
                person1 = person2
                person2 = assign()

            print(f"Name: {person1['real_name']}, Account: {person1['account_name']}, Desc: {person1['description']}")
            print(vs)
            print(f"Name: {person2['real_name']}, Account: {person2['account_name']}, Desc: {person2['description']}")
            print("----------------------------------------------")
            print(f"Your current score is: {score}")
            print("----------------------------------------------")

            guess = input("Enter who do you think has higher follower: ")

            if compare(person1, person2, guess):
                score += 1
            else:
                still_guessing = False

        play_again = input("Want to Play Again? (y/n): ").lower()

        if play_again == 'y':
            continue
        elif play_again == 'n':
            playing_game = False
            clear()
        else:
            playing_game = False

playing = input("Would you like to play Higher or Lower? (Press 'y' for yes, 'n' for no)\n").lower()

if playing == 'y':
    clear()
    higher_or_lower()
elif playing == 'n':
    print("Program exited successfully")
else:
    print("Invalid argument. Program has been exited.")
