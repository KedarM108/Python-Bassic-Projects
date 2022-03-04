# 1.Guess the number

"""In this game you have to guess the number until you get it correct. """

actual_number = 50
attempts = 0


while True:
    attempts += 1
    guess = int(input("Guess a number from 1 to 50:\n"))
    if guess < actual_number:
         print("Your guess was too low.")
    elif guess>actual_number:\
        print("Your guess was too high.")
    else:
         print(f"You guessed it in {attempts} attempts.")
         break

