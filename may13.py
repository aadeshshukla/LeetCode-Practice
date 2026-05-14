# python code for a simple game 
# chess game
# chess game is a two player game
# the game is played on a 8x8 board
# each player has 16 pieces
# the pieces are: king, queen, rook, bishop, knight, pawn
class ChessGame:
    def __init__(self):
        self.board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        self.current_player = 'w'
    def display_board(self):
        for row in self.board:
            print(' '.join(row))
    def make_move(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
        piece = self.board[start_row][start_col]
        if piece == ' ':
            print("No piece at the starting position.")
            return False
        if (self.current_player == 'w' and piece.islower()) or (self.current_player == 'b' and piece.isupper()):
            print("It's not your turn.")
            return False
        # For simplicity, we won't implement actual move validation here
        self.board[end_row][end_col] = piece
        self.board[start_row][start_col] = ' '
        self.current_player = 'b' if self.current_player == 'w' else 'w'
        return True
game = ChessGame()
game.display_board()
game.make_move((1, 1), (3, 1))
game.display_board()
game.make_move((6, 6), (4, 6))
game.display_board()    
# it should be looped until the game is over, but for simplicity we will just make a few moves here.    
# lets implement fully playable chess game.
class ChessGame:
    def __init__(self):
        self.board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        self.current_player = 'w'
    def display_board(self):
        for row in self.board:
            print(' '.join(row))
    def make_move(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
        piece = self.board[start_row][start_col]
        if piece == '':
            print("No piece at the starting position.")
            return False
        if (self.current_player == "w" and piece.islower()) or (self.current_player == "b" and piece.isupper()):
            print("It's not your turn.")
            return False
        # For simplicity, we won't implement actual move validation here
        self.board[end_row][end_col] = piece
        self.board[start_row][start_col] = ''
        self.current_player = "b" if self.current_player == "w" else "w"
        return True
game = ChessGame()
while True:
    game.display_board()
    # Add move input and validation here
    try:
        start_input = input("Enter the starting position (e.g., 'e2'): ")
        end_input = input("Enter the ending position (e.g., 'e4'): ")
        
        # Convert input to board coordinates
        start_col = ord(start_input[0]) - ord('a')
        start_row = 8 - int(start_input[1])
        end_col = ord(end_input[0]) - ord('a')
        end_row = 8 - int(end_input[1])

        if not game.make_move((start_row, start_col), (end_row, end_col)):
            print("Invalid move. Try again.")
    except (ValueError, IndexError):
        print("Invalid input. Please enter positions in the format 'e2'.")