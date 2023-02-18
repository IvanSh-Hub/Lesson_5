import random

# Напишите программу, удаляющую из текста все слова, содержащие ""абв""

# string = "амотваиту абв ывавиабвывпварабв  вп ыва абв"
# newStr = string.replace('абв', '')
# print(newStr)



###################################################################################################################################3


# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота ""интеллектом""


# sweetNumber = 200
# maxTake = 28
# minTake = 1
#
# yourMoveFirst = False
#
# players = ["You", "Computer"]
#
# coin = random.choice(players)
#
# print(f"First move will be done by {coin}")
#
#
# if coin == "You":
#     while sweetNumber > 0:
#         yourTake = 0
#         ComputerTake = 0
#
#         if sweetNumber <= maxTake and sweetNumber > 0:
#             print("You won, Dude!!!")
#             break
#         else:
#             while yourTake < minTake or yourTake > maxTake or yourTake > sweetNumber:
#                 yourTake = int(input(f"Please take your sweets (max number is {maxTake}): "))
#                 if yourTake < minTake or yourTake > maxTake or yourTake > sweetNumber:
#                     print("Please take proper number of sweets")
#             if sweetNumber <= maxTake:
#                 print("You won, Dude!!!")
#                 break
#
#         sweetNumber -= yourTake
#         print("Total sweets left " + str(sweetNumber))
#
#         if sweetNumber <= maxTake:
#             print("Computer won! :(")
#             break
#         else:
#             ComputerTake = random.randrange(minTake, maxTake)
#         print(f"Now is computer's move and it took {ComputerTake}")
#
#         sweetNumber -= ComputerTake
#         print("Total sweets left " + str(sweetNumber))
# else:
#     while sweetNumber > 0:
#         yourTake = 0
#         ComputerTake = 0
#
#         if sweetNumber <= maxTake and sweetNumber > 0:
#             print("Computer won! :(")
#             break
#         else:
#             ComputerTake = random.randrange(minTake, maxTake)
#             print(f"Computer took {ComputerTake} sweets")
#
#         sweetNumber -= ComputerTake
#         print("Total sweets left " + str(sweetNumber))
#
#         while yourTake < minTake or yourTake > maxTake or yourTake > sweetNumber:
#             yourTake = int(input(f"Please take your sweets (max number is {maxTake}): "))
#             if yourTake < minTake or yourTake > maxTake or yourTake > sweetNumber:
#                 print("Please take proper number of sweets")
#
#         sweetNumber -= yourTake
#         print("Total sweets left " + str(sweetNumber))













#####################################################################################################################
# Создайте программу для игры в ""Крестики-нолики""

#
# class Fuild():
#     cells = [x for x in range(9)]
#     table = dict.fromkeys(cells, '.')
#     cellsForBot = []
#
#     def drawChecking(self):
#         if '.' not in self.table.values():
#             print("We have draw!!!")
#             return True
#
#
# class fuildFullFill(Fuild):
#     mySymbol = ''
#     botSymbol = ''
#
#     def __init__(self, symbol):
#         self.mySymbol = symbol
#         if self.mySymbol == 'X':
#             self.botSymbol = 'O'
#         elif self.mySymbol == 'O':
#             self.botSymbol = 'X'
#
#     def myMove(self, num):
#         Fuild.table[num] = self.mySymbol
#
#     def computerMove(self, num):
#         Fuild.table[num] = self.botSymbol
#
# class checkForWinner(Fuild):
#
#     def isComputerWinner(self):
#         if Fuild.table[0] == Fuild.table[1] == Fuild.table[2] == 'O':
#             return True
#         elif Fuild.table[3] == Fuild.table[4] == Fuild.table[5] == 'O':
#             return True
#         elif Fuild.table[6] == Fuild.table[7] == Fuild.table[8] == 'O':
#             return True
#         elif Fuild.table[0] == Fuild.table[3] == Fuild.table[6] == 'O':
#             return True
#         elif Fuild.table[1] == Fuild.table[4] == Fuild.table[7] == 'O':
#             return True
#         elif Fuild.table[2] == Fuild.table[5] == Fuild.table[8] == 'O':
#             return True
#         elif Fuild.table[2] == Fuild.table[4] == Fuild.table[6] == 'O':
#             return True
#         elif Fuild.table[0] == Fuild.table[4] == Fuild.table[8] == 'O':
#             return True
#
#     def areYouWinner(self):
#         if Fuild.table[0] == Fuild.table[1] == Fuild.table[2] == 'X':
#             return True
#         elif Fuild.table[3] == Fuild.table[4] == Fuild.table[5] == 'X':
#             return True
#         elif Fuild.table[6] == Fuild.table[7] == Fuild.table[8] == 'X':
#             return True
#         elif Fuild.table[0] == Fuild.table[3] == Fuild.table[6] == 'X':
#             return True
#         elif Fuild.table[1] == Fuild.table[4] == Fuild.table[7] == 'X':
#             return True
#         elif Fuild.table[2] == Fuild.table[5] == Fuild.table[8] == 'X':
#             return True
#         elif Fuild.table[2] == Fuild.table[4] == Fuild.table[6] == 'X':
#             return True
#         elif Fuild.table[0] == Fuild.table[4] == Fuild.table[8] == 'X':
#             return True
#
# class displayFuild(Fuild):
#
#     def display(self):
#         print("\n");
#         print("     |     |     ")
#         print("  {}  |  {}  |  {}  ".format(self.table[0], self.table[1], self.table[2]))
#         print("_____|_____|_____")
#         print("     |     |     ")
#         print("  {}  |  {}  |  {} ".format(self.table[3], self.table[4], self.table[5]))
#         print("_____|_____|_____")
#         print("     |     |     ")
#         print("  {}  |  {}  |  {}  ".format(self.table[6], self.table[7], self.table[8]))
#         print("     |     |     ")

