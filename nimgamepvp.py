from nimgametools import *

game = Game([4,3,2])
print('\n'*2)
print("Welcome to nimgame--------------------------------------------------------------")
while True:
    print('\n'*3)
    game.show()
    m = eval(input("Player "+str(game.player)+" enter your move as a tuple (heapno,noofcoins): "))
    w = game.move(m[1],m[0])
    if w is not None:
        print(w,"moved the last coin")
        break
    