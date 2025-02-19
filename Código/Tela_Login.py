import customtkinter as c
from PIL import Image
from Tela_Auxiliar import Tela_Auxiliar
from Script_Banco_Dados import Exibir

class Tela_Login(c.CTk):
    def __init__(self):
        super().__init__()

        self._configurar_janela()
        self._iniciar_componentes()
        self._iniciar_funcoes()

    def _configurar_janela(self):
        c.set_appearance_mode("dark")
        self.centralizar_tela(900,600)
        self.title('Sistema Gerenciador - Login')
        self.resizable(False, False)

    def _iniciar_componentes(self):
        self.imagem_de_fundo()
        self.frame_principal()
        self.titulo_login()
        self.area_usuario()
        self.area_senha()
        self.area_botao_entrar()

    def _iniciar_funcoes(self):
        self.funcao_tela_login = Funcoes_Tela_Login(self)

    def imagem_de_fundo(self):
        caminho_img_fundo = c.CTkImage(dark_image=Image.open(r'imagens\fundo_tela_login.jpg'), size=(900,600))

        img_fundo = c.CTkLabel(
            self,
            text='',
            image=caminho_img_fundo
        )
        img_fundo.grid(row=0, column=0)

    def frame_principal(self):
        self.frame_principal_login = c.CTkFrame(
            self,
            height=500,
            width=450,
            fg_color='#1d2027'
        )
        self.frame_principal_login.grid(row=0, column=0, sticky='nse')
        self.frame_principal_login.grid_propagate(False)

        for i in range(6):
            self.frame_principal_login.grid_rowconfigure(i, weight=0)        
       
    def titulo_login(self):
        titulo_login = c.CTkLabel(
            self.frame_principal_login,
            text='LOGIN',
            font=('Arial', 50, 'bold')
        )
        titulo_login.grid(row=0, column=0, padx=145, pady=50)

    def area_usuario(self):
        texto_usuario_login = c.CTkLabel(
            self.frame_principal_login,
            text='USUÁRIO',
            font=('Arial', 12, 'bold')
        )
        texto_usuario_login.grid(row=1, column=0, sticky='w', padx=50)

        self.nome_usuario = c.CTkEntry(
            self.frame_principal_login,
            font=('Arial', 16),
            height=40,
            width=370
        )
        self.nome_usuario.grid(row=2, column=0, sticky='n', padx=45)

    def area_senha(self):
        texto_senha_login = c.CTkLabel(
            self.frame_principal_login,
            text='SENHA',
            font=('Arial', 12, 'bold')
        )
        texto_senha_login.grid(row=4, column=0, sticky='w', padx=50, pady=40)

        self.senha_login = c.CTkEntry(
            self.frame_principal_login,
            show='*',
            font=('Arial', 16),
            height=40,
            width=370
        )
        self.senha_login.grid(row=4, column=0, sticky='s', padx=45)

    def area_botao_entrar(self):
        self.botao_entrar = c.CTkButton(
            self.frame_principal_login,
            text='ENTRAR',
            height=60,
            width=370,
            font=('Arial', 20, 'bold'),
            cursor="hand2",

            command=lambda: self.funcao_tela_login.execucao_geral()
        )
        self.botao_entrar.grid(row=5, column=0, sticky='w', padx=50, pady=80)

    def centralizar_tela(self, largura, altura):
        largura_monitor = self.winfo_screenwidth()
        altura_monitor = self.winfo_screenheight()

        pos_x = (largura_monitor - largura) // 2
        pos_y = (altura_monitor - altura) // 2

        self.geometry(f'{largura}x{altura}+{pos_x}+{pos_y}')


class Funcoes_Tela_Login:
    def __init__(self, tela_login):
        self.tela_login = tela_login
        self.exibir = Exibir()
        
    def autenticação(self):
        self.nome_usuario = self.tela_login.nome_usuario.get()
        self.senha = self.tela_login.senha_login.get()

        lista_usuarios = self.exibir.exibir_usuarios()
        
        for usuario in lista_usuarios:
            if self.nome_usuario.upper() == usuario[4] and self.senha == usuario[5]:
                self.nome_usuario = usuario[1]
                self.funcao = usuario[3]
                return True

        self.tela_aviso = Tela_Auxiliar(self.tela_login, texto='Usuário ou senha incorretos!')
        return False
         
    def formatar_nome_e_funcao(self):
        sep_nome = self.nome_usuario.split()
        pri_nome = sep_nome[0]
        ultimo_nome = sep_nome[-1]

        if len(sep_nome) == 1:
            juncao_nome_usuario = pri_nome
        else:
            juncao_nome_usuario = f'{pri_nome} {ultimo_nome}'
            
        if len(juncao_nome_usuario) > 16:
            juncao_nome_usuario = f'{pri_nome} {ultimo_nome[:1]}.'
        
        if len(self.funcao) > 20:
            sep_funcao = self.funcao.split()
            funcao = sep_funcao[0]
        else:
            funcao = self.funcao

        return juncao_nome_usuario, funcao

    def execucao_geral(self):
        from Interface import Janela_Principal

        if self.autenticação():
            nome_usuario, funcao_usuario = self.formatar_nome_e_funcao()

            self.tela_login.destroy()

            tela_principal = Janela_Principal(nome_usuario, funcao_usuario)
            tela_principal.protocol('WM_DELETE_WINDOW', tela_principal._func_fechar_janela)
            tela_principal.mainloop()

if __name__ == '__main__':
    app = Tela_Login()

    app.mainloop()