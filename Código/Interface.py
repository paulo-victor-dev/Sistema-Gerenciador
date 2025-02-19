import tkinter as tk
from tkinter import ttk
import customtkinter as c
from PIL import Image
from Funcoes_Gerais import Botoes_Navegacao, Botoes_Area_Usuario, Botoes_Barra_Acao
from Estilos import Cores
from Tela_Auxiliar import Tela_Auxiliar

class Janela_Principal(c.CTk):
    def __init__(self, nome_usuario, funcao_usuario):
        super().__init__()

        self.nome_usuario = nome_usuario
        self.funcao_usuario = funcao_usuario

        self._configurar_janela()
        self._iniciar_componentes_principais()
        
        self._funcoes_botoes_navegacao()
        self._funcoes_botoes_area_usuario()
        self._funçoes_botoes_barra_acao()
        self._config_inicial()
        
    def _configurar_janela(self):
        c.set_appearance_mode('dark')
        self.title('Sistema Gerenciador')
        self.centralizar_tela(1200,800)
        self.resizable(False, False)
        self.grid_propagate(False)
        self.protocol('WM_DELETE_WINDOW', self._func_fechar_janela)

    def _iniciar_componentes_principais(self):
        self.barra_lateral = Barra_Lateral(self)
        self.conteudo_geral = Conteudo_Geral(self)
        self.tabela = Tabelas(self)

    def _funcoes_botoes_navegacao(self):
        self.funcoes_botoes_navegacao = Botoes_Navegacao(self.conteudo_geral, self.tabela, self.barra_lateral.botoes_criados)

    def _funcoes_botoes_area_usuario(self):
        self.funcoes_botoes_area_usuario = Botoes_Area_Usuario(self)

    def _funçoes_botoes_barra_acao(self):
        self.funçoes_botoes_barra_acao = Botoes_Barra_Acao(self, self.conteudo_geral, self.tabela)
        self.funçoes_botoes_barra_acao._aplicar_funcao_barra_pesquisa()

    def _config_inicial(self):
        self.funcoes_botoes_navegacao._executar_acoes('PEDIDOS')

    def _func_fechar_janela(self):
        Tela_Auxiliar(self, True, self.funcoes_botoes_area_usuario._acao_botao_encerrar, texto='Realmente deseja encerrar o programa?')

    def centralizar_tela(self, largura, altura):
        largura_monitor = self.winfo_screenwidth()
        altura_monitor = self.winfo_screenheight()

        pos_x = (largura_monitor - largura) // 2
        pos_y = (altura_monitor - altura) // 2

        self.geometry(f'{largura}x{altura}+{pos_x}+{pos_y}')

        
