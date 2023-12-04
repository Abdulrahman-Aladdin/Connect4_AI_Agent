import customtkinter as ctk
from settings import *
from tkinter import font
from GameFrameClass import GameFrame
from customWidgets.IntegerInputClass import IntegerInput
from controller.ControllerClass import Controller
from tree import *


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f'{WIN_WIDTH}x{WIN_HEIGHT}')
        self.title(TITLE)
        self.com_score = ctk.StringVar(value='Agent score: 0')
        self.user_score = ctk.StringVar(value='User score: 0')
        self.state_value = ctk.StringVar(value='State value: 0')

        self.controller = Controller()

        self.game_frame = GameFrame(master=self, com_score=self.com_score, user_score=self.user_score,
                                    state_value=self.state_value, agent_fn=self.get_agent_play)

        self.welcome_frame = ctk.CTkFrame(master=self)
        self.welcome_frame.pack(expand=True, fill='both')

        self.pruning_option_var = ctk.StringVar(value='without pruning')
        self.k_value = ctk.StringVar(value='1')

        self.set_welcome_frame()
        # print(font.families())
        self.mainloop()

    def set_welcome_frame(self):
        self.welcome_frame.rowconfigure((0, 1, 2), weight=1, uniform='a')
        self.welcome_frame.columnconfigure((0, 1, 2, 3), weight=1, uniform='b')

        title_label = ctk.CTkLabel(master=self.welcome_frame, text='Connect Four',
                                   font=ctk.CTkFont(family=FONT_FAMILY, size=LARGE_FONT_SIZE))
        title_label.grid(row=0, column=1, columnspan=2, stick='nsew')

        input_frame = ctk.CTkFrame(master=self.welcome_frame, fg_color='transparent')
        input_frame.grid(row=1, column=1, rowspan=2, columnspan=2, stick='nsew', pady=30)

        label = ctk.CTkLabel(master=input_frame, text='Choose game configurations',
                             font=ctk.CTkFont(family=FONT_FAMILY, size=MEDIUM_FONT_SIZE))
        label.pack(padx=10, pady=10)

        seg_btn = ctk.CTkSegmentedButton(master=input_frame, values=['With pruning', 'without pruning'],
                                         variable=self.pruning_option_var,
                                         font=ctk.CTkFont(family=FONT_FAMILY, size=SMALL_FONT_SIZE))
        seg_btn.pack(padx=10, pady=10)

        k_entry = IntegerInput(master=input_frame, var=self.k_value)
        k_entry.pack(padx=10, pady=10)

        start_btn = ctk.CTkButton(master=input_frame, text='start game',
                                  command=self.start_game, font=ctk.CTkFont(family=FONT_FAMILY, size=SMALL_FONT_SIZE))
        start_btn.pack(padx=10, pady=10)

    def start_game(self):
        self.welcome_frame.pack_forget()
        self.game_frame.pack(expand=True, fill='both')
        prun = False
        if self.pruning_option_var.get() == 'With pruning':
            prun = True
        self.controller.initiate_agent(int(self.k_value.get()), prun)

    def get_agent_play(self, state):
        column, user_score, agent_score, state_value, adj_list, values = self.controller.agent_turn(state)
        self.user_score.set(f'User score: {user_score}')
        self.com_score.set(f'Agent score: {agent_score}')
        self.state_value.set(f'State value: {state_value}')
        self.game_frame.upper_frame.play_at(column)
        # self.show_tree(adj_list, values)

    def show_tree(self, adj_list, values):
        win = ctk.CTkToplevel(self)
        tree_viewer = TreeGraphGUI(win, adj_list, values, int(self.k_value.get()))
        tree_viewer.display_tree()


if __name__ == '__main__':
    App()
