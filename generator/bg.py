import random

class GuessNumber:
    def __init__(self):
        self.number = random.randint(1, 100)
        self.guesses = 0
        self.game_over = False

    def play(self):
        while not self.game_over:
            guess = int(input("Guess a number between 1 and 100: "))
            self.guesses += 1
            if guess == self.number:
                print("You guessed the number in ", self.guesses," guesses!")
                self.game_over = True
            elif guess < self.number:
                print("Too low!")
            else:
                print("Too high!")

game = GuessNumber()
game.play()