class Barra_Lateral:
    def __init__(self, janela_principal):
        self.janela_principal = janela_principal
        self.botoes_criados = {}

        self._iniciar_componentes()

    def _iniciar_componentes(self):
        self._frame_geral()
        self._frame_campo_usuario()
        self._icon_nome_funcao_usuario()
        self._botoes_encerrar_deslogar()
        self._botoes_navegacao()

    def _frame_geral(self):
        self.frame_barra_lateral = c.CTkFrame(
            self.janela_principal,
            width=250,
            height=800,
            corner_radius=0,
            fg_color=Cores.cinza_medio
        )
        self.frame_barra_lateral.grid(row=0, column=0, sticky='w')
        self.frame_barra_lateral.grid_propagate(False)


        self.frame_barra_lateral.grid_rowconfigure(3, weight=0)

    def _frame_campo_usuario(self):
            self.campo_usuario = c.CTkFrame(
                self.frame_barra_lateral,
                width=250,
                height=110,
                corner_radius=0,
                fg_color=Cores.cinza_escuro
            )
            self.campo_usuario.grid(row=0, column=0, sticky='nw')
            self.campo_usuario.grid_propagate(False)

            self.campo_usuario.grid_columnconfigure(0, weight=0)
            self.campo_usuario.grid_columnconfigure(1, weight=1)
            self.campo_usuario.grid_columnconfigure(2, weight=0)

            self.campo_usuario.grid_rowconfigure(0, weight=0)
            self.campo_usuario.grid_rowconfigure(1, weight=0)
            self.campo_usuario.grid_rowconfigure(2, weight=0)
        
    def _icon_nome_funcao_usuario(self):
        img_usuario = c.CTkImage(dark_image=Image.open(r'Imagens\usuario.png'), size=(40,40))
        icone_usuario = c.CTkLabel(
            self.campo_usuario,
            text='',
            image=img_usuario,
            bg_color=Cores.cinza_escuro,
            fg_color=Cores.cinza_escuro
        )
        icone_usuario.grid(row=0, column=0, sticky='w', padx=10, rowspan=2)

        self.nome_usuario = c.CTkLabel(
            self.campo_usuario,
            text=self.janela_principal.nome_usuario,
            font=('Arial', 16, 'bold'),
            bg_color='#2b313f',
            fg_color='#2b313f',
            anchor='s'
        )
        self.nome_usuario.grid(row=0, column=1, sticky='sw', padx=5, pady=5, columnspan=2)

        self.funcao_usuario = c.CTkLabel(
            self.campo_usuario,
            text=self.janela_principal.funcao_usuario,
            font=('Arial', 14),
            bg_color='#2b313f',
            fg_color='#2b313f',
            anchor='n'
        )
        self.funcao_usuario.grid(row=1, column=1, sticky='nw', padx=5, columnspan=3)

    def _botoes_encerrar_deslogar(self):
            img_deslogar = c.CTkImage(dark_image=Image.open(r'Imagens\deslogar.png'), size=(25,25))
            self.botao_deslogar = c.CTkButton(
                self.campo_usuario,
                text='Deslogar',
                image=img_deslogar,
                width=20,
                bg_color=Cores.cinza_escuro,
                anchor='s',
                cursor="hand2",

                command=lambda: self.janela_principal.funcoes_botoes_area_usuario._executar_acao('DESLOGAR')
            )
            self.botao_deslogar.grid(row=2, column=2, sticky='e', padx=10, columnspan=2)

            img_encerrar = c.CTkImage(dark_image=Image.open(r'Imagens\encerrar.png'), size=(25,25))
            self.botao_encerrar = c.CTkButton(
                self.campo_usuario,
                text='Encerrar',
                image=img_encerrar,
                width=20,
                bg_color=Cores.cinza_escuro,
                fg_color=Cores.vermelho_medio,
                hover_color=Cores.vermelho_escuro,
                anchor='s',
                cursor="hand2",

                command=lambda: self.janela_principal.funcoes_botoes_area_usuario._executar_acao('ENCERRAR')
            )
            self.botao_encerrar.grid(row=2, column=0, sticky='w', padx=10, columnspan=2)

    def _botoes_navegacao(self):
        nomes_botoes = [
            'PEDIDOS',
            'CLIENTES',
            'PRODUTOS',
            'USUÁRIOS'
        ]

        for pos, nome_botao in enumerate(nomes_botoes):
            botao = c.CTkButton(
                self.frame_barra_lateral,
                text=nome_botao,
                height=50,
                width=250,
                font=('Arial', 15, 'bold'),
                corner_radius=0,
                fg_color=Cores.cinza_medio,
                bg_color=Cores.cinza_medio,
                hover_color=Cores.cinza_hover,
                cursor="hand2",
                command=self._obter_comando(nome_botao)
            )
            botao.grid(row=pos+2, column=0, sticky='nw', pady=5)

            self.botoes_criados[nome_botao] = botao

    def _obter_comando(self, funcao_botao):
        funcoes = {
            'PEDIDOS': lambda: self.janela_principal.funcoes_botoes_navegacao._executar_acoes('PEDIDOS'),
            'CLIENTES': lambda: self.janela_principal.funcoes_botoes_navegacao._executar_acoes('CLIENTES'),
            'PRODUTOS': lambda: self.janela_principal.funcoes_botoes_navegacao._executar_acoes('PRODUTOS'),
            'USUÁRIOS': lambda: self.janela_principal.funcoes_botoes_navegacao._executar_acoes('USUÁRIOS')
        }

        return funcoes.get(funcao_botao, lambda: None)


