import customtkinter as ctk


class LowerFrame(ctk.CTkFrame):
    def __init__(self, agent_score, user_score, state_value, **kwargs):
        super().__init__(**kwargs)
