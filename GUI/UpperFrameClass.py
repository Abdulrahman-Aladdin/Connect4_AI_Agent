import customtkinter as ctk
from customWidgets.MainFrameClass import MainFrame
from PIL import Image


class UpperFrame(ctk.CTkFrame):
    def __init__(self, com_score, user_score, **kwargs):
        super().__init__(**kwargs)

        self.board_frame = ctk.CTkFrame(master=self, fg_color='#12a', corner_radius=20)
        self.board_frame.place(relx=.5, rely=.5, anchor='center')
        self.row = 6
        self.col = 7
        self.com_score = com_score
        self.user_score = user_score
        self.turn = 1

        self.rowconfigure(tuple(range(self.row + 1)), weight=1, uniform='a')
        self.columnconfigure(tuple(range(self.col)), weight=1, uniform='b')
        self.img_size = 80
        self.board = [[0 for _ in range(self.col)] for _ in range(self.row)]
        self.red_img = ctk.CTkImage(Image.open('red_circle.png'),
                                    size=(self.img_size, self.img_size))
        self.blue_img = ctk.CTkImage(Image.open('blue_circle.png'),
                                     size=(self.img_size, self.img_size))
        self.img = ctk.CTkImage(Image.open('oval.png'),
                                size=(self.img_size, self.img_size))

        for i in range(self.col):
            ctk.CTkLabel(master=self.board_frame, text=f'{i+1}', corner_radius=20).grid(row=0, column=i, stick='nsew')

        self.board_btns = [[ctk.CTkButton(master=self.board_frame, text='', image=self.img, fg_color='transparent',
                                          corner_radius=20, command=lambda col=j: self.play_at(col))
                            for j in range(self.col)]
                           for _ in range(self.row)]
        for i in range(1, self.row + 1):
            for j in range(self.col):
                self.board_btns[i-1][j].grid(row=i, column=j)

    def play_at(self, i):
        for j in range(self.row - 1, -1, -1):
            if self.board[j][i] == 0:
                if self.turn == 1:  # user turn
                    self.board_btns[j][i].configure(image=self.red_img)
                    self.board[j][i] = 1
                    self.turn = -1
                else:
                    self.board_btns[j][i].configure(image=self.blue_img)
                    self.board[j][i] = -1
                    self.turn = 1
                break

        if all(cell != 0 for row in self.board for cell in row):
            print('game over!')
            for row in self.board_btns:
                for btn in row:
                    btn.configure(state='disabled')

    def evaluate(self, i, j):
        pass
