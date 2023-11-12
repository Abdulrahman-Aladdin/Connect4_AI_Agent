from customWidgets.MainFrameClass import MainFrame
from LowerFrameClass import LowerFrame
from UpperFrameClass import UpperFrame
import customtkinter as ctk


class GameFrame(ctk.CTkFrame):
    def __init__(self, com_score, user_score, **kwargs):
        super().__init__(**kwargs)

        self.upper_frame = UpperFrame(master=self, com_score=com_score, user_score=user_score)
        self.upper_frame.place(x=0, y=0, relwidth=1, relheight=.7)

        self.lower_frame = LowerFrame(master=self)
        self.lower_frame.place(x=0, rely=.7, relwidth=1, relheight=.3)
