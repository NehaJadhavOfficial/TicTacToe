from tkinter import Frame, Tk, Label, E, W, Button, END, Text, FLAT, messagebox, RIDGE
import pandas as pd


class GenerateGui(Frame, object):
    """
    For Creating GUI.
    """

    def __init__(self, master):
        """
        Initializing Variables for Creating GUI
        :rtype: object
        :param master:
        """
        super(GenerateGui, self).__init__(master)
        self.matrix = pd.DataFrame([[""] * 3] * 3)
        self.result = False
        self.user = "O"
        self.generate_buttons()

    def generate_buttons(self, ):
        for row, rows in self.matrix.iterrows():
            for column, value in rows.items():
                action = lambda x=row, y=column: self.update_data(x, y)
                Button(self, text=" ", command=action, width=10, height=3, relief=RIDGE).grid(row=row, column=column)

    def update_data(self, row, column):
        self.matrix[row][column] = self.user
        Button(self, text=self.user, width=10, height=3, relief=RIDGE,font=("Courier", 9)).grid(row=row, column=column)
        self.check_result()
        if self.user == "X":
            self.user = "O"
        else:
            self.user = "X"

    def check_result(self):
        for element in [0, 1, 2]:
            if list(self.matrix[element]).count("X") == 3 or list(self.matrix[element]).count("O") == 3:
                self.result = True
            elif list(self.matrix.T[element]).count("X") == 3 or list(self.matrix.T[element]).count("O") == 3:
                self.result = True
        if (self.matrix[0][0] == self.matrix[1][1] == self.matrix[2][2]) and self.matrix[0][0] != "":
            self.result = True
        if (self.matrix[2][0] == self.matrix[1][1] == self.matrix[0][2]) and self.matrix[2][0] != "":
            self.result = True
        if self.result:
            messagebox.showinfo("Result", "Woooo...We Have Winner\n******* '{0}' *******\n   Is The Winner".format(self.user))
            self.reset_game()
        if self.matrix.stack().value_counts()[""] == 1:
            messagebox.showinfo("Result", "Its a Draw...\nLets Play Again")
            self.reset_game()

    def reset_game(self):
        self.matrix = pd.DataFrame([[""] * 3] * 3)
        self.result = False
        self.generate_buttons()


if __name__ == '__main__':
    ROOT = Tk()
    ROOT.title("TicTacToe")
    LOGIN = GenerateGui(ROOT)
    LOGIN.grid(sticky=E)
    ROOT.mainloop()
