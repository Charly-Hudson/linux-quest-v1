import datetime
import json
import os
from random_word import RandomWords


now = datetime.datetime.now()
today_key = "day-" + now.strftime("%d/%m/%Y")

r = RandomWords()
secret_word = r.get_random_word()
# testing
# print(secret_word)
word_length = len(secret_word)
counter = word_length - 2
letters_revealed = 1

score_file_path = "./game/score.json"
day_file_path = "./game/day.json"

# Ensure score.json exists
if not os.path.exists(score_file_path) or os.stat(score_file_path).st_size == 0:
    with open(score_file_path, 'w') as f:
        json.dump({"score": 0}, f)

# Ensure day.json exists
if not os.path.exists(day_file_path) or os.stat(day_file_path).st_size == 0:
    with open(day_file_path, 'w') as f:
        json.dump({}, f)

# Load Score Data
with open(score_file_path, 'r') as score_file:
    score_data = json.load(score_file)
    score = score_data.get("score", 0)  # Default to 0 if missing

# Load Day Data
with open(day_file_path, 'r') as day_file:
    daily_guess = json.load(day_file)

# Ensure today's key exists in daily_guess
if today_key not in daily_guess:
    daily_guess[today_key] = {"date": now.strftime("%d/%m/%Y"), "tried": False, "beat": False}

tried = daily_guess[today_key]["tried"]
beat = daily_guess[today_key]["beat"]

# Prevent multiple attempts in a single day
if tried and beat:
    print("||------------------------------------||")
    print("||  You have already guessed today,   ||")
    print("|| You beat today, come back tomorrow ||")
    print("||------------------------------------||")
    exit()
elif tried and not beat:
    print("||---------------------------------||")
    print("|| You have already guessed today, ||")
    print("||    but you did not beat today   ||")
    print("||    Come back tomorrow to try    ||")
    print("||---------------------------------||")
    exit()

# Start the guessing loop
while counter > 0:
    print("||------------------------------||")
    print("|| What is today's secret word? ||")
    print("||------------------------------||")
    
    guess = input("Please Respond Here: ").strip()

    if guess.lower() == secret_word.lower():
        winnings = counter * 100
        points = score + winnings

        print("||-----------------------------||")
        print("|| You have guessed correctly! ||")
        print(f"|| You won {winnings} points      ||")
        print(f"|| You now have {points} points ||")
        print("||-----------------------------||")

        # Save the updated score
        with open(score_file_path, 'w') as score_file:
            json.dump({"score": points}, score_file)

        # Update daily guess data
        daily_guess[today_key]["tried"] = True
        daily_guess[today_key]["beat"] = True

        with open(day_file_path, 'w') as day_file:
            json.dump(daily_guess, day_file, indent=4)

        break

    else:
        counter -= 1
        print("||----------------------------------||")
        print("||   You have guessed incorrectly   ||")
        print(f"||     You have {counter} guesses left     ||")

        if letters_revealed < len(secret_word):
            print(f"|| Hint: The first {letters_revealed} letter(s) is: {secret_word[:letters_revealed]} ||")
            letters_revealed += 1  # Reveal one more letter

        print("||----------------------------------||")

# If the player runs out of attempts
if counter == 0:
    daily_guess[today_key]["tried"] = True
    daily_guess[today_key]["beat"] = False  # Mark the day as tried but failed

    with open(day_file_path, 'w') as day_file:
        json.dump(daily_guess, day_file, indent=4)

    print("||-----------------------------||")
    print("|| You have run out of guesses ||")
    print(f"||    The secret word was '{secret_word}' ||")
    print("||     Come back tomorrow      ||")
    print("||-----------------------------||")
