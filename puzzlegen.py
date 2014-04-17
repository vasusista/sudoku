from numpy import *
import json
import sys

def reduce_options(board, Pcube):
  row,col = where(board == 0)
  playoption = []
  for i in range(9):
    for j in range(9):
      if board[i,j] != 0:
        Pcube[i,j,Pcube[i,j]!=board[i,j]] *= 0
  for i,j in zip(row,col):
    exclude = set(board[i])
    exclude = exclude.union(board[:,j])
    exclude = exclude.union(board[i/3*3:i/3*3+3,j/3*3:j/3*3+3].flat)
    for each in exclude:
      Pcube[i,j,Pcube[i,j]==each] = 0

  for layer in Pcube.T:
    for i in range(9):
      rowsfilled = sum(layer[i,:3])>0, sum(layer[i,3:6])>0, sum(layer[i,6:])>0
      if sum(rowsfilled) == 1:
        rowsfilled = repeat(rowsfilled,3)
        layer[i/3*3+(i+1)%3,rowsfilled] *= 0
        layer[i/3*3+(i+2)%3,rowsfilled] *= 0
    layer = layer.T
    for i in range(9):
      rowsfilled = sum(layer[i,:3])>0, sum(layer[i,3:6])>0, sum(layer[i,6:])>0
      if sum(rowsfilled) == 1:
        rowsfilled = repeat(rowsfilled,3)
        layer[i/3*3+(i+1)%3,rowsfilled] *= 0
        layer[i/3*3+(i+2)%3,rowsfilled] *= 0

  for i,j in zip(row,col):
    if count_nonzero(Pcube[i,j]) == 1:
      playoption.append( (i,j,sum(Pcube[i,j])) )
  return playoption

def isSolvable(testgame):
  board = testgame.copy()
  P = ones((9,9,9),int)
  for i in arange(9):
    P[:,:,i] *= i+1
  playorder = []
  laststate = sum(P)
  while sum(board == 0) > 0:
    playoptions = reduce_options(board, P)
    for i,j,v in playoptions:
      board[i,j] = v
    thisstate = sum(P)
    if thisstate == laststate:
      break
    else:
      laststate = thisstate
  return True if sum(board == 0) == 0 else False

def generate_game(x,method):
  S = array(x)
  gametest = S.copy()
  if method == 1:
    for i in range(81):
      #i = random.randint(81)
      if gametest.flat[i] != 0:
        temp = gametest.flat[i]
        gametest.flat[i] = 0
        if not isSolvable(gametest):
          gametest.flat[i] = temp

  elif method == 2:
    x = range(81)
    while x:
      i = random.choice(x)
      if gametest.flat[i] != 0:
        x.remove(i)
        temp = gametest.flat[i]
        gametest.flat[i] = 0
        if not isSolvable(gametest):
          gametest.flat[i] = temp

  return (81 - sum(gametest == 0))
  #return gametest

#print generate_game([[5, 2, 4, 3, 1, 9, 6, 7, 8], [7, 9, 1, 6, 8, 4, 3, 5, 2], [6, 8, 3, 5, 7, 2, 4, 1, 9], [3, 7, 5, 4, 9, 8, 2, 6, 1], [8, 4, 2, 1, 6, 7, 5, 9, 3], [9, 1, 6, 2, 5, 3, 7, 8, 4], [2, 6, 7, 9, 3, 1, 8, 4, 5], [1, 3, 8, 7, 4, 5, 9, 2, 6], [4, 5, 9, 8, 2, 6, 1, 3, 7]],2)

##for line in sys.stdin:
##  print generate_game(json.loads(line.strip()),2)

"""f = open('sudokus1.txt','rb')
for line in f:
  s = json.loads(line)
  print generate_game(s)"""