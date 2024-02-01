import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

        # Create buttons for the game board
        self.buttons = [[tk.Button(self.root, text=' ', font=('Helvetica', 24), width=5, height=2, command=lambda row=row, col=col: self.click(row, col)) for col in range(3)] for row in range(3)]

        # Place the buttons on the grid
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].grid(row=row, column=col)

    def click(self, row, col):
        # Check if the clicked cell is empty
        if self.board[row][col] == ' ':
            # Update the board and button text
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            # Check for a winner
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_board()
            else:
                # Switch to the next player
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ' or \
               self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ' or \
           self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False

    def check_draw(self):
        # Check if the board is full
        return all(cell != ' ' for row in self.board for cell in row)

    def reset_board(self):
        # Reset the board and button text
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=' ')

    def run(self):
        self.root.mainloop()

# Create and run the TicTacToe game
if __name__ == "__main__":
    game = TicTacToe()
    game.run()
