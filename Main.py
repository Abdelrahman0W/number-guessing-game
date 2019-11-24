#Guess The Number Game (Computer Guesses)

l = 0
h = 100
g = 50
while g < 100:
    print (g)
    x = input()
    if x == 'h':
        l = g + 1
    if x == 'l':
        h = g
    g = (l+h)//2
    if x == 'c':
        print ('Game Over!\nComputer Wins ;D')
        break
