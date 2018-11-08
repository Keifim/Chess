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
        self.player = False # False is player 1(white) and True is player 2(black)

        self.white_pieces = [u"\u2654", u"\u2655", u"\u2656",u"\u2657",u"\u2658",u"\u2659"]
        self.black_pieces = [u"\u265A", u"\u265B", u"\u265C",u"\u265D",u"\u265E",u"\u265F"]

        self.layoutLenght = len(self.layout)

  def movement(self):
    self.layout[int(self.user_move_to[0:1])][int(self.user_move_to[1:2])] = self.piece
    self.layout[int(self.user_move_from[0:1])][int(self.user_move_from[1:2])] = u"\u2610"
    self.move = False

  def pieceMove(self):
    if self.user_move_to != self.user_move_from:
      self.piece = self.layout[int(self.user_move_from[0:1])][int(self.user_move_from[1:2])]
      print(self.piece)
      print(self.player)

      # Piece Rules:
      self.king = [int(self.user_move_from[0:1])+1,
        int(self.user_move_from[0:1])-1,
        int(self.user_move_from[1:2])+1,
        int(self.user_move_from[1:2])-1,
        int(self.user_move_from[0:1]),
        int(self.user_move_from[1:2])]

      if self.piece in self.white_pieces and self.player == False:
        print("player 1 true")
        if self.piece == self.white_pieces[0]:
          print("player 1 piece true")
          print(self.king)
          print(self.user_move_to[0:1], self.king[0:2], self.king[4:6])
          print(self.user_move_to[1:2], self.king[2:4], self.king[4:6])

          if int(self.user_move_to[0:1]) in self.king[0:2] \
            and int(self.user_move_to[1:2]) in self.king[2:4] \
            or int(self.user_move_to[0:1]) in self.king[4:6] \
            and int(self.user_move_to[1:2]) in self.king[2:4] \
            or int(self.user_move_to[1:2]) in self.king[4:6] \
            and int(self.user_move_to[0:1]) in self.king[0:2]:
            print("can move true")
            self.movement()

      elif self.piece in self.black_pieces and self.player == True:
        pass

      elif self.piece == u"\u2610":
        pass


  def outlines(self):
    #print("\033c")
    self.lowerRow = ""
    for y, obj in enumerate(self.layout):
      print(str(y)+" "+" | ".join(self.layout[y]))
      self.lowerRow+="  "+str(y)+" "
    print(self.lowerRow)

  def userinput(self):
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
      self.userinput()
      #if self.player == False: self.player = True
      #else: self.player = False
      self.move = True

  def run(self):
    self.engine()

Chess(layout).run()
