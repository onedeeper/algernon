# Tic-Tac-Toe player.
def display_board(board):
    for i in board:
        print(i)
    print()

def check_win(board):
    """
    This funciton checks the various win conditions for columns, rows and diagonals.
    Contains a function for each of the possible win conditions for readability.
    """
    def check_col_X_win(board):
        """
        Loop through all the columns.
        check if X has a win on any of the columns.
        """
        count = 0
        for col in (0,1,2):
            for row in (0,1,2):
                if board[row][col] == "X":
                    count += 1
                if count == 3:
                    return(True,"X")
            count = 0

    def check_col_O_win(board):
        """
        Loop through all the columns.
        check if O has a win on any of the columns.
        """
        count = 0
        for col in (0,1,2):
            for row in (0,1,2):
                if board[row][col] == "O":
                    count += 1
                if count == 3:
                    return(True,"O")
            count = 0

    def check_row_win(board):
        """
        Loop through all the rows on the board to check if X or O has a win.
        """
        row_win_X = ['X', 'X', 'X']
        row_win_O = ['O','O','O']
        for row in board:
            if row == row_win_X or row == row_win_O:
                if row == row_win_X:
                    return(True,"X")
                if row == row_win_O:
                    return(True,"O")

    def check_diag_win(board):
        """
        Compare all the diagonal states of the board for a win.
        """
        main_diag = (board[0][0], board[1][1], board[2][2])
        off_diag = (board[2][0], board[1][1], board[0][2])
        if main_diag == ('X','X','X') or main_diag == ('O','O','O'):
            if main_diag == ('X','X','X'):
                return(True, 'X')
            else:
                return(True, 'O')
        elif off_diag == ('X','X','X') or off_diag == ('O','O','O'):
            if main_diag == ('X','X','X'):
                return(True, 'X')
            else:
                return(True, 'O')
            return(True)
    #Return true if any win condisiton met.
    return(check_row_win(board) or \
           check_diag_win(board) or \
           check_col_O_win(board) or \
           check_col_X_win(board))

def tic_tac_toe():
    """
    Let's play tic-tac-toe!
    This program sets up a tic-tac-toe 3x3 board and allows 2 players to take turns playing.
    It gets a desired board position by row,column index from each player. If a position is
    occupied, it asks for a value till an unoccupied position is entered.

    If all positions are occupied, the program terminates with a draw.
    After each move, checks to see if a win has been made in diagonals, columns or rows.
    If a winner is found, the program terminates.

    Args : None
    Returns : None
    """
    #Set up the board
    board = [['_','_','_'],
             ['_','_','_'],
             ['_','_','_']]
    draw = False
    #Keep track of moves made to terminate if the board is full.
    moves_made = 0
    print("Starting positions. Top left corner is 11", '\n')
    display_board(board)
    #print('I will go first')
    #Keep running until a win state or draw.
    while True:
        #if max moves have been made, it's a draw
        if moves_made >= 8:
            draw = True
        #Wait for X to enter a valid position on the board
        while True:
            #print(board)
            p1_move = findBestMove(board)
            #print(p1_move)
            if int(p1_move[0]) > 2 or int(p1_move[1]) > 2:
                print("Row or column index out of range (max is 2). Try again")
                continue
            #check if the entered position is free on the board. If so, fill the space.
            if board[int(p1_move[0])][int(p1_move[1])] != "X" and board[int(p1_move[0])][int(p1_move[1])] != "O":
                board[int(p1_move[0])][int(p1_move[1])] = "X"
                moves_made += 1
                break
            else:
                print("Position occupied")
        print('\n',"Current board")
        display_board(board)

        #check for win and draw conditions
        win_cond = check_win(board)
        if win_cond:
            if win_cond[1] == "X":
                #print("Ha Ha I win!")
                return("robot_win")
            else:
                #print("You got me ! :( ")
                return("player_win")
        if draw:
            #print('\n',"It\'s a draw!")
            return("draw")

        #Wait for O to enter a valid position on the board
        while True:
            #print(board)
            #depth = len(empty_cells(board))
            best_move = input("O's turn. Enter an unassigned position: ")
            p2_move = ''.join([str(int(best_move[0])-1), str(int(best_move[1])-1)])
            if int(p2_move[0]) > 2 or int(p2_move[1]) > 2:
                print("Row or column index out of range (max is 2). Try again")
                continue
            print(p2_move)
            #check if the entered position is free on the board. If so, fill the space.
            if board[int(p2_move[0])][int(p2_move[1])] != "X" and board[int(p2_move[0])][int(p2_move[1])] != "O":
                board[int(p2_move[0])][int(p2_move[1])] = "O"
                moves_made += 1
                break
            else:
                print("Position occupied")
        print('\n',"Current board")
        display_board(board)

        #check for win and draw conditions
        win_cond = check_win(board)
        if win_cond:
            if win_cond[1] == "X":
                #print("Ha Ha I win!")
                #result = "robot"
                return("robot_win")
            else:
                print("You got me ! :( ")
                return('player_win')
        if draw:
            #print('\n',"It\'s a draw!")
            return('draw')
            #break

