import random

def randint(mini,maxi):
    secretNumber=random.randint(mini,maxi)
    return secretNumber

    
    
    
print("Number Guessing Game")
level=input("Please Choose Between Difficulty Level 1-3: ")
if level=="1":
    print("Difficulty Level 1\nGuess A Number Between 1 and 10")
    guess_count=0
    guess_limit=6
    secretNumber=randint(1,10)
    while guess_count<guess_limit:
        print(f"Guesses Left: {guess_limit - guess_count}")
        guess=int(input("Guess: "))
        guess_count+=1
        if guess==secretNumber:
            print("You Guessed Right!")
            break
        else:
            print("That Was Wrong!")
    else:
        print("Your 6 guesses were wrong!")
        print(f"Correct Number is {secretNumber}\nGame Over!")
        
elif level=="2":
    print("Difficulty Level 2\nGuess A Number Between 1 and 20")
    guess_count=0
    guess_limit=4
    secretNumber=randint(1,20)
    while guess_count<guess_limit:
        print(f"Guesses Left: {guess_limit - guess_count}")
        guess=int(input("Guess: "))
        guess_count+=1
        if guess==secretNumber:
            print("You Guessed Right!")
            break
        else:
            print("That Was Wrong!")
    else:
        print("Your 4 guesses were wrong!")
        print(f"Correct Number is {secretNumber}\nGame Over!")
        
elif level=="3":
    print("Difficulty Level 3\nGuess A Number Between 1 and 50")
    guess_count=0
    guess_limit=3
    secretNumber=randint(1,50)
    while guess_count<guess_limit:
        print(f"Guesses Left: {guess_limit - guess_count}")
        guess=int(input("Guess: "))
        guess_count+=1
        if guess==secretNumber:
            print("You Guessed Right!")
            break
        else:
            print("That Was Wrong!")
    else:
        print("Your 3 guesses were wrong!")
        print(f"Correct Number is {secretNumber}\nGame Over!")
else:
    print("You've Not Selected Any Level")
    