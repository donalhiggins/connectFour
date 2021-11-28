import pygame
import time

def drawBoard(screen, board):
    red = pygame.image.load('img/red.png')
    red = pygame.transform.scale(red, (90, 90))
    yellow = pygame.image.load('img/yellow.png')
    yellow = pygame.transform.scale(yellow, (90, 90))
    screen.fill((11, 0, 158))
    for i in range(6):
        for j in range(7):
            if board[i][j] == 'r':
                screen.blit(red, (25 + j * 105, 25 + i * 105))

            elif board[i][j] == 'y':
                screen.blit(yellow, (25 + j * 105, 25 + i * 105))
            else:
                pygame.draw.circle(screen, (255, 255, 255),
                                   (70 + j * 105, 70 + i * 105), 45)

def findWaitTime(coords):
    return ((70 + coords[1] * 105) / 5) * 0.0004

# Makes the move and checks to see if move is valid
def move(board, color, move):
    row = move[1]
    col = move[0]
    newRow = row
    valid = True
    if board[row][col] == '-':
        for i in range(row, 6):
            if board[i][col] == '-':
                newRow += 1
            else:
                break
    else:
        return False

    return (newRow - 1, col)

def findCoords(board, move):
    row = move[1]
    col = move[0]
    newRow = row
    if board[row][col] == '-':
        for i in range(row, 6):
            if board[i][col] == '-':
                newRow += 1
            else:
                break
    return (col, newRow - 1)

def dropAnimation(screen, move, color, board):
    row = move[1]
    col = move[0]
    speed = 5
    boardImg = pygame.image.load('img/board.png')
    red = pygame.image.load('img/red.png')
    yellow = pygame.image.load('img/yellow.png')
    x = 25 + col * 105
    final_y = 30 + row * 105
    y = 0
    img = red if color == 'r' else yellow
    color = (153, 0, 0) if color == 'r' else (255, 213, 0)
    
    img = pygame.transform.scale(img, (90, 90))

    while y < final_y:
        screen.blit(img, (x, y))
        screen.blit(boardImg, (0, 0))
        y += speed
        
        pygame.display.update()
        drawBoard(screen, board)
        pygame.time.delay(4)
    

# Checks for winner
def didWin(board):
    for i in range(6):
        for j in range(7):
            if board[i][j] == 'r':
                if j < 4:
                    if board[i][j + 1] == board[i][j + 2] == board[i][j + 3] == 'r':
                        return 'r'
                if i < 3:
                    if board[i + 1][j] == board[i + 2][j] == board[i + 3][j] == 'r':
                        return 'r'
                if i < 3 and j < 4:
                    if board[i + 1][j + 1] == board[i + 2][j + 2] == board[i + 3][j + 3] == 'r':
                        return 'r'
                if i < 3 and j > 2:
                    if board[i + 1][j - 1] == board[i + 2][j - 2] == board[i + 3][j - 3] == 'r':
                        return 'r'
            elif board[i][j] == 'y':
                if j < 4:
                    if board[i][j + 1] == board[i][j + 2] == board[i][j + 3] == 'y':
                        return 'y'
                if i < 3:
                    if board[i + 1][j] == board[i + 2][j] == board[i + 3][j] == 'y':
                        return 'y'
                if i < 3 and j < 4:
                    if board[i + 1][j + 1] == board[i + 2][j + 2] == board[i + 3][j + 3] == 'y':
                        return 'y'
                if i < 3 and j > 2:
                    if board[i + 1][j - 1] == board[i + 2][j - 2] == board[i + 3][j - 3] == 'y':
                        return 'y'
    return False

# Displays winner
def displayWinner(screen, winner):
    screen.fill((255, 255, 255))
    if winner == 'r':
        font = pygame.font.SysFont('Arial', 48)
        img = font.render('Red wins!', True, (0, 0, 0))
        screen.blit(img, (290, 40))
    elif winner == 'y':
        font = pygame.font.SysFont('Arial', 48)
        img = font.render('Yellow wins!', True, (0, 0, 0))
        screen.blit(img, (290, 40))
    else:
        font = pygame.font.SysFont('Arial', 48)
        img = font.render('Tie!', True, (0, 0, 0))
        screen.blit(img, (290, 40))

def didTie(board):
    for i in range(6):
        for j in range(7):
            if board[i][j] == '-':
                return False
    return True

# Initalize pygame
pygame.init()

# Set up window
screen = pygame.display.set_mode((780, 665))
pygame.display.set_caption('Connect 4')
icon = pygame.image.load('img/icon.png')
pygame.display.set_icon(icon)

# Create game board
gameBoard = [['-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-']]

# Set up running variables
running = True
yellowTurn = True
gameWon = False

while running:
    if not gameWon:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                coords = (pos[0] // 105, pos[1] // 105)

                if coords[0] < 7 and coords[1] < 6:
                    if gameBoard[coords[1]][coords[0]] == '-':
                        if yellowTurn:
                            moveCoords = move(gameBoard, 'y', coords)
                            coords = findCoords(gameBoard, coords)
                            dropAnimation(screen, coords, 'y', gameBoard)
                            time.sleep(findWaitTime(coords))
                            gameBoard[moveCoords[0]][moveCoords[1]] = 'y'
                            yellowTurn = False
                        else:
                            moveCoords = move(gameBoard, 'r', coords)
                            coords = findCoords(gameBoard, coords)
                            dropAnimation(screen, coords, 'r', gameBoard)
                            time.sleep(findWaitTime(coords))
                            gameBoard[moveCoords[0]][moveCoords[1]] = 'r'
                            yellowTurn = True
        if didWin(gameBoard) != False:
            gameWon = True

        if didTie(gameBoard):
            gameWon = True


        screen.fill((11, 0, 158))
        drawBoard(screen, gameBoard)
        pygame.display.flip()
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        displayWinner(screen, didWin(gameBoard))
        pygame.display.flip()

pygame.quit()
