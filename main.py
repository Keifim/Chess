#!/usr/bin/env python3
# encoding utf-8
import pickle
with open("layout", "rb") as file:
  layout = pickle.load(file)

class Chess:
  def __init__(self, layout):
        self.layout = layout
        self.user_move_from = None
        self.user_move_to = None
        self.move = False
        self.player = True # Falseeis player 1(white) and True is player 2(black)

        self.white_pieces = [u"\u2654", u"\u2655", u"\u2656",u"\u2657",u"\u2658",u"\u2659"]
        self.black_pieces = [u"\u265A", u"\u265B", u"\u265C",u"\u265D",u"\u265E",u"\u265F"]

  # Movement of pieces
  def pieceRules(self, moves):
    self.king = [1-int(moves), int(moves)+1]

  def pieceMove(self):
    self.piece = self.layout[int(self.user_move_from[0:1])][int(self.user_move_from[1:2])]
    print(self.piece)
    print(self.player)

    def move(self):
      self.layout[int(self.user_move_to[0:1])][int(self.user_move_to[1:2])] = self.piece
      self.layout[int(self.user_move_from[0:1])][int(self.user_move_from[1:2])] = u"\u2610"
      self.move = False

    if self.piece in self.white_pieces and self.player == False:
      print("player 1 true")
      if self.piece == self.white_pieces[0]:
        print("player 1 piece true")
        if int(self.user_move_to[0:1]) in self.king(self.user_move_to[0:1]):
            #or self.user_move_to in self.pieceRules(self.user_move_to[1:2]).self.king:
            print("can move true")
            move()

    elif self.piece in self.black_pieces and self.player == True:
      pass

    elif self.piece == u"\u2610":
      pass


  def outlines(self):
    self.lowerRow = ""
    for y, obj in enumerate(self.layout):
      print(str(y)+" "+" | ".join(self.layout[y]))
      self.lowerRow+="  "+str(y)+" "
    print(self.lowerRow)

  def movement(self):
    if self.player == True: print("Player 1's turn")
    else: print("Player 2's turn")
    self.user_move_from = input("Move from: ")
    self.user_move_to = input("Move to: ")
    self.move = True

  def engine(self):
    while True:
      if self.move == True:
        self.pieceMove()
      self.outlines()
      self.movement()
      if self.player == False: self.player = True
      else: self.player = False
      self.move = True

  def run(self):
    self.engine()

Chess(layout).run()
