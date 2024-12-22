import customtkinter as ctk
from PIL import Image
import os

class Plague(ctk.CTk):

    def __init__(self):
        super().__init__()

        # JANELA
        self.geometry("640x360") # Tamanho da janela
        self.title("Plague Hack | by Swth") # Título da janela
        self._set_appearance_mode("dark") # Tema da janela
        self.resizable(False,False)   # Travar janela

        # Background
        self.bg_path = "app/models/src/background.png"
        image = Image.open(self.bg_path)
        self.bg_image = ctk.CTkImage(dark_image=image, size=(640,360))

        # Image de Fundo
        self.bg_label = ctk.CTkLabel(self, image=self.bg_image, text="")
        self.bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Widgets

        self.entrada = ctk.CTkEntry(self, placeholder_text="Quantidade DNA")
        self.entrada.place(relx=0.5, rely=0.45, anchor="center")

        self.botao_enviar = ctk.CTkButton(self, text="Inject", fg_color="#363636",hover_color="#4F4F4F")
        self.botao_enviar.place(relx=0.5, rely=0.55, anchor="center")