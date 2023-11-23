import customtkinter as ctk
from settings import *


class LowerFrame(ctk.CTkFrame):
    def __init__(self, agent_score, user_score, state_value, **kwargs):
        super().__init__(**kwargs)
        agent_score_label = ctk.CTkLabel(master=self, textvariable=agent_score,
                                         font=ctk.CTkFont(size=MEDIUM_FONT_SIZE, family=FONT_FAMILY))
        user_score_label = ctk.CTkLabel(master=self, textvariable=user_score,
                                        font=ctk.CTkFont(size=MEDIUM_FONT_SIZE, family=FONT_FAMILY))
        state_value_label = ctk.CTkLabel(master=self, textvariable=state_value,
                                         font=ctk.CTkFont(size=MEDIUM_FONT_SIZE, family=FONT_FAMILY))
        agent_score_label.pack()
        user_score_label.pack()
        state_value_label.pack()
