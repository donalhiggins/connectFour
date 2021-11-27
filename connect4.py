import pygame

def drawBoard(screen, board):
    for i in range(6):
        for j in range(7):
            if board[i][j] == 'r':
                pygame.draw.circle(screen, (153, 0, 0),
                                   (70 + j * 105, 70 + i * 105), 45)
            elif board[i][j] == 'y':
                pygame.draw.circle(screen, (255, 213, 0),
                                   (70 + j * 105, 70 + i * 105), 45)
            else:
                pygame.draw.circle(screen, (255, 255, 255),
                                   (70 + j * 105, 70 + i * 105), 45)

# Makes the move and checks to see if move is valid
def move(board, color, move):
    row = move[1]
    col = move[0]
    valid = True
    if row < 5:
        for i in range(row + 1, 6):
            if board[i][col] == '-':
                valid = False
                break
    if board[row][col] == '-' and valid:
        board[row][col] = color
    if not valid:
        return False
    return board

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
                            tBoard = move(gameBoard, 'y', coords)
                            if type(tBoard) == bool:
                                print('Invalid move')
                            else:
                                gameBoard = tBoard
                                yellowTurn = False
                        else:
                            tBoard = move(gameBoard, 'r', coords)
                            if type(tBoard) == bool:
                                print('Invalid move')
                            else:
                                gameBoard = tBoard
                                yellowTurn = True
        if didWin(gameBoard) != False:
            print(didWin(gameBoard))
            gameWon = True

        if didTie(gameBoard):
            print('Tie')
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