class Conteudo_Geral:
    def __init__(self, janela_principal):
        self.janela_principal = janela_principal
        self.botoes_cad_alt_exc = []
        self.botoes_imp_exp = []

        self._iniciar_componentes()

    def _iniciar_componentes(self):
        self._frame_conteudo_geral()
        self._nome_btn_qtd_itens()
        self._frame_barra_de_acoes()
        self._barra_pesquisa()
        self._botoes_importar_exportar()
        self._botoes_cadastrar_editar_excluir()

    def _frame_conteudo_geral(self):
        self.frame_conteudo = c.CTkFrame(
            self.janela_principal,
            width=950,
            height=800,
            corner_radius=0,
            fg_color=Cores.cinza_claro,
        )
        self.frame_conteudo.grid(row=0, column=1, sticky='ne')
        self.frame_conteudo.grid_propagate(False)

    def _nome_btn_qtd_itens(self):
        self.nome_botao_selecionado = c.CTkLabel(
            self.frame_conteudo,
            text='PEDIDOS',
            font=('Arial', 35, 'bold'),
            text_color=Cores.cinza_escuro,
            bg_color=Cores.cinza_claro
        )
        self.nome_botao_selecionado.grid(row=0, column=1, sticky='nw', padx=15, pady=30)

        self.qtd_itens = c.CTkLabel(
            self.frame_conteudo,
            text='',
            font=('Arial', 17,),
            text_color=Cores.cinza_escuro,
            bg_color=Cores.cinza_claro
        )
        self.qtd_itens.grid(row=0, column=1, sticky='nw', padx=230, pady=40)

    def _frame_barra_de_acoes(self):
        self.frame_barra_de_acoes = c.CTkFrame(
            self.frame_conteudo,
            width=930,
            height=60,
            corner_radius=10,
            bg_color=Cores.cinza_claro,
            fg_color=Cores.branco
        )
        self.frame_barra_de_acoes.grid(row=0, column=1, sticky='n', padx=10, pady=100)
        self.frame_barra_de_acoes.grid_propagate(False)

        self.frame_barra_de_acoes.grid_columnconfigure(0, weight=0)
        self.frame_barra_de_acoes.grid_columnconfigure(1, weight=1)
        self.frame_barra_de_acoes.grid_columnconfigure(2, weight=0)
        self.frame_barra_de_acoes.grid_columnconfigure(3, weight=0)
        self.frame_barra_de_acoes.grid_columnconfigure(4, weight=1)
        self.frame_barra_de_acoes.grid_columnconfigure(5, weight=0)
        self.frame_barra_de_acoes.grid_columnconfigure(6, weight=0)
        self.frame_barra_de_acoes.grid_columnconfigure(7, weight=0)

    def _barra_pesquisa(self):
        self.barra_pesquisa = c.CTkEntry(
            self.frame_barra_de_acoes,
            placeholder_text='Id do pedido ou nome do cliente',
            width=300,
            height=50,
            corner_radius=10,
            border_color=Cores.cinza_borda,
            border_width=2,
            fg_color=Cores.branco,
            bg_color=Cores.branco,
            font=('Arial', 15),
            text_color=Cores.cinza_escuro
        )
        self.barra_pesquisa.grid(row=0, column=0, sticky='nw', padx=5, pady=5)


        img_lupa = c.CTkImage(dark_image=Image.open(r'Imagens\lupa.png'), size=(35,35))
        label_img_lupa = c.CTkLabel(
            self.frame_barra_de_acoes,
            text='',
            width=35,
            height=35,
            image=img_lupa,
            bg_color=Cores.branco,
            fg_color=Cores.branco,
        )
        label_img_lupa.grid(row=0, column=0, sticky='ne', padx=15, pady=12)

    def _botoes_importar_exportar(self):
        self.botoes_imp_exp.clear()

        config_botoes = [
            {
                'texto': 'Importar itens',
                'img': r'Imagens\importar.png',
                'tam_img': (20,20),
                'comando': lambda: print('funcionou')
            },

            {
                'texto': 'Exportar itens',
                'img': r'Imagens\exportar.png',
                'tam_img': (20,20),
                'comando': lambda: print('funcionou')
            }
        ]

        for pos, botao in enumerate(config_botoes):
            img = c.CTkImage(dark_image=Image.open(botao['img']), size=botao['tam_img'])

            btn = c.CTkButton(
                self.frame_barra_de_acoes,
                text=botao['texto'],
                compound='left',
                image=img,
                width=120,
                height=50,
                corner_radius=10,
                font=('Arial', 15, 'bold'),
                text_color='black',
                bg_color=Cores.branco,
                fg_color=Cores.branco,
                hover_color=Cores.cinza_borda,
                cursor="hand2",
                command=botao['comando']
            )
            btn.grid(row=0, column=pos+2 if pos==0 else 3, sticky='w', padx=5 if pos==0 else 10, pady=5)

            self.botoes_imp_exp.append(btn)

    def _botoes_cadastrar_editar_excluir(self):
        self.botoes_cad_alt_exc.clear()

        self.config_botoes = [
            {
                'imagem': r'Imagens\adicionar.png',
                'tam_img': (35,35),
                'comando': lambda: self.janela_principal.funçoes_botoes_barra_acao._gerar_form_cadastro()
            },

            {
                'imagem': r'Imagens\editar.png',
                'tam_img': (35,35),
                'comando': lambda: self.janela_principal.funçoes_botoes_barra_acao._gerar_form_alt_item()
            },

            {
                'imagem': r'Imagens\excluir.png',
                'tam_img': (35,35),
                'comando': lambda: self.janela_principal.funçoes_botoes_barra_acao._acao_excluir_dado()
            }
        ]

        for pos, botao in enumerate(self.config_botoes):
            imagem = c.CTkImage(dark_image=Image.open(botao['imagem']), size=botao['tam_img'])

            btn = c.CTkButton(
                self.frame_barra_de_acoes,
                text='',
                image=imagem,
                width=35,
                height=50,
                corner_radius=10,
                bg_color=Cores.branco,
                fg_color=Cores.branco,
                hover_color=Cores.cinza_borda,
                cursor='hand2',
                command=botao['comando']
            )
            btn.grid(row=0, column=5+pos, sticky='w', padx=5, pady=5)

            self.botoes_cad_alt_exc.append(btn)