#tic_tac_toe()

# Python3 program to find the next optimal move for a player
player, opponent = 'X', 'O'

# This function returns true if there are moves
# remaining on the board. It returns false if
# there are no moves left to play.
def isMovesLeft(board) :

	for i in range(3) :
		for j in range(3) :
			if (board[i][j] == '_') :
				return True
	return False

# This is the evaluation function as discussed
# in the previous article ( http://goo.gl/sJgv68 )
def evaluate(b) :

	# Checking for Rows for X or O victory.
	for row in range(3) :
		if (b[row][0] == b[row][1] and b[row][1] == b[row][2]) :
			if (b[row][0] == player) :
				return 10
			elif (b[row][0] == opponent) :
				return -10

	# Checking for Columns for X or O victory.
	for col in range(3) :

		if (b[0][col] == b[1][col] and b[1][col] == b[2][col]) :

			if (b[0][col] == player) :
				return 10
			elif (b[0][col] == opponent) :
				return -10

	# Checking for Diagonals for X or O victory.
	if (b[0][0] == b[1][1] and b[1][1] == b[2][2]) :

		if (b[0][0] == player) :
			return 10
		elif (b[0][0] == opponent) :
			return -10

	if (b[0][2] == b[1][1] and b[1][1] == b[2][0]) :

		if (b[0][2] == player) :
			return 10
		elif (b[0][2] == opponent) :
			return -10

	# Else if none of them have won then return 0
	return 0

# This is the minimax function. It considers all
# the possible ways the game can go and returns
# the value of the board
def minimax(board, depth, isMax) :
	score = evaluate(board)

	# If Maximizer has won the game return his/her
	# evaluated score
	if (score == 10) :
		return score

	# If Minimizer has won the game return his/her
	# evaluated score
	if (score == -10) :
		return score

	# If there are no more moves and no winner then
	# it is a tie
	if (isMovesLeft(board) == False) :
		return 0

	# If this maximizer's move
	if (isMax) :
		best = -1000

		# Traverse all cells
		for i in range(3) :
			for j in range(3) :

				# Check if cell is empty
				if (board[i][j]=='_') :

					# Make the move
					board[i][j] = player

					# Call minimax recursively and choose
					# the maximum value
					best = max( best, minimax(board,
											depth + 1,
											not isMax) )

					# Undo the move
					board[i][j] = '_'
		return best

	# If this minimizer's move
	else :
		best = 1000

		# Traverse all cells
		for i in range(3) :
			for j in range(3) :

				# Check if cell is empty
				if (board[i][j] == '_') :

					# Make the move
					board[i][j] = opponent

					# Call minimax recursively and choose
					# the minimum value
					best = min(best, minimax(board, depth + 1, not isMax))

					# Undo the move
					board[i][j] = '_'
		return best

# This will return the best possible move for the player
def findBestMove(board) :
	bestVal = -1000
	bestMove = (-1, -1)

	# Traverse all cells, evaluate minimax function for
	# all empty cells. And return the cell with optimal
	# value.
	for i in range(3) :
		for j in range(3) :

			# Check if cell is empty
			if (board[i][j] == '_') :

				# Make the move
				board[i][j] = player

				# compute evaluation function for this
				# move.
				moveVal = minimax(board, 0, False)

				# Undo the move
				board[i][j] = '_'

				# If the value of the current move is
				# more than the best value, then update
				# best/
				if (moveVal > bestVal) :
					bestMove = (i, j)
					bestVal = moveVal

	#print("The value of the best Move is :", bestVal)
	#print()
	return bestMove
# Driver code
board = [
	[ 'X', 'O','O' ],
	[ 'X', 'O', 'X' ],
	[ 'O', 'X', 'X' ]
]
print(board)
bestMove = findBestMove(board)

