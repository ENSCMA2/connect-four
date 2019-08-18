print "Welcome to Connect Four!"
print "The goal of this game is simply to have four of your symbols in a vertical, horizontal, or diagonal row."
print "Player 1, your symbol is an x. Player 2, your symbol is an o."
print "You will be prompted to enter a column number as your move."
print "This will fill the bottom-most blank space in your chosen column with your symbol."
print "Let's start!"
arrayBoard = [[], [], [], [], [], [], [], []]
for i in range(0,8):
	for k in range(0,8):
		arrayBoard[i].append(".")
turnNumber = 1
def toString(array):
	out = ""
	for i in array:
		out += i + " "
	return out
for i in range(0,8):
	print toString(arrayBoard[i])
def oneMovePlayer1():
	move = input("Player 1, enter your move. Just enter the column number (1-8).")
	while 1 > move or 8 < move:
		move = input("Please enter a number from 1-8.")
	topspot = 7
	while topspot >= 0:
		if arrayBoard[topspot][move-1] == ".":
			break
		else:
			topspot -= 1
	while topspot < 0:
		move = input("Player 1, enter your move. Just enter the column number (1-8).")
		while move < 1 or move > 8:
			move = input("Please enter a number from 1-8.")
		topspot = 7
		while topspot >= 0:
			if arrayBoard[topspot][move-1] == ".":
				break
			else:
				topspot -= 1
	arrayBoard[topspot][move-1] = "x"
	for i in range(0,8):
		print toString(arrayBoard[i])
def oneMovePlayer2():
		move = input("Player 2, enter your move. Just enter the column number (1-8).")
		while move < 1 or move > 8:
			move = input("Please enter a number from 1-8.")
		topspot = 7
		while topspot >= 0:
			if arrayBoard[topspot][move-1] == ".":
				break
			else:
				topspot -= 1
		while topspot < 0:
			move = input("Player 2, enter your move. Just enter the column number (1-8).")
			while move < 1 or move > 8:
				move = input("Please enter a number from 1-8.")
			topspot = 7
			while topspot >= 0:
				if arrayBoard[topspot][move-1] == ".":
					break
				else:
					topspot -= 1
		arrayBoard[topspot][move-1] = "o"
		for i in range(0,8):
			print toString(arrayBoard[i])
def winningCondition(board, symbol):
	for i in range(0,8):
		for k in range(0, 5):
			if arrayBoard[i][k] == symbol:
				if arrayBoard[i][k+1] == symbol:
					if arrayBoard[i][k+2] == symbol:
						if arrayBoard[i][k+3] == symbol:
							return True
	for i in range(0,5):
		for k in range(0, 8):
			if arrayBoard[i][k] == symbol:
				if arrayBoard[i+1][k] == symbol:
					if arrayBoard[i+2][k] == symbol:
						if arrayBoard[i+3][k] == symbol:
							return True
	for i in range(0,5):
		for k in range(0,5):
			if arrayBoard[i][7-k] == symbol:
				if arrayBoard[i+1][6-k] == symbol:
					if arrayBoard[i+2][5-k] == symbol:
						if arrayBoard[i+3][4-k] == symbol:
							return True
	for i in range(0,5):
		for k in range(0,5):
			if arrayBoard[i][k] == symbol:
				if arrayBoard[i+1][k+1] == symbol:
					if arrayBoard[i+2][k+2] == symbol:
						if arrayBoard[i+3][k+3] == symbol:
							return True
	return False
while winningCondition(arrayBoard, "x") == False and winningCondition(arrayBoard, "o") == False:
	if turnNumber %2 == 1:
		oneMovePlayer1()
		turnNumber += 1
	else:
		oneMovePlayer2()
		turnNumber += 1
if winningCondition(arrayBoard, "x") == True:
	print "Player 1 won!"
else:
	print "Player 2 won!"
def askToPlayAgain():
	response = raw_input("Do you want to play again? y or n")
	while response != "y" and response != "n" and response != "Y" and response != "N":
		response = raw_input("Do you want to play again? y or n")
	if response == "y":
		return True
	return False
while askToPlayAgain():
	arrayBoard = [[], [], [], [], [], [], [], []]
	for i in range(0,8):
		for k in range(0,8):
			arrayBoard[i].append(".")
	turnNumber = 1
	for i in range(0,8):
		print toString(arrayBoard[i])
	while winningCondition(arrayBoard, "x") == False and winningCondition(arrayBoard, "o") == False:
		if turnNumber %2 == 1:
			oneMovePlayer1()
			turnNumber += 1
		else:
			oneMovePlayer2()
			turnNumber += 1
	if winningCondition(arrayBoard, "x") == True:
		print "Player 1 won!"
	else:
		print "Player 2 won!"
print "Thanks for playing! Bye!"