class Tabelas:
    def __init__(self, janela_principal):
        self.janela_principal = janela_principal
        
        self.tabela_criada = None
        
        self._iniciar_componentes()

    def _iniciar_componentes(self):
        self._frame_tabela()
        self._estilo_tabela()

    def _estilo_tabela(self):
        self.estilo_tabela = ttk.Style()
        self.estilo_tabela.configure("Treeview.Heading", font=("Arial", 12, "bold"))
        self.estilo_tabela.configure("Treeview", rowheight=25, font=("Arial", 10))
        self.estilo_tabela.configure("Treeview", highlightthickness=0, bd=0, borderwidth=0)
        self.estilo_tabela.layout("Treeview", [("Treeview.treearea", {"sticky": "nswe"})])

    def _frame_tabela(self):
        self.corpo_tabela = c.CTkFrame(
            self.janela_principal,
            width=930,
            height=620,
            corner_radius=10,
            bg_color=Cores.cinza_claro,
            fg_color=Cores.branco
        )
        self.corpo_tabela.grid(row=0, column=1, sticky='s', pady=10)
        self.corpo_tabela.grid_propagate(False)

    def _criar_tabela_geral(self, colunas, larguras, valores):
        self.tabela = ttk.Treeview(
            self.corpo_tabela,
            columns=colunas,
            show='headings',
            height=23
        )

        for coluna, largura in zip(colunas, larguras):
            self.tabela.heading(coluna, text=coluna)
            self.tabela.column(coluna, width=largura, anchor='center')

        self.tabela.grid(row=0, column=0, padx=5, pady=8)

        for valor in valores:
            self.tabela.insert('', index=tk.END, values=valor)

        self._config_barra_rolagem()
        self.tabela_criada = self.tabela

    def _config_barra_rolagem(self):
        self.barra_rolagem_tabela = c.CTkScrollbar(
            self.corpo_tabela,
            orientation='vertical',
            command=self.tabela.yview
        )
        self.barra_rolagem_tabela.grid(row=0, column=1, sticky='ns')

        self.tabela.configure(yscrollcommand=self.barra_rolagem_tabela.set)

    def _att_valores_tabela(self, valores):
        for item in self.tabela_criada.get_children():
            self.tabela_criada.delete(item)

        for valor in valores:
            self.tabela_criada.insert('', index=tk.END, values=valor)
        

