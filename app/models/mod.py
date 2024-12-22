import customtkinter

class Plague(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # JANELA
        self.geometry("640x360")
        self.title("Plague Hack | by Swth")
        self._set_appearance_mode("dark") # Tema da janela
        self.resizable(False,False)   # Travar janela

