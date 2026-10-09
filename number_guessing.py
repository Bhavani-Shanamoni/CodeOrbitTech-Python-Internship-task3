#importing the random module to generate random numbers
import random
# function to implement the number guessing game
def number_guessing_game():
    #for mutiple rounds of the game, we use a while loop
    while True:
        number = random.randint(1, 100)
        attempts = 0
        #using a while loop to allow the user to keep guessing until they get the correct number
        while True:
            guess = int(input("Guess a number between 1 and 100:"))
            attempts += 1
            if guess<number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            elif guess == number:
                print("Correct guess in", attempts, "attempts")
                break
            #asking the user if they want to play again after each round
        if (input("Do you want to play again? (yes/no): ").lower() == "no"):
            print("Thanks for playing!")
            break

#main function to call the number guessing game
def main():
    number_guessing_game()

#calling the main function to start the game
if __name__ == "__main__":
    main()