import pygame
import sys
from engine import check_winner, minimax

# Inisialisasi Pygame
pygame.init()

# Ukuran Jendela & Warna
WIDTH, HEIGHT = 400, 400
LINE_WIDTH = 10
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

CIRCLE_RADIUS = 45
CIRCLE_WIDTH = 12
CROSS_WIDTH = 20
SPACE = 40

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE AI - GUI')

# Papan (Data)
board = [" " for _ in range(9)]
game_over = False
player_turn = True 

def draw_lines():
    screen.fill(BG_COLOR)
    # Horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, 133), (400, 133), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 266), (400, 266), LINE_WIDTH)
    # Vertikal
    pygame.draw.line(screen, LINE_COLOR, (133, 0), (133, 400), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (266, 0), (266, 400), LINE_WIDTH)

def draw_figures():
    for i in range(9):
        row = i // 3
        col = i % 3
        if board[i] == 'O':
            pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * 133 + 133 / 2), int(row * 133 + 133 / 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
        elif board[i] == 'X':
            pygame.draw.line(screen, CROSS_COLOR, (col * 133 + SPACE, row * 133 + 133 - SPACE), (col * 133 + 133 - SPACE, row * 133 + SPACE), CROSS_WIDTH)
            pygame.draw.line(screen, CROSS_COLOR, (col * 133 + SPACE, row * 133 + SPACE), (col * 133 + 133 - SPACE, row * 133 + 133 - SPACE), CROSS_WIDTH)

def reset_game():
    global board, game_over, player_turn
    board = [" " for _ in range(9)]
    game_over = False
    player_turn = True
    draw_lines()

draw_lines()

# Main Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over and player_turn:
            mouseX, mouseY = event.pos
            clicked_row, clicked_col = int(mouseY // 133), int(mouseX // 133)
            index = clicked_row * 3 + clicked_col

            if board[index] == " ":
                board[index] = "X"
                draw_figures()
                pygame.display.update()
                
                if check_winner(board): 
                    game_over = True
                else:
                    player_turn = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()

    # Giliran AI
    if not player_turn and not game_over:
        pygame.time.wait(400)
        best_score = -float('inf')
        best_move = None
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, 0, False)
                board[i] = " "
                if score > best_score:
                    best_score = score
                    best_move = i
        
        if best_move is not None:
            board[best_move] = "O"
            draw_figures()
            pygame.display.update()
            
            if check_winner(board): 
                game_over = True
            else:
                player_turn = True

    # Jika Game Selesai: Tunggu 2 detik lalu tutup otomatis
    if game_over:
        print(f"Hasil Akhir: {check_winner(board)}")
        pygame.time.wait(2000) 
        pygame.quit()
        sys.exit()

    pygame.display.update()