class Form_Cadastrar_Item:
    def __init__(self, janela_principal, classe_tabela):
        self.janela_principal = janela_principal
        self.classe_tabela = classe_tabela

        self.lista_entrys = []
        self.lista_frames_tabelas = []

    def _iniciar_form(self, texto_titulo, subtitulos=[], form_pedidos=False):
        for item in self.classe_tabela.corpo_tabela.winfo_children():
            item.destroy()

        self._titulo_form(texto_titulo)

        if form_pedidos:
            self._layout_pedidos()
        else:
            self._layout_padrao_form(subtitulos)
            return self.lista_entrys
            
    def _titulo_form(self, texto_titulo):
        self.titulo_cad = c.CTkLabel(
            self.classe_tabela.corpo_tabela,
            text=texto_titulo,
            font=('Arial', 20, 'bold'),
            text_color=Cores.cinza_escuro
        )
        self.titulo_cad.grid(row=0, column=0, sticky='nw', padx=20, pady=20)

        linha_titulo = c.CTkFrame(
            self.classe_tabela.corpo_tabela,
            height=2,
            width=890,
            corner_radius=10,
            fg_color=Cores.cinza_claro,
            bg_color=Cores.branco,
        )
        linha_titulo.grid(row=0, column=0, sticky='s', padx=20, pady=10)

    def _layout_padrao_form(self, subtitulos):
        self.lista_entrys.clear()

        for pos, subtitulo in enumerate(subtitulos, start=2):
            descricao_campo = c.CTkLabel(
                self.classe_tabela.corpo_tabela,
                text=subtitulo,
                font=('Arial', 15, 'bold'),
                text_color=Cores.cinza_escuro,
                anchor='s'
            )
            descricao_campo.grid(row=(pos-1)*2, column=0, sticky='sw', padx=20)
            
            self.dado_entry = c.CTkEntry(
                self.classe_tabela.corpo_tabela,
                height=30,
                width=890,
                corner_radius=5,
                border_color=Cores.cinza_borda,
                border_width=2,
                fg_color=Cores.branco,
                bg_color=Cores.branco,
                font=('Arial', 14),
                text_color=Cores.cinza_escuro
            )
            self.dado_entry.grid(row=(pos-1)*2+1, column=0, sticky='nw', padx=20, pady=10)

            self.lista_entrys.append(self.dado_entry)

        self.botao_salvar = c.CTkButton(
            self.classe_tabela.corpo_tabela,
            text='SALVAR',
            width=100,
            height=40,
            font=('Arial', 15, 'bold'),
            corner_radius=10,
            bg_color=Cores.branco,
            fg_color=Cores.verde_medio,
            hover_color=Cores.verde_escuro,
            cursor="hand2",
            
            command=lambda: self.janela_principal.funçoes_botoes_barra_acao._acao_cadastrar_dado()
        )
        self.botao_salvar.grid(row=(len(subtitulos)*2)+2, column=0, sticky='w', padx=130, pady=20)

        botao_voltar = c.CTkButton(
            self.classe_tabela.corpo_tabela,
            text='VOLTAR',
            width=100,
            height=40,
            font=('Arial', 15, 'bold'),
            corner_radius=10,
            bg_color=Cores.branco,
            cursor="hand2",

            command=lambda: self.janela_principal.funçoes_botoes_barra_acao._acao_btn_voltar()
        )
        botao_voltar.grid(row=(len(subtitulos)*2)+2, column=0, sticky='w', padx=20, pady=20)

    def _layout_pedidos(self):
        self._frame_cliente_info_ped()
        self._campo_selecionar_cliente()
        self._campo_itens_pedido()
        self._frames_tabelas_cad_pedido()
        self._titulos_tabelas()
        self._btns_tabelas()
        self._barra_pesquisa_tabelas()
        self._entrys_labels_qtd_itens()
        self._btns_voltar_salvar()
        self._campo_total_pedido()

    def _frame_cliente_info_ped(self):
        self.frame_cliente_info_ped = c.CTkFrame(
            self.classe_tabela.corpo_tabela,
            width=930,
            height=88,
            corner_radius=0,
            fg_color=Cores.branco,
            bg_color=Cores.branco
        )
        self.frame_cliente_info_ped.grid(row=2, column=0, sticky='nw')
        self.frame_cliente_info_ped.grid_propagate(False)

        for i in range(0, 3):
            self.frame_cliente_info_ped.grid_columnconfigure(i, weight=1)

    def _campo_selecionar_cliente(self):
        label_sele_cliente = c.CTkLabel(
            self.frame_cliente_info_ped,
            text='SELECIONE O CLIENTE',
            font=('Arial', 15, 'bold'),
            text_color=Cores.cinza_escuro,
            anchor='s'
        )
        label_sele_cliente.grid(row=0, column=0, sticky='sw', padx=20)

        self.entry_sele_cliente = c.CTkEntry(
            self.frame_cliente_info_ped,
            height=40,
            width=300,
            corner_radius=5,
            border_color=Cores.cinza_borda,
            border_width=2,
            fg_color=Cores.branco,
            bg_color=Cores.branco,
            font=('Arial', 14),
            text_color=Cores.cinza_escuro,
            placeholder_text='Id, Nome ou CPF do cliente'
        )
        self.entry_sele_cliente.grid(row=1, column=0, sticky='nw', padx=20, pady=10, columnspan=2)

    def _campo_itens_pedido(self):
        label_itens = c.CTkLabel(
            self.classe_tabela.corpo_tabela,
            text='SELECIONE OS ITENS DO PEDIDO',
            font=('Arial', 15, 'bold'),
            text_color=Cores.cinza_escuro,
            anchor='s'
        )
        label_itens.grid(row=4, column=0, sticky='sw', padx=20)

        self.frame_itens_pedido = c.CTkFrame(
            self.classe_tabela.corpo_tabela,
            width=930,
            height=430,
            corner_radius=0,
            fg_color=Cores.branco,
            bg_color=Cores.branco
        )
        self.frame_itens_pedido.grid(row=5, column=0, sticky='nw')
        self.frame_itens_pedido.grid_propagate(False)

        for i in range(0, 7):
            self.frame_itens_pedido.grid_columnconfigure(i, weight=1)

    def _titulos_tabelas(self):
        lista_titulos_tabs = ['PRODUTOS CADASTRADOS:', 'PRODUTOS DO PEDIDO:']

        for pos, tab in enumerate(lista_titulos_tabs):
            titulo_tab = c.CTkLabel(
                self.frame_itens_pedido,
                text=tab,
                font=('Arial', 14, 'bold'),
                text_color=Cores.cinza_escuro,
                anchor='s'
            )
            titulo_tab.grid(row=0, column=0 if pos == 0 else 4, sticky='sw', padx=20, pady=5, columnspan=3)

    def _btns_tabelas(self):
        botoes_tab = [
            {
              'texto_btn': 'ADICIONAR ITEM',
              'comando': lambda: print('funcionou')
            },

            {
              'texto_btn': 'EXCLUIR ITEM',
              'comando': lambda: print('funcionou')
            }
        ]
        for pos, btn in enumerate(botoes_tab):
            btn_tabela = c.CTkButton(
                self.frame_itens_pedido,
                text=btn['texto_btn'],
                height=20,
                font=('Arial', 13, 'bold'),
                corner_radius=10,
                bg_color=Cores.branco,
                cursor="hand2",
                anchor='s',
                
                command=btn['comando']
            )
            btn_tabela.grid(row=0, column=2 if pos == 0 else 6, sticky='sw' if pos==0 else 'se', padx=None if pos==0 else 20, pady=5, columnspan=3)

    def _barra_pesquisa_tabelas(self):
        for i in range(0, 2):
            self.barra_pesquisa_tabs = c.CTkEntry(
                self.frame_itens_pedido,
                placeholder_text='ID, descrição ou cód. de barras',
                width=225,
                height=30,
                corner_radius=10,
                border_color=Cores.cinza_borda,
                border_width=2,
                fg_color=Cores.branco,
                bg_color=Cores.branco,
                font=('Arial', 13),
                text_color=Cores.cinza_escuro
            )
            self.barra_pesquisa_tabs.grid(row=2, column=0 if i==0 else 4, sticky='w', padx=20, pady=5, columnspan=4)

    def _entrys_labels_qtd_itens(self):
        for i in range(0, 2):
            self.labels_qtd_itens = c.CTkLabel(
                self.frame_itens_pedido,
                text='QUANTIDADE:',
                font=('Arial', 13, 'bold'),
                text_color=Cores.cinza_escuro
            )
            self.labels_qtd_itens.grid(row=2, column=1 if i==0 else 5, sticky='e', padx=5 if i==0 else 85, pady=5, columnspan=2)


            self.entrys_quantidade_itens = c.CTkEntry(
                self.frame_itens_pedido,
                width=60,
                height=30,
                corner_radius=10,
                border_color=Cores.cinza_borda,
                border_width=2,
                fg_color=Cores.branco,
                bg_color=Cores.branco,
                font=('Arial', 13),
                text_color=Cores.cinza_escuro
            )
            self.entrys_quantidade_itens.grid(row=2, column=2 if i==0 else 6, sticky='e', padx=20, pady=5, columnspan=2)

    def _frames_tabelas_cad_pedido(self):
        for i in range(0, 2):
            frame_tab_cad_pedido = c.CTkFrame(
                self.frame_itens_pedido,
                width=450,
                height=300,
                corner_radius=0,
                border_width=2,
                fg_color=Cores.branco,
                bg_color=Cores.branco
            )
            frame_tab_cad_pedido.grid(row=3, column=0 if i==0 else 4, sticky='nw', padx=20, columnspan=4)
            frame_tab_cad_pedido.grid_propagate(False)

            self.lista_frames_tabelas.append(frame_tab_cad_pedido)

    def _btns_voltar_salvar(self):
        btn_voltar_cad_pedido = c.CTkButton(
            self.frame_itens_pedido,
            text='VOLTAR',
            width=100,
            height=40,
            font=('Arial', 15, 'bold'),
            corner_radius=10,
            bg_color=Cores.branco,
            cursor="hand2",

            command=lambda: self.janela_principal.funçoes_botoes_barra_acao._acao_btn_voltar()
        )
        btn_voltar_cad_pedido.grid(row=4, column=0, sticky='w', padx=20, pady=10)

        btn_salvar_cad_pedido = c.CTkButton(
            self.frame_itens_pedido,
            text='SALVAR',
            width=100,
            height=40,
            font=('Arial', 15, 'bold'),
            corner_radius=10,
            bg_color=Cores.branco,
            fg_color=Cores.verde_medio,
            hover_color=Cores.verde_escuro,
            cursor="hand2",

            command=lambda: print('Funcionou')
        )
        btn_salvar_cad_pedido.grid(row=4, column=0, sticky='e', padx=65, pady=10, columnspan=2)

    def _campo_total_pedido(self):
        total_pedido = c.CTkLabel(
            self.frame_itens_pedido,
            text='TOTAL PEDIDO: ',
            font=('Arial', 16, 'bold'),
            text_color=Cores.cinza_escuro
        )
        total_pedido.grid(row=4, column=4, sticky='w', padx=25, pady=5, columnspan=2)
        
        self.valor_pedido = c.CTkLabel(
            self.frame_itens_pedido,
            text='R$ 0,00',
            font=('Arial', 18, 'bold'),
            text_color=Cores.cinza_escuro
        )
        self.valor_pedido.grid(row=4, column=4, sticky='e', padx=25, pady=5, columnspan=4)


class Form_Alterar_Item(Form_Cadastrar_Item):        
    def __init__(self, janela_principal, classe_tabela):
        super().__init__(janela_principal, classe_tabela)

    def _iniciar_form_alt_item(self, valores, texto_titulo, subtitulos=[], form_pedidos=False):
        lista_entrys = self._iniciar_form(texto_titulo, subtitulos, form_pedidos)
        self._preencher_valores_entrys(valores)
        self._alterar_command_btn_salvar()

        return lista_entrys
        
        
    def _preencher_valores_entrys(self, valores):
        for valor, dado in zip(valores, self.lista_entrys):
            dado.insert(0, valor)
            
    def _alterar_command_btn_salvar(self):
        self.botao_salvar.configure(command=lambda: self.janela_principal.funçoes_botoes_barra_acao._acao_alterar_dado())


if __name__ == '__main__':
    app = Janela_Principal('PAULO GONÇALVES', 'ADMINISTRADOR DE REDE')
    app.mainloop()

    "Também, colocar datas de criação e alteração do pedido"
    "Colocar um campo de comentário e rever a lógica para aparecer esse comentário"