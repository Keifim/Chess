#!/usr/bin/env python3
# encoding utf-8
# board = [
#   ["black_rock", "black_knight", "black_bishop", "black_king", "black_queen", "black_bishop", "black_knight", "black_rock"],
#   ["black_pawn", "black_pawn", "black_pawn", "black_pawn", "black_pawn", "black_pawn", "black_pawn", "black_pawn"],
#   ["square", "square", "square", "square", "square", "square", "square", "square"],
#   ["square", "square", "square", "square", "square", "square", "square", "square"],
#   ["square", "square", "square", "square", "square", "square", "square", "square"],
#   ["square", "square", "square", "square", "square", "square", "square", "square"],
#   ["white_pawn", "white_pawn", "white_pawn", "whhite_pawn", "white_pawn", "white_pawn", "white_pawn", "white_pawn"],
#   ["white_rock", "white_knight", "white_bishop", "white_king", "white_queen", "white_bishop", "white_knight", "white_rock"],
# ]
import pickle
with open("layout", "wb") as file:
  layout = pickle.load(file)

layout = [
  [u"\u265C", u"\u265E", u"\u265D", u"\u265A", u"\u265B", u"\u265D", u"\u265E", u"\u265C"],
  [u"\u265F", u"\u265F", u"\u265F", u"\u265F", u"\u265F", u"\u265F", u"\u265F", u"\u265F"],
  [u"\u2610", u"\u2610", u"\u2610", u"\u2610", u"\u2610", u"\u2610", u"\u2610", u"\u2610"],
  [u"\u2610", u"\u2610", u"\u2610", u"\u2610", u"\u2610", u"\u2610", u"\u2610", u"\u2610"],
  [u"\u2610", u"\u2610", u"\u2610", u"\u2610", u"\u2610", u"\u2610", u"\u2610", u"\u2610"],
  [u"\u2610", u"\u2610", u"\u2610", u"\u2610", u"\u2610", u"\u2610", u"\u2610", u"\u2610"],
  [u"\u2659", u"\u2659", u"\u2659", u"\u2659", u"\u2659", u"\u2659", u"\u2659", u"\u2659"],
  [u"\u2656", u"\u2658", u"\u2657", u"\u2654", u"\u2655", u"\u2657", u"\u2658", u"\u2656"],
]

class Chess:
  def __init__(self, layout):
        self.layout = layout
        self.user_move_from = None
        self.user_move_to = None
        self.move = False

  def pieceMove(self):
    self.piece = self.layout[int(self.user_move_from[0:1])][int(self.user_move_from[1:2])]
    self.layout[int(self.user_move_to[0:1])][int(self.user_move_to[1:2])] = self.piece
    self.layout[int(self.user_move_from[0:1])][int(self.user_move_from[1:2])] = u"\u2610"
    self.move = False

  def outlines(self):
    self.lowerRow = ""
    for y, obj in enumerate(self.layout):
      print(str(y)+" "+" | ".join(self.layout[y]))
      self.lowerRow+="  "+str(y)+" "
    print(self.lowerRow)

  def movement(self):
    self.user_move_from = input("Move from: ")
    self.user_move_to = input("Move to: ")
    self.move = True

  def engine(self):
    while True:
      if self.move == True:
        self.pieceMove()
      self.outlines()
      self.movement()

  def run(self):
    self.engine()

Chess(layout).run()
