from customtkinter import CTkFrame


class MainFrame(CTkFrame):
    def __init__(self, com_score, user_score, **kwargs):
        super().__init__(**kwargs, corner_radius=0, fg_color='transparent')
