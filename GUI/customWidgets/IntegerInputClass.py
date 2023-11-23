import customtkinter as ctk
from settings import *


class IntegerInput(ctk.CTkFrame):
    def __init__(self, master, var):
        super().__init__(master=master, fg_color='transparent')

        self.var = var

        self.title = ctk.CTkLabel(master=self, text='Search depth',
                                  font=ctk.CTkFont(size=SMALL_FONT_SIZE, family=FONT_FAMILY))
        self.title.pack(side='top', expand=True)
        self.label = ctk.CTkLabel(master=self, textvariable=var,
                                  font=ctk.CTkFont(size=SMALL_FONT_SIZE, family=FONT_FAMILY))
        self.inc_btn = ctk.CTkButton(master=self, text='+',
                                     width=20, height=20,
                                     font=ctk.CTkFont(size=SMALL_FONT_SIZE, family=FONT_FAMILY))

        self.inc_btn.bind('<B1-Motion>', self.increment)
        self.inc_btn.bind('<Button-1>', self.increment)

        self.dec_btn = ctk.CTkButton(master=self, text='-', state='disabled',
                                     width=20, height=20,
                                     font=ctk.CTkFont(size=SMALL_FONT_SIZE, family=FONT_FAMILY))
        self.dec_btn.bind('<B1-Motion>', self.decrement)
        self.dec_btn.bind('<Button-1>', self.decrement)

        self.counter = 1

        self.dec_btn.pack(side='left', padx=5, pady=2, expand=True)
        self.label.pack(side='left', padx=5, pady=2, expand=True)
        self.inc_btn.pack(side='left', padx=5, pady=2, expand=True)

    def increment(self, e):
        self.counter = self.counter + 1
        if self.counter > 1:
            self.dec_btn.configure(state='normal')
        self.var.set(self.counter)

    def decrement(self, e):
        self.counter = self.counter - 1
        self.var.set(max(1, self.counter))
        if self.counter == 1:
            self.var.set(1)
            self.dec_btn.configure(state='disabled')
