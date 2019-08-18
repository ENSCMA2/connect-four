import random
import sys
import os
import Tkinter
import tkMessageBox
class Tile(Tkinter.Frame):
	__height = 17
	__width = 30
	__bg = "cyan"
	__actualFrame = Tkinter.Frame(height = 17, width = 30, bg = "cyan")
	__position = [0, 0]
	def __init__(self, backgroundColor, position):
		self.__bg = backgroundColor
		self.__position = position
		self.__actualFrame = Tkinter.Frame(height = 17, width = 30, bg = self.__bg)
		self.__actualFrame.grid(column = self.__position[0], row = self.__position[1])
	def getActualFrame(self):
		return self.__actualFrame
	def getHeight(self):
		return self.__height
	def getWidth(self):
		return self.__width
	def getBG(self):
		return self.__bg
	def setActualFrame(self, frame):
		self.__actualFrame = frame
	def setHeight(self, height):
		self.__height = height
	def setWidth(self, width):
		self.__width = width
	def setBG(self, bg):
		self.__bg = bg
	def getPosition(self):
		return self.__position
	def setPosition(self, position):
		self.__position = position
class Board(Tkinter.Tk):
	__top = Tkinter.Tk()
	__top.__oneButton = Tkinter.Button(text = "1")
	__top.__oneButton.grid(column=0, row=0)
	__top.__twoButton = Tkinter.Button(text = "2")
	__top.__twoButton.grid(column = 1, row = 0)
	__top.__threeButton = Tkinter.Button(text = "3")
	__top.__threeButton.grid(column = 2, row = 0)
	__top.__fourButton = Tkinter.Button(text = "4")
	__top.__fourButton.grid(column = 3, row = 0)
	__top.__fiveButton = Tkinter.Button(text = "5")
	__top.__fiveButton.grid(column = 4, row = 0)
	__top.__sixButton = Tkinter.Button(text = "6")
	__top.__sixButton.grid(column = 5, row = 0)
	__top.__sevenButton = Tkinter.Button(text = "7")
	__top.__sevenButton.grid(column = 6, row = 0)
	__top.__eightButton = Tkinter.Button(text = "8")
	__top.__eightButton.grid(column = 7, row = 0)
	__arrayOfTiles = []
	def __init__(self):
		self.__top = Tkinter.Tk()
		self.__top.__oneButton = Tkinter.Button(text = "1")
		self.__top.__oneButton.grid(column=0, row=0)
		self.__top.__twoButton = Tkinter.Button(text = "2")
		self.__top.__twoButton.grid(column = 1, row = 0)
		self.__top.__threeButton = Tkinter.Button(text = "3")
		self.__top.__threeButton.grid(column = 2, row = 0)
		self.__top.__fourButton = Tkinter.Button(text = "4")
		self.__top.__fourButton.grid(column = 3, row = 0)
		self.__top.__fiveButton = Tkinter.Button(text = "5")
		self.__top.__fiveButton.grid(column = 4, row = 0)
		self.__top.__sixButton = Tkinter.Button(text = "6")
		self.__top.__sixButton.grid(column = 5, row = 0)
		self.__top.__sevenButton = Tkinter.Button(text = "7")
		self.__top.__sevenButton.grid(column = 6, row = 0)
		self.__top.__eightButton = Tkinter.Button(text = "8")
		self.__top.__eightButton.grid(column = 7, row = 0)
		self.__arrayOfTiles = [[], [], [], [], [], [], [], []]
		for i in range(0, 8):
			for k in range(0, 8):
				if k % 2 == 0:
					self.__arrayOfTiles[i].append(Tile("cyan", [i, k+1]))
				else:
					self.__arrayOfTiles[i].append(Tile("blue", [i, k+1]))
	def getTop(self):
		return self.__top
	def getOneButton(self):
		return self.__top.__oneButton
	def getTwoButton(self):
		return self.__top.__twoButton
	def getThreeButton(self):
		return self.__top.__threeButton
	def getFourButton(self):
		return self.__top.__fourButton
	def getFiveButton(self):
		return self.__top.__fiveButton
	def getSixButton(self):
		return self.__top.__sixButton
	def getSevenButton(self):
		return self.__top.__sevenButton
	def getEightButton(self):
		return self.__top.__eightButton
	def getArrayOfTiles(self):
		return self.__arrayOfTiles
	def setOneButton(self, button):
		self.__oneButton = button
	def setTwoButton(self, button):
		self.__twoButton = button
	def setThreeButton(self, button):
		self.__threeButton = button
	def setFourButton(self, button):
		self.__fourButton = button
	def setFiveButton(self, button):
		self.__fiveButton = button
	def setSixButton(self, button):
		self.__sixButton = button
	def setSevenButton(self, button):
		self.__sevenButton = button
	def setEightButton(self, button):
		self.__eightButton = button
