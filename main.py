import inquirer

class Guess:
    def __init__(self, low, high) -> None:
        self.low = low
        self.high = high
        self.guess = (self.low+self.high)//2
    
    def play(self):
        while self.guess < self.high:
            print ('\n'+str(self.guess))
            user_input = input('\n[?] Was my guess correct? (y/n): ')

            while True:
                if user_input.lower() not in 'yn':
                    user_input = input('\nPlease enter (y/n) only.\n[?] Was my guess correct? (y/n): ')
                else:
                    break

            if user_input.lower() == 'y':
                print ('\nI did it ;D')
                break
            elif user_input.lower() == 'n':
                guess_confirmation = input('\n[?] Was my guess lower or higher?\nEnter >>> "l" for lower\nEnter >>> "h" for higher\n>>> ')

                while True:
                    if guess_confirmation.lower() not in 'lh':
                        guess_confirmation = input('\nPlease enter (h/l) only.\n[?] Was my guess higher or lower?\nenter >>> "l" for lower\nenter >>> "h" for higher\n>>> ')
                    else:
                        break

                if guess_confirmation.lower() == 'l':
                    self.high = self.guess
                if guess_confirmation.lower() == 'h':
                    self.low = self.guess + 1
                self.guess = (self.low+self.high)//2

if __name__ == "__main__":
    input('\nWelcome to "Number Guessing Game".\nIn this game, you will be asked to enter two numbers and think of any number between them. Then and I will try to guess that number.\nPress any button to continue.\n')
    while True:
        try:
            low = int(input('\nEnter the lower number: '))
            high = int(input('\nEnter the higher number: '))
        except ValueError:
            print("\nNot a number!\nPlease enter valid numbers")
            continue
        else:
            break
    game = Guess(low, high)
    game.play()