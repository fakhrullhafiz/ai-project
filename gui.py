import tkinter as tk
from tkinter import ttk, messagebox
import math

class TicTacToe:
    def __init__(self, user_starts_first=True, difficulty="Medium", user_color="blue", ai_color="red"):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "User" if user_starts_first else "AI"
        self.difficulty = difficulty
        self.user_color = user_color
        self.ai_color = ai_color
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_gui()
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)  # Handle close event
        if self.current_player == "AI":
            self.ai_move()  # AI starts first if selected
        self.window.mainloop()

    def create_gui(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                    self.window, text=" ", font=("Arial", 20), width=5, height=2,
                    command=lambda row=i, col=j: self.user_move(row, col)
                )
                self.buttons[i][j].grid(row=i, column=j)

    def user_move(self, row, col):
        if self.board[row][col] == " " and self.current_player == "User":
            self.board[row][col] = "X"
            self.buttons[row][col].config(text="X", fg=self.user_color)
            if self.check_winner("X"):
                messagebox.showinfo("Game Over", "You win!")
                self.disable_buttons()
            elif self.is_full():
                messagebox.showinfo("Game Over", "It's a draw!")
            else:
                self.current_player = "AI"
                self.ai_move()

    def ai_move(self):
        best_score = -math.inf
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.board[i][j] = "O"
                    score = self.minimax(0, False)
                    self.board[i][j] = " "
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        if best_move:
            row, col = best_move
            self.board[row][col] = "O"
            self.buttons[row][col].config(text="O", fg=self.ai_color)
            if self.check_winner("O"):
                messagebox.showinfo("Game Over", "AI wins!")
                self.disable_buttons()
            elif self.is_full():
                messagebox.showinfo("Game Over", "It's a draw!")
            else:
                self.current_player = "User"

    def minimax(self, depth, is_maximizing):
        if self.check_winner("X"):
            return -1
        if self.check_winner("O"):
            return 1
        if self.is_full():
            return 0

        if is_maximizing:
            best_score = -math.inf
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == " ":
                        self.board[i][j] = "O"
                        score = self.minimax(depth + 1, False)
                        self.board[i][j] = " "
                        best_score = max(best_score, score)
            return best_score
        else:
            best_score = math.inf
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == " ":
                        self.board[i][j] = "X"
                        score = self.minimax(depth + 1, True)
                        self.board[i][j] = " "
                        best_score = min(best_score, score)
            return best_score

    def check_winner(self, symbol):
        for i in range(3):
            if all(self.board[i][j] == symbol for j in range(3)):
                return True
            if all(self.board[j][i] == symbol for j in range(3)):
                return True
        if all(self.board[i][i] == symbol for i in range(3)):
            return True
        if all(self.board[i][2 - i] == symbol for i in range(3)):
            return True
        return False

    def is_full(self):
        return all(cell != " " for row in self.board for cell in row)

    def disable_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state="disabled")

    def on_close(self):
        """Safely handle the closing of the game window."""
        if self.window.winfo_exists():
            self.window.destroy()
        print("Tic Tac Toe window closed.")

def main_menu():
    def start_game():
        if menu_window.winfo_exists():
            menu_window.destroy()
        TicTacToe(
            user_starts_first=user_starts_first.get(),
            difficulty=difficulty.get(),
            user_color=user_color.get(),
            ai_color=ai_color.get(),
        )

    def on_close():
        """Safely handle the main menu close event."""
        if menu_window.winfo_exists():
            menu_window.destroy()
        print("Main menu window closed.")

    menu_window = tk.Tk()
    menu_window.title("Tic-Tac-Toe Main Menu")

    user_starts_first = tk.BooleanVar(value=True)
    difficulty = tk.StringVar(value="Medium")
    user_color = tk.StringVar(value="blue")
    ai_color = tk.StringVar(value="red")

    tk.Label(menu_window, text="Welcome to Tic-Tac-Toe", font=("Arial", 16)).pack(pady=10)
    tk.Label(menu_window, text="Do you want to start first?").pack(pady=5)
    tk.Radiobutton(menu_window, text="Yes", variable=user_starts_first, value=True).pack()
    tk.Radiobutton(menu_window, text="No", variable=user_starts_first, value=False).pack()

    tk.Label(menu_window, text="Select AI Difficulty:").pack(pady=5)
    ttk.Combobox(menu_window, textvariable=difficulty, values=["Easy", "Medium", "Hard"]).pack()

    tk.Label(menu_window, text="Choose your (X) color:").pack(pady=5)
    ttk.Combobox(menu_window, textvariable=user_color, values=["blue", "green", "purple", "yellow"]).pack()

    tk.Label(menu_window, text="Choose AI (O) color:").pack(pady=5)
    ttk.Combobox(menu_window, textvariable=ai_color, values=["red", "orange", "black", "brown"]).pack()

    tk.Button(menu_window, text="Start Game", command=start_game, bg="green", fg="white").pack(pady=20)

    menu_window.protocol("WM_DELETE_WINDOW", on_close)
    menu_window.mainloop()

main_menu()