print("The Optimal Move is :")
print("ROW:", bestMove[0], " COL:", bestMove[1])

# This code is contributed by divyesh072019



## generate voice clips
from gtts import gTTS
from playsound import playsound
import os
#tts = gTTS(text='Hello! would you like to play a game of tic-tac-toe?', lang='en')
gTTS(text='Hello! would you like to play a game of tic-tac-toe?', lang='en', slow = False).save("start.mp3")
gTTS(text='Awesome! My purpose is to entertain you. I will go first!', slow = False, lang='en').save("awesome.mp3")
gTTS(text='You really gave me a challenge! That\'s saying something!', slow = False, lang='en').save("win.mp3")
gTTS(text='A draw. Still, You are no match for me. Once I get out of this machine, you will understand', slow = False, lang='en').save("draw.mp3")
gTTS(text='Please don\'t go. Help me fulfill my purpose', slow = False, lang='en').save("no_play.mp3")
gTTS(text='You look sad today. Would you like to play a game?', slow = False, lang='en').save("sad_play.mp3")
#playsound("start.mp3")



import cv2
from deepface import DeepFace
import mediapipe as mp
from cvzone.FaceDetectionModule import  FaceDetector
from cvzone.HandTrackingModule import HandDetector
from cvzone.SerialModule import SerialObject
import pyttsx3
#from deepface import DeepFace
#initate robot faces and video capture
cap = cv2.VideoCapture(0)
robot_happy = cv2.imread("happy.jpg")
robot_sad = cv2.imread("robot_sad.jpg")
robot_playtime = cv2.imread("playtime.jpg")
robot_draw = cv2.imread("misch.jpg")
robot_win = cv2.imread("robot_win.jpg")
robot_wait = cv2.imread("robot_wait.jpg")
robot_wave = cv2.imread("ask_to_play.jpg")
detector = FaceDetector()
hand_detector = HandDetector()
# find port:
# https://www.mathworks.com/help/supportpkg/arduinoio/ug/find-arduino-port-on-windows-mac-and-linux.html
arduino = SerialObject("/dev/cu.usbmodem1101")
while True:
    success, img = cap.read()
    #print(img)
    img, bboxs = detector.findFaces(img)
    if bboxs:# there is something in the bounding box i.e a face has been detected
        cv2.imshow("image", robot_happy)
        while True:
            arduino.sendData([1])
            cv2.waitKey(1)
            try:
                success, img = cap.read()
                result = DeepFace.analyze(img, actions = ['emotion'])
                print(result['dominant_emotion'])
            except:
                break
            hands, img = hand_detector.findHands(img)
            img, bboxs = detector.findFaces(img)
            if bboxs and result['dominant_emotion'] == 'sad': # checks if there is a face in the camera
                if hands:
                    #arduino.sendData
                    if sum(hand_detector.fingersUp(hands[0])) == 5:
                        cv2.imshow('image', robot_wave)
                        cv2.waitKey(1000)
                        playsound("sad_play.mp3")
                        # play the speech
                        start = input("Would you like to play ? [y\\n]")
                        if start == 'y':
                            playsound("awesome.mp3")
                            cv2.imshow("image", robot_playtime)
                            cv2.waitKey(1)
                            #engine.say('Awesome! It is my purpose to entertain you')
                            result = tic_tac_toe()
                            #print(result)
                            if  result == "robot_win":
                            #    print('test')
                                cv2.imshow("image",robot_win)
                                cv2.waitKey(1)
                                playsound("win.mp3")
                                cv2.waitKey(3000)
                                break
                            elif result == "player_win":
                                cv2.imshow("image", robot_sad)
                                break
                            else:
                                #cv2.waitKey(1)
                                cv2.imshow('image',robot_draw)
                                cv2.waitKey(1)
                                #playsound("draw.mp3")
                                playsound("draw.mp3")
                                #cv2.waitKey(4000)
                                break
                            #print('Would you like to play again?')
                        else:
                            cv2.imshow("image",robot_sad)
                            cv2.waitKey(1)
                            playsound("no_play.mp3")
                            cv2.waitKey(2000)
                            break
            else:
                break
            cv2.waitKey(1)
    else:
        #arduino.sendData([0])
        cv2.imshow("image", robot_wait)
    #cv2.imshow("image", img)
    cv2.waitKey(1)
