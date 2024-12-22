import customtkinter as ctk

class Plague(ctk.CTk):

    def __init__(self):
        super().__init__()

        # JANELA
        self.geometry("640x360") # Tamanho da janela
        self.title("Plague Hack | by Swth") # Título da janela
        self._set_appearance_mode("dark") # Tema da janela
        self.resizable(False,False)   # Travar janela

        # Widgets
        self.label_instrucoes = ctk.CTkLabel(self, text="P L A G U E",font=("Arial",14))
        self.label_instrucoes.pack(pady=10)

        self.entrada = ctk.CTkEntry(self, placeholder_text="Quantidade DNA")
        self.entrada.pack(pady=10)

        self.botao_enviar = ctk.CTkButton(self, text="Inject", )
        self.botao_enviar.pack(pady=10)