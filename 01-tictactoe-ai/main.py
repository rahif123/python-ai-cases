from engine import check_winner, minimax

# Inisialisasi papan kosong
board = [" " for _ in range(9)]

def print_board():
    print("\n")
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6: print("-----------")
    print("\n")

print("--- TIC TAC TOE AI (UNBEATABLE) ---")
print("Gunakan angka 0-8 untuk memilih posisi")
print_board()

while True:
    # Giliran Pemain (X)
    try:
        move = int(input("Pilih posisi (0-8): "))
        if board[move] != " ":
            print("Posisi sudah terisi, cari yang lain!")
            continue
    except (ValueError, IndexError):
        print("Input salah! Masukkan angka 0-8.")
        continue
        
    board[move] = "X"
    if check_winner(board): break

    # Giliran AI (O)
    print("AI sedang berpikir...")
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
    
    print_board()
    if check_winner(board): break

# Hasil Akhir
winner = check_winner(board)
print_board()
if winner == "Tie":
    print("Hasilnya: SERI! (Minimax emang jago)")
else:
    print(f"PEMENANGNYA ADALAH: {winner}")