class ConnectFourGame():
	__gameboard = Board()
	__turnNumber = 1
	def getGameBoard(self):
		return self.__gameboard
	def oneMove(self, column):
		marker = 8
		if self.__turnNumber % 2 == 1:
			while marker >= 1:
				if self.__gameboard.getArrayOfTiles()[column][marker-1].getBG() == "blue":
					self.__gameboard.getArrayOfTiles()[column][marker-1] = Tile("yellow", [column, marker])
					break
				elif self.__gameboard.getArrayOfTiles()[column][marker-1].getBG() == "cyan":
					self.__gameboard.getArrayOfTiles()[column][marker-1] = Tile("yellow", [column, marker])
					break
				else:
					marker -=1
		else:
			while marker >= 0:
				if self.__gameboard.getArrayOfTiles()[column][marker-1].getBG() == "blue" or self.__gameboard.getArrayOfTiles()[column][marker-1].getBG() == "cyan":
					self.__gameboard.getArrayOfTiles()[column][marker-1] = Tile("red", [column, marker])
					break
				else:
					marker -=1
		self.__turnNumber += 1
	def __init__(self):
		self.__gameboard = Board()
		self.__turnNumber = 1
		self.__gameboard.setOneButton(Tkinter.Button(text = "1", command = lambda:self.oneMove(0).pack()))
		self.__gameboard.getOneButton().grid(column=0, row=0)
		self.__gameboard.setTwoButton(Tkinter.Button(text = "2", command = lambda: self.oneMove(1).pack()))
		self.__gameboard.getTwoButton().grid(column=1, row=0)
		self.__gameboard.setThreeButton(Tkinter.Button(text = "3", command = lambda: self.oneMove(2).pack()))
		self.__gameboard.getThreeButton().grid(column=2, row=0)
		self.__gameboard.setFourButton(Tkinter.Button(text = "4", command = lambda: self.oneMove(3).pack()))
		self.__gameboard.getFourButton().grid(column=3, row=0)
		self.__gameboard.setFiveButton(Tkinter.Button(text = "5", command = lambda: self.oneMove(4).pack()))
		self.__gameboard.getFiveButton().grid(column=4, row=0)
		self.__gameboard.setSixButton(Tkinter.Button(text = "6", command = lambda: self.oneMove(5).pack()))
		self.__gameboard.getSixButton().grid(column=5, row=0)
		self.__gameboard.setSevenButton(Tkinter.Button(text = "7", command = lambda: self.oneMove(6).pack()))
		self.__gameboard.getSevenButton().grid(column=6, row=0)
		self.__gameboard.setEightButton(Tkinter.Button(text = "8", command = lambda: self.oneMove(7).pack()))
		self.__gameboard.getEightButton().grid(column=7, row=0)
	def winningCondition(self, color):
		for i in range(0,8):
			for k in range(0, 4):
				if self.__gameboard.getArrayOfTiles()[i][k].getBG() == color:
					if self.__gameboard.getArrayOfTiles()[i][k+1].getBG() == color:
						if self.__gameboard.getArrayOfTiles()[i][k+2].getBG() == color:
							if self.__gameboard.getArrayOfTiles()[i][k+3].getBG() == color:
								return True
		for i in range(0,4):
			for k in range(0, 8):
				if self.__gameboard.getArrayOfTiles()[i][k].getBG() == color:
					if self.__gameboard.getArrayOfTiles()[i+1][k].getBG() == color:
						if self.__gameboard.getArrayOfTiles()[i+2][k].getBG() == color:
							if self.__gameboard.getArrayOfTiles()[i+3][k].getBG() == color:
								return True
		for i in range(0,5):
			for k in range(0,5):
				if self.__gameboard.getArrayOfTiles()[i][7-k].getBG() == color:
					if self.__gameboard.getArrayOfTiles()[i+1][6-k].getBG() == color:
						if self.__gameboard.getArrayOfTiles()[i+2][5-k].getBG() == color:
							if self.__gameboard.getArrayOfTiles()[i+3][4-k].getBG() == color:
								return True
		for i in range(0,5):
			for k in range(0,5):
				if self.__gameboard.getArrayOfTiles()[i][k].getBG() == color:
					if self.__gameboard.getArrayOfTiles()[i+1][k+1].getBG() == color:
						if self.__gameboard.getArrayOfTiles()[i+2][k+2].getBG() == color:
							if self.__gameboard.getArrayOfTiles()[i+3][k+3].getBG() == color:
								return True
		return False
	def oneGame(self):
		self.__gameboard.getTop().mainloop()
		if self.winningCondition("red") == True:
			tkMessageBox.showinfo("Player 2 won!")
		if self.winningCondition("yellow") == True:
			tkMessageBox.showinfo("Player 1 won!")
connectFour = ConnectFourGame()
connectFour.oneGame()