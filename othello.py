# Othello/Reversi
import random
import sys
from gameRules import *

print('Welcome to Reversi!')

playerTile, computerTile = enterPlayerTile()

while True:
    finalBoard = playGame(playerTile, computerTile)

    # Display the final score.
    drawBoard(finalBoard)
    scores = getScoreOfBoard(finalBoard)
    print('X scored %s points. O scored %s points.' % (scores['X'], scores['O']))
    if scores[playerTile] > scores[computerTile]:
        print('You beat the computer by %s points! Congratulations!' % (scores[playerTile] - scores[computerTile]))
    elif scores[playerTile] < scores[computerTile]:
        print('You lost. The computer beat you by %s points.' % (scores[computerTile] - scores[playerTile]))
    else:
        print('The game was a tie!')

    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break
