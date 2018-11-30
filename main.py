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
        self.player = True # False is player 1(white) and True is player 2(black)

        self.white_pieces = [u"\u2654", u"\u2655", u"\u2656",u"\u2657",u"\u2658",u"\u2659"]
        self.black_pieces = [u"\u265A", u"\u265B", u"\u265C",u"\u265D",u"\u265E",u"\u265F"]

        self.move_king = None
        self.move_rock = None
        self.move_bishop = None
        self.move_queen = None
        self.move_knight = None
        self.move_pawn = None

        self.white_pawn_boost = []
        self.black_pawn_boost = []

        for index, object in enumerate(self.layout):
          for position, string in enumerate(object):
            if string == u"\u2659":
              self.white_pawn_boost.append(str(index)+str(position))
            elif string == u"\u265F":
              self.black_pawn_boost.append(str(index)+str(position))

  def movement(self):
    self.layout[int(self.user_move_to[0:1])][int(self.user_move_to[1:2])] = self.piece
    self.layout[int(self.user_move_from[0:1])][int(self.user_move_from[1:2])] = u"\u2610"
    self.move = False

  def pawnMove(self):
    if self.player == False and self.user_move_from in self.white_pawn_boost:
      self.white_pawn_boost.remove(self.user_move_from)
    elif self.player == True and self.user_move_from in self.black_pawn_boost:
      self.black_pawn_boost.remove(self.user_move_from)

    self.movement()

  def rock_queen_move(self):
    self.rank = []
    for index, object in enumerate(self.layout):
      for item, string in enumerate(object):
        if index == int(self.user_move_from[0:1]) or item == int(self.user_move_from[1:2]):
          self.rank.append(str(index)+str(item))

    self.unmovable = []
    for indx, xy in enumerate(self.rank):
      if self.layout[int(xy[0])][int(xy[1])] in self.white_pieces \
        or self.layout[int(xy[0])][int(xy[1])] in self.black_pieces:
        self.unmovable.append(xy)

    for xy in self.unmovable:
      self.rank.remove(xy)

    x=0;y=0
    for index, object in enumerate(self.layout):
      x+=1
      for item, string in enumerate(object):
        y+=1; break

    for _y in range(int(self.user.move_from[0:1]), y):
      print("_Y",_y)


    for _y in reversed(range(int(self.user_move_from[0:1]), 0):
        pass
        #print("_Y",_y)
                                                      ######### TOOO DOOO 

    print("rank"+str(self.rank))
    return self.rank

  def moveRules(self):

    # King rules
    self.king = [int(self.user_move_from[0:1])+1,
      int(self.user_move_from[0:1])-1,
      int(self.user_move_from[1:2])+1,
      int(self.user_move_from[1:2])-1,
      int(self.user_move_from[0:1]),
      int(self.user_move_from[1:2])]


    # Queen_bishop rules
    self.queen_bishop_move = []
    self.loop=0
    for i in self.rock_queen_move():
      if self.user_move_from[0:1] == i[0]:
        self.loop+=1
        self.queen_bishop_move.append(str(int(i[0])-int(self.loop))+str(int(self.user_move_from[1:2])-self.loop))
        self.queen_bishop_move.append(str(int(i[0])+int(self.loop))+str(int(self.user_move_from[1:2])-self.loop))
        self.queen_bishop_move.append(str(int(i[0])-int(self.loop))+str(int(self.user_move_from[1:2])+self.loop))
        self.queen_bishop_move.append(str(int(i[0])+int(self.loop))+str(int(self.user_move_from[1:2])+self.loop))

    # Knight rules
    self.knight = [
        str(int(self.user_move_from[0:1])+1)+str(int(self.user_move_from[1:2])+2),
        str(int(self.user_move_from[0:1])-1)+str(int(self.user_move_from[1:2])-2),
        str(int(self.user_move_from[0:1])+2)+str(int(self.user_move_from[1:2])+1),
        str(int(self.user_move_from[0:1])-2)+str(int(self.user_move_from[1:2])-1),

        str(int(self.user_move_from[0:1])+2)+str(int(self.user_move_from[1:2])-1),
        str(int(self.user_move_from[0:1])-2)+str(int(self.user_move_from[1:2])+1),
        str(int(self.user_move_from[0:1])+1)+str(int(self.user_move_from[1:2])-2),
        str(int(self.user_move_from[0:1])-1)+str(int(self.user_move_from[1:2])+2)
    ]

    # Pawn rules
    self.white_pawn = [int(self.user_move_from[0:1])-1, int(self.user_move_from[0:1])-2]
    self.black_pawn = [int(self.user_move_from[0:1])+1, int(self.user_move_from[0:1])+2]


    # King move
    if self.move_king == True:
      if int(self.user_move_to[0:1]) in self.king[0:2] \
        and int(self.user_move_to[1:2]) in self.king[2:4] \
        or int(self.user_move_to[0:1]) in self.king[4:6] \
        and int(self.user_move_to[1:2]) in self.king[2:4] \
        or int(self.user_move_to[1:2]) in self.king[4:6] \
        and int(self.user_move_to[0:1]) in self.king[0:2]:
          self.movement()
          self.move_king = False

    # Queen move
    elif self.move_queen == True:
      if self.user_move_to in self.rock_queen_move() or self.user_move_to in self.queen_bishop_move:
          self.movement()
          self.move_queen = False

    # Rock move
    elif self.move_rock == True:
      if self.user_move_to in self.rock_queen_move():
        self.movement()
        self.move_rock = False

    # Bishop move
    elif self.move_bishop == True:
      if self.user_move_to in self.queen_bishop_move:
        self.movement()
        self.move_bishop = False

    # Knight move
    elif self.move_knight == True:
      if self.user_move_to in self.knight:
        self.movement()
        self.move_knight = False

    # Pawn move
    elif self.move_pawn == True:
      if self.player == False \
        and int(self.user_move_to[0:1]) in self.white_pawn \
        and self.user_move_to[1:2] == self.user_move_from[1:2] \
        or self.player == True \
        and int(self.user_move_to[0:1]) in self.black_pawn \
        and self.user_move_to[1:2] == self.user_move_from[1:2]:
          if int(self.user_move_to[0:1]) == self.white_pawn[1] \
              and self.player == False \
              and self.user_move_from in self.white_pawn_boost \
              or int(self.user_move_to[0:1]) == self.black_pawn[1] \
              and self.player == True \
              and self.user_move_from in self.black_pawn_boost:
                self.pawnMove()
          elif int(self.user_move_to[0:1]) == self.white_pawn[0] \
              and self.player == False \
              or int(self.user_move_to[0:1]) == self.black_pawn[0] \
              and self.player == True:
                self.pawnMove()
          else:
            print("Can't move there")
          self.move_pawn = False


  def pieceMove(self):
    if self.user_move_to != self.user_move_from:

      self.piece = self.layout[int(self.user_move_from[0:1])][int(self.user_move_from[1:2])]
      self.piece_to = self.layout[int(self.user_move_to[0:1])][int(self.user_move_to[1:2])]

      if self.piece in self.white_pieces and self.player == False and self.piece_to not in self.white_pieces \
        or self.piece in self.black_pieces and self.player == True and self.piece_to not in self.black_pieces:

        # King
        if self.piece == self.white_pieces[0] or self.piece == self.black_pieces[0]:
          self.move_king = True
          self.moveRules()

        # Queen
        if self.piece == self.white_pieces[1] or self.piece == self.black_pieces[1]:
          self.move_queen = True
          self.moveRules()

        # Rock
        elif self.piece == self.white_pieces[2] or self.piece == self.black_pieces[2]:
          self.move_rock = True
          self.moveRules()

        # Bishop
        if self.piece == self.white_pieces[3] or self.piece == self.black_pieces[3]:
          self.move_bishop = True
          self.moveRules()

        # Knight
        elif self.piece == self.white_pieces[4] or self.piece == self.black_pieces[4]:
          self.move_knight = True
          self.moveRules()

        # Pawn
        elif self.piece == self.white_pieces[5] or self.piece == self.black_pieces[5]:
          self.move_pawn = True
          self.moveRules()

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
    if self.player == False: print("Player 2's turn")
    else: print("Player 1's turn")
    self.user_move_from = input("Move from: ")
    self.user_move_to = input("Move to: ")
    self.move = True

  def engine(self):
    while True:
      if self.move == True:
        self.pieceMove()
      self.outlines()
      self.userinput()
      if self.player == False: self.player = True
      else: self.player = False
      self.move = True

  def run(self):
    self.engine()

Chess(layout).run()
