# getting secret word from API gateways
import datetime
import json

counter = 5

secret_word = ""

with open('score.json', 'r') as score:
    score = json.loads('score')

daily_guess = dict(json.loads())
with open('day.json', 'r') as day:
    daily_guess = json.load(day)


if daily_guess['date'[0]] == str(datetime.date.today()):
    x = False
    print("||--------------------------------||")
    print("|| You have already guessed today ||")
    print("||--------------------------------||")
else:
    x = True

while x:
    print("Hello")
    print("||-----------------------------||")
    print("|| What is todays secret word? ||")
    print("||-----------------------------||")
    input = input("Please Respond Here")
    
    if input == secret_word:
        print("||-----------------------------||")
        print("|| You have guessed correctly! ||")
        print("|| You won " + str(counter*100) + " points ||")
        print("|| You now have " + str(score+counter) + " points ||")
        print("||-----------------------------||")
        json.dumps(score+counter)
        x = False
    else:
        print("||------------------------------||")
        print("|| You have guessed incorrectly ||")
        print("|| You have " + str(counter) + " guesses left ||")
        print("||------------------------------||")
        counter -= 1

    if counter == 0:
        x = False