# class WinningOpp(checkForWinner):
#
#     winMove = False
#     idx = 9
#
#     def botWinningOpp(self):
#         for i in super().cellsForBot:
#             super().table[i] = 'O'
#             if super().isComputerWinner():
#
#
#             #     super().table[i] = '.'
#             #     winMove = True
#             #     idx = i
#             #     return self.winMove, idx
#             # else:
#             #     super().table[i] = '.'
#
#     def playerWinningOpp(self):
#         for i in super().cellsForBot:
#             super().table[i] = 'X'
#             if super().areYouWinner():
#                 super().table[i] = '.'
#                 winMove = True
#                 return winMove
#             else:
#                 super().table[i] = '.'
#                 return False




# haveWinner = False
# checkingForWinner = checkForWinner()
# disp = displayFuild()
# # checkWinningOpp = WinningOpp()
#
# yourMove = False
#
# # Определим символ, которым будем играть, и передадим его в класс fuildFullFill
# playerSide = input("Please choose your tool (X or O):  ")
# turn = fuildFullFill(playerSide)
#------------------------------------------------------------------------------


#
#
# if turn.mySymbol == 'X':
#     while not haveWinner:
#         cell = 9
#         while cell < 0 or cell > 8 or Fuild.table[cell] == 'X':
#             cell = int(input("Make your move to empty cell (from 0 to 8): "))
#
#         turn.myMove(cell) # запишем ход в поле
#
#         # определяем пустые клетки
#         for key, value in Fuild.table.items():
#             if value == ".":
#                 Fuild.cellsForBot.append(key)
#
#         # bot moves
#         cell = random.choice(Fuild.cellsForBot)
#         print(f"Computer's move: {cell}")
#         turn.computerMove(cell)
#
#         disp.display()
#         Fuild.cellsForBot.clear() # нужно очистить, т.к. происходят задвоения и бот ходит в позиции, куда уже ходил
#
#         if checkingForWinner.isComputerWinner() or checkingForWinner.areYouWinner():
#             haveWinner = True
#             if checkingForWinner.isComputerWinner():
#                 print("COMPUTER WON!!!")
#             elif checkingForWinner.areYouWinner():
#                 print("YOU WON!!!")
# elif turn.mySymbol == 'O':
#     while not haveWinner:
#         cell = 9
#         # определяем пустые клетки
#         for key, value in Fuild.table.items():
#             if value == ".":
#                 Fuild.cellsForBot.append(key)
#
#         # bot moves
#         cell = random.choice(Fuild.cellsForBot)
#         print(f"Computer's move: {cell}")
#         turn.computerMove(cell)
#         disp.display()
#
#         while cell < 0 or cell > 8 or Fuild.table[cell] == 'X':
#             cell = int(input("Make your move to empty cell (from 0 to 8): "))
#
#         turn.myMove(cell) # запишем ход в поле
#
#         Fuild.cellsForBot.clear()
#
#         if checkingForWinner.isComputerWinner() or checkingForWinner.areYouWinner():
#             haveWinner = True
#             if checkingForWinner.isComputerWinner():
#                 print("COMPUTER WON!!!")
#             elif checkingForWinner.areYouWinner():
#                 print("YOU WON!!!")
