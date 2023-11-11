import customtkinter as ctk
from settings import *


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f'{WIN_WIDTH}x{WIN_HEIGHT}')
        self.title(TITLE)
        self.mainloop()


if __name__ == '__main__':
    App()
