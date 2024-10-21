import tkinter as tk
from tkinter import messagebox

class Game:
    def __init__(self,root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.player_turn = "X"
        #self.board = [["" for _ in range(3)] for _ in range(3)] # create an array to track each board position
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        #create buttons to dispaly each column
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(self.root,text = "", font = ("Ariel",20), height = 2, width = 5, command = lambda r = row, c = col: self.on_click(r,c))
                self.buttons[row][col].grid(row = row ,column = col) 
            
        #create a reset button
        self.reset_game = tk.Button(self.root,text="Reset",command = self.reset)
        self.reset_game.grid(row = 3, column= 0 , columnspan=3)


    #on click function
    def on_click(self,r,c):
        if self.buttons[r][c]['text'] == "": #if the button is empty
            #self.board[r][c] = self.player_turn #update board value with current player value
            self.buttons[r][c]['text'] = self.player_turn #update button to display the value

        #check for winner or draw after each click
        if self.check_winner():
            messagebox.showinfo('Game Over',f'Player {self.player_turn} wins!')
            self.disable_buttons()
        elif self.check_draw():
            messagebox.showinfo('Game Over','Its a Draw!')
            self.disable_buttons()
        else:
            self.player_turn = "O" if self.player_turn == "X" else "X" #switch to other player

    #check winner
    def check_winner(self):
        #check row and column wise
        for i in range(3):
            if self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] != "":
                return True
            if self.buttons[0][i]['text'] == self.buttons[1][i]['text'] == self.buttons[2][i]['text'] != "":
                return True
            
        #check diagonals
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
                return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
                return True
        return False
    
    #check draw
    def check_draw(self):
        #if no empty place on button
        for row in self.buttons:
              for col in row:
                if col['text'] == "":
                    return False
        return True
    
    #disable button
    def disable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.config(state = tk.DISABLED)

    #reset button
    def reset(self):
        self.player_turn = "X"
        #self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in self.buttons:
            for button in row:
                button.config(text="",state=tk.NORMAL)

#main tkinter window
root = tk.Tk()
tictactoe = Game(root)
root.mainloop()