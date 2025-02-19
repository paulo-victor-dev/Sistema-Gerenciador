from Script_Banco_Dados import *
from Tela_Login import Tela_Login
from Tela_Auxiliar import Tela_Auxiliar


class Botoes_Navegacao:
    def __init__(self, classe_conteudo_geral, classe_tabela, dict_botoes=None):
        self.classe_conteudo_geral = classe_conteudo_geral
        self.classe_tabela = classe_tabela
        self.dict_botoes = dict_botoes
        self.exibir = Exibir()
        
    def _att_titulo(self, texto_titulo):
        self.classe_conteudo_geral.nome_botao_selecionado.configure(text=texto_titulo)

    def _att_placeholder_barra_pesquisa(self, texto_placeholder):
        self.classe_conteudo_geral.barra_pesquisa.configure(placeholder_text=texto_placeholder)
    
    def _att_qtd_itens(self, tipo_lista):
        if tipo_lista == 'PEDIDOS':
            lista_itens = self.exibir.exibir_pedidos()
        
        elif tipo_lista == 'CLIENTES':
            lista_itens = self.exibir.exibir_clientes()

        elif tipo_lista == 'PRODUTOS':
            lista_itens = self.exibir.exibir_produtos()
        
        elif tipo_lista == 'USUÁRIOS':
            lista_itens = self.exibir.exibir_usuarios()

        total_itens = len(lista_itens)

        self.classe_conteudo_geral.qtd_itens.configure(text=f'{total_itens} Item(ns) cadastrado(s)')

    def _att_tabela(self, nome_tabela):
        for item in self.classe_tabela.corpo_tabela.winfo_children():
            item.destroy()

        if nome_tabela == 'PEDIDOS':
            lista_itens = self.exibir.exibir_pedidos()

            self.classe_tabela._criar_tabela_geral(
                ['ID PEDIDO', 'NOME CLIENTE', 'STATUS', 'TOTAL', 'DATA PEDIDO', 'DATA ALTERAÇÃO'],
                [100, 270, 110, 130, 130, 160],
                lista_itens
            )
        
        elif nome_tabela == 'CLIENTES':
            lista_itens = self.exibir.exibir_clientes()

            self.classe_tabela._criar_tabela_geral(
                ['ID CLIENTE', 'NOME CLIENTE', 'CPF', 'EMAIL', 'TELEFONE'],
                [100, 300, 100, 250, 150],
                lista_itens
            )

        elif nome_tabela == 'PRODUTOS':
            lista_itens = self.exibir.exibir_produtos()

            self.classe_tabela._criar_tabela_geral(
                ['ID PRODUTO', 'DESCRIÇÃO', 'CÓDIGO DE BARRAS', 'PREÇO', 'QUANTIDADE'],
                [120, 300, 200, 150, 130],
                lista_itens
            )

        elif nome_tabela == 'USUÁRIOS':
            lista_itens = self.exibir.exibir_usuarios()

            self.classe_tabela._criar_tabela_geral(
                ['ID USUÁRIO', 'NOME USUÁRIO', 'CPF', 'FUNÇÃO'],
                [150, 300, 150, 300],
                lista_itens
            )

    def _att_estado_visual_botao(self, botao_selecionado):
        from Estilos import Cores

        for botao in self.dict_botoes.values():
            botao.configure(fg_color=Cores.cinza_medio)

        self.dict_botoes[botao_selecionado].configure(fg_color=Cores.cinza_hover)
    
    def _restaurar_botoes_barra_acao(self):
        lista_botoes = self.classe_conteudo_geral.botoes_cad_alt_exc + self.classe_conteudo_geral.botoes_imp_exp

        for botao in lista_botoes:
            botao.destroy()

        self.classe_conteudo_geral._botoes_importar_exportar()
        self.classe_conteudo_geral._botoes_cadastrar_editar_excluir()

    def _desabilitar_botoes_barra_acao(self):
        lista_botoes = self.classe_conteudo_geral.botoes_cad_alt_exc + self.classe_conteudo_geral.botoes_imp_exp

        for botao in lista_botoes:
            botao.configure(command=None)

    def _executar_acoes(self, botao_selecionado):   
        self._restaurar_botoes_barra_acao()
        self._att_estado_visual_botao(botao_selecionado)

        if botao_selecionado == 'PEDIDOS':
            self._att_titulo('PEDIDOS')
            self._att_placeholder_barra_pesquisa('Id do pedido ou nome do cliente')
            self._att_qtd_itens('PEDIDOS')
            self._att_tabela('PEDIDOS')

        elif botao_selecionado == 'CLIENTES':
            self._att_titulo('CLIENTES')
            self._att_placeholder_barra_pesquisa('ID, nome ou CPF do cliente')
            self._att_qtd_itens('CLIENTES')
            self._att_tabela('CLIENTES')

        elif botao_selecionado == 'PRODUTOS':
            self._att_titulo('PRODUTOS')
            self._att_placeholder_barra_pesquisa('ID, descrição ou cód. de barras')
            self._att_qtd_itens('PRODUTOS')
            self._att_tabela('PRODUTOS')

        elif botao_selecionado == 'USUÁRIOS':
            self._att_titulo('USUÁRIOS')
            self._att_placeholder_barra_pesquisa('ID, nome ou CPF do usuário')
            self._att_qtd_itens('USUÁRIOS')
            self._att_tabela('USUÁRIOS')

class Botoes_Area_Usuario:
    def __init__(self, janela_principal):
        self.janela_principal = janela_principal

    def _acao_botao_deslogar(self):
        self.janela_principal.destroy()

        app = Tela_Login()
        app.mainloop()
    
    def _acao_botao_encerrar(self):
        self.janela_principal.destroy()

    def _executar_acao(self, botao_selecionado):
        if botao_selecionado == 'DESLOGAR':
            Tela_Auxiliar(self.janela_principal, True, self._acao_botao_deslogar, texto='Realmente deseja fazer logout?')

        elif botao_selecionado == 'ENCERRAR':
            Tela_Auxiliar(self.janela_principal, True, self._acao_botao_encerrar, texto='Realmente deseja encerrar o programa?')

class Botoes_Barra_Acao(Botoes_Navegacao):
    def __init__(self, janela_principal, classe_conteudo_geral, classe_tabela):
        from Interface import Form_Cadastrar_Item
        from Interface import Form_Alterar_Item
        self.janela_principal = janela_principal
        self.classe_conteudo_geral = classe_conteudo_geral
        self.classe_tabela = classe_tabela
        self.form_cad_item = Form_Cadastrar_Item(janela_principal, classe_tabela)
        self.form_alt_item = Form_Alterar_Item(janela_principal, classe_tabela)
        self.cadastrar = Cadastrar()
        self.alterar = Alterar()
        self.excluir = Excluir()
        self.exibir = Exibir()
        self.id_item_tabela = None
        self.lista_entrys = []
        
    def _selecionar_dado_tabela(self):
        nome_btn_selecionado = self.classe_conteudo_geral.nome_botao_selecionado.cget('text')
        tabela_atual = self.classe_tabela.corpo_tabela.winfo_children()

        tabela = tabela_atual[0]
        item_selecionado = tabela.selection()

        if item_selecionado:  
            valores_item = tabela.item(item_selecionado[0], 'values')
            return nome_btn_selecionado, valores_item
        else:
            Tela_Auxiliar(self.janela_principal, texto='Selecione um dado na lista primeiro!')
            self._restaurar_botoes_barra_acao()
            return None, None
        
    def _selecionar_dado_form(self):
        nome_btn_selecionado = self.classe_conteudo_geral.nome_botao_selecionado.cget('text')

        erros = 0
        lista_retorno = []
 
        for dado in self.lista_entrys:
            item = dado.get()

            if item == '':
                erros += 1
            else:
                lista_retorno.append(item)
        
        if erros > 0:
            Tela_Auxiliar(
                    self.janela_principal,
                    texto='Os campos não podêm estar vazios.', 
                    titulo='ERRO!'
                )
            return None, None
        else:
            return nome_btn_selecionado, lista_retorno

    def _gerar_form_cadastro(self):
        self._desabilitar_botoes_barra_acao()

        nome_btn_selecionado = self.classe_conteudo_geral.nome_botao_selecionado.cget('text')
        lista_entrys = None

        if nome_btn_selecionado == 'PEDIDOS':
            self.form_cad_item._iniciar_form('CADASTRAR PEDIDO', form_pedidos=True)

        elif nome_btn_selecionado == 'CLIENTES':
            lista_entrys = self.form_cad_item._iniciar_form('CADASTRAR CLIENTE', ['NOME','CPF','EMAIL','TELEFONE'])

        elif nome_btn_selecionado == 'PRODUTOS':
            lista_entrys = self.form_cad_item._iniciar_form('CADASTRAR PRODUTO', ['DESCRIÇÃO','CÓDIGO DE BARRAS','PREÇO','QUANTIDADE'])

        elif nome_btn_selecionado == 'USUÁRIOS':
            lista_entrys = self.form_cad_item._iniciar_form('CADASTRAR USUÁRIO', ['NOME','CPF','FUNÇÃO','NOME LOGIN','SENHA'])

        self.lista_entrys.clear()
        self.lista_entrys.extend(lista_entrys) if lista_entrys else None

    def _gerar_form_alt_item(self):
        self._desabilitar_botoes_barra_acao()

        nome_btn_selecionado, valores_tabela = self._selecionar_dado_tabela()
        lista_entrys = None

        if valores_tabela:
            self.id_item_tabela = valores_tabela[0]

        if nome_btn_selecionado == 'PEDIDOS':
            pass
            #self.form_cad_item._iniciar_form('CADASTRAR PEDIDO', form_pedidos=True)

        elif nome_btn_selecionado == 'CLIENTES':
            lista_entrys = self.form_alt_item._iniciar_form_alt_item(valores_tabela[1:], 'ALTERAR CLIENTE', ['NOME','CPF','EMAIL','TELEFONE'])

        elif nome_btn_selecionado == 'PRODUTOS':
            lista_entrys = self.form_alt_item._iniciar_form_alt_item(valores_tabela[1:], 'ALTERAR PRODUTO', ['DESCRIÇÃO','CÓDIGO DE BARRAS','PREÇO','QUANTIDADE'])

        elif nome_btn_selecionado == 'USUÁRIOS':
            lista_entrys = self.form_alt_item._iniciar_form_alt_item(valores_tabela[1:], 'ALTERAR USUÁRIO', ['NOME','CPF','FUNÇÃO','NOME LOGIN','SENHA'])

        self.lista_entrys.clear()
        self.lista_entrys.extend(lista_entrys) if lista_entrys else None
      
    def _limpar_form(self):
        lista_dados = self.form_cad_item.lista_entrys

        for dado in lista_dados:
            dado.delete(0, 'end')

    def _acao_btn_voltar(self):
        nome_btn_selecionado = self.classe_conteudo_geral.nome_botao_selecionado.cget('text')
        self._att_tabela(nome_btn_selecionado)
        self._restaurar_botoes_barra_acao()

    def _acao_cadastrar_dado(self):
        nome_btn_selecionado, valores_form = self._selecionar_dado_form()

        if valores_form and nome_btn_selecionado == 'PEDIDOS':
            pass

        elif valores_form and nome_btn_selecionado == 'CLIENTES':
            tela_aux = Tela_Auxiliar(
                self.janela_principal,
                btn_sim_nao=True, 
                funcao_btn_s=lambda: self.cadastrar.cadastrar_clientes(valores_form[0], valores_form[1], valores_form[2], valores_form[3]), 
                texto='Realmente deseja cadastrar esse CLIENTE?'
            )

            if tela_aux.resultado_funcao_btn_s == 'ERRO INTEGRIDADE':
                Tela_Auxiliar(
                    self.janela_principal,
                    texto='CPF já cadastrado.', 
                    titulo='ERRO!'
                )
            else:
                if tela_aux.botao_sim_pressionado:
                    Tela_Auxiliar(
                        self.janela_principal,
                        texto='CLIENTE cadastrado com sucesso!', 
                        titulo='SUCESSO!'
                    )
                    self._att_qtd_itens('CLIENTES')
                    self._limpar_form()

        elif valores_form and nome_btn_selecionado == 'PRODUTOS':
            tela_aux = Tela_Auxiliar(
                self.janela_principal,
                btn_sim_nao=True, 
                funcao_btn_s=lambda: self.cadastrar.cadastrar_produtos(valores_form[0], valores_form[1], valores_form[2], valores_form[3]), 
                texto='Realmente deseja cadastrar esse PRODUTO?'
            )

            if tela_aux.resultado_funcao_btn_s == 'ERRO INTEGRIDADE':
                Tela_Auxiliar(
                    self.janela_principal,
                    texto='CÓDIGO DE BARRAS já cadastrado.', 
                    titulo='ERRO!'
                )
            else:
                if tela_aux.botao_sim_pressionado:
                    Tela_Auxiliar(
                        self.janela_principal,
                        texto='PRODUTO cadastrado com sucesso!', 
                        titulo='SUCESSO!'
                    )
                    self._att_qtd_itens('PRODUTOS')
                    self._limpar_form()

        elif valores_form and nome_btn_selecionado == 'USUÁRIOS':
            tela_aux = Tela_Auxiliar(
                self.janela_principal,
                btn_sim_nao=True, 
                funcao_btn_s=lambda: self.cadastrar.cadastrar_usuarios(valores_form[0], valores_form[1], valores_form[2], valores_form[3], valores_form[4]),
                texto='Realmente deseja cadastrar esse USUÁRIO?'
            )

            if tela_aux.resultado_funcao_btn_s == 'ERRO INTEGRIDADE':
                Tela_Auxiliar(
                    self.janela_principal,
                    texto='CPF já cadastrado.', 
                    titulo='ERRO!'
                )
            else:
                if tela_aux.botao_sim_pressionado:
                    Tela_Auxiliar(
                        self.janela_principal,
                        texto='USUÁRIO cadastrado com sucesso!', 
                        titulo='SUCESSO!'
                    )
                    self._att_qtd_itens('USUÁRIOS')
                    self._limpar_form()

    def _acao_alterar_dado(self):
        nome_btn_selecionado, valores_form = self._selecionar_dado_form()

        if valores_form and nome_btn_selecionado == 'PEDIDOS':
            pass

        elif valores_form and nome_btn_selecionado == 'CLIENTES':
            tela_aux = Tela_Auxiliar(
                self.janela_principal,
                btn_sim_nao=True, 
                funcao_btn_s=lambda: self.alterar.alterar_clientes(self.id_item_tabela, valores_form[0], valores_form[1], valores_form[2], valores_form[3]),
                texto='Realmente deseja alterar esse CLIENTE?'
            )

            if tela_aux.botao_sim_pressionado:
                Tela_Auxiliar(
                    self.janela_principal,
                    texto='CLIENTE alterado com sucesso!', 
                    titulo='SUCESSO!'
                )
                self._acao_btn_voltar()

        elif valores_form and nome_btn_selecionado == 'PRODUTOS':
            tela_aux = Tela_Auxiliar(
                self.janela_principal,
                btn_sim_nao=True, 
                funcao_btn_s=lambda: self.alterar.alterar_produtos(self.id_item_tabela, valores_form[0], valores_form[1], valores_form[2], valores_form[3]),
                texto='Realmente deseja alterar esse PRODUTO?'
            )

            if tela_aux.botao_sim_pressionado:
                Tela_Auxiliar(
                    self.janela_principal,
                    texto='PRODUTO alterado com sucesso!', 
                    titulo='SUCESSO!'
                )
                self._acao_btn_voltar()

        elif valores_form and nome_btn_selecionado == 'USUÁRIOS':
            tela_aux = Tela_Auxiliar(
                self.janela_principal,
                btn_sim_nao=True, 
                funcao_btn_s=lambda: self.alterar.alterar_usuarios(self.id_item_tabela, valores_form[0], valores_form[1], valores_form[2], valores_form[3], valores_form[4]),
                texto='Realmente deseja alterar esse USUÁRIO?'
            )

            if tela_aux.botao_sim_pressionado:
                Tela_Auxiliar(
                    self.janela_principal,
                    texto='USUÁRIO alterado com sucesso!', 
                    titulo='SUCESSO!'
                )
                self._acao_btn_voltar()

    def _acao_excluir_dado(self):
        nome_btn_selecionado, valores = self._selecionar_dado_tabela()

        if valores and nome_btn_selecionado == 'PEDIDOS':
            tela_aux = Tela_Auxiliar(
                self.janela_principal,
                btn_sim_nao=True, 
                funcao_btn_s=lambda: self.excluir.excluir_pedidos(valores[0]), 
                texto='Realmente deseja excluir esse PEDIDO?'
            )

            if tela_aux.botao_sim_pressionado:
                Tela_Auxiliar(
                    self.janela_principal,
                    texto='PEDIDO excluído com sucesso!', 
                    titulo='SUCESSO!'
                )

            self._att_tabela('PEDIDOS')
            self._att_qtd_itens('PEDIDOS')

        elif valores and nome_btn_selecionado == 'CLIENTES':
            tela_aux = Tela_Auxiliar(
                self.janela_principal,
                btn_sim_nao=True, 
                funcao_btn_s=lambda: self.excluir.excluir_clientes(valores[0]), 
                texto='Realmente deseja excluir esse CLIENTE?'
            )

            if tela_aux.botao_sim_pressionado:
                Tela_Auxiliar(
                    self.janela_principal,
                    texto='CLIENTE excluído com sucesso!', 
                    titulo='SUCESSO!'
                )

            self._att_tabela('CLIENTES')
            self._att_qtd_itens('CLIENTES')

        elif valores and nome_btn_selecionado == 'PRODUTOS':
            tela_aux = Tela_Auxiliar(
                self.janela_principal,
                btn_sim_nao=True, 
                funcao_btn_s=lambda: self.excluir.excluir_produtos(valores[0]), 
                texto='Realmente deseja excluir esse PRODUTO?'
            )

            if tela_aux.botao_sim_pressionado:
                Tela_Auxiliar(
                    self.janela_principal,
                    texto='PRODUTO excluído com sucesso!', 
                    titulo='SUCESSO!'
                )

            self._att_tabela('PRODUTOS')
            self._att_qtd_itens('PRODUTOS')

        elif valores and nome_btn_selecionado == 'USUÁRIOS':
            tela_aux = Tela_Auxiliar(
                self.janela_principal,
                btn_sim_nao=True, 
                funcao_btn_s=lambda: self.excluir.excluir_usuarios(valores[0]), 
                texto='Realmente deseja excluir esse USUÁRIO?'
            )

            if tela_aux.botao_sim_pressionado:
                Tela_Auxiliar(
                    self.janela_principal,
                    texto='USUÁRIO excluído com sucesso!', 
                    titulo='SUCESSO!'
                )

            self._att_tabela('USUÁRIOS')
            self._att_qtd_itens('USUÁRIOS')

    def _aplicar_funcao_barra_pesquisa(self):
        barra_pesquisa = self.classe_conteudo_geral.barra_pesquisa
        barra_pesquisa.bind('<KeyRelease>', lambda evento: self._funcao_barra_pesquisa())

    def _funcao_barra_pesquisa(self):
        botao_selecionado = self.classe_conteudo_geral.nome_botao_selecionado.cget('text')
        texto_digitado = self.classe_conteudo_geral.barra_pesquisa.get().upper()
        itens_tabela = []

        if botao_selecionado == 'PEDIDOS':
            lista_itens = self.exibir.exibir_pedidos()

            for itens in lista_itens:
                if texto_digitado in str(itens[0]) or texto_digitado in itens[1] or texto_digitado in itens[2]:
                    itens_tabela.extend([itens])

            if itens_tabela:
                self.classe_tabela._att_valores_tabela(itens_tabela)
            
            if texto_digitado in ['', ' ', None]:
                self._att_tabela(botao_selecionado)

        elif botao_selecionado == 'CLIENTES':
            lista_itens = self.exibir.exibir_clientes()

            for itens in lista_itens:
                if texto_digitado in str(itens[0]) or texto_digitado in itens[1] or texto_digitado in itens[2]:
                    itens_tabela.extend([itens])

            if itens_tabela:
                self.classe_tabela._att_valores_tabela(itens_tabela)
            
            if texto_digitado in ['', ' ', None]:
                self._att_tabela(botao_selecionado)
        
        elif botao_selecionado == 'PRODUTOS':
            lista_itens = self.exibir.exibir_produtos()

            for itens in lista_itens:
                if texto_digitado in str(itens[0]) or texto_digitado in itens[1] or texto_digitado in itens[2]:
                    itens_tabela.extend([itens])

            if itens_tabela:
                self.classe_tabela._att_valores_tabela(itens_tabela)
            
            if texto_digitado in ['', ' ', None]:
                self._att_tabela(botao_selecionado)

        elif botao_selecionado == 'USUÁRIOS':
            lista_itens = self.exibir.exibir_usuarios()

            for itens in lista_itens:
                if texto_digitado in str(itens[0]) or texto_digitado in itens[1] or texto_digitado in itens[2]:
                    itens_tabela.extend([itens])

            if itens_tabela:
                self.classe_tabela._att_valores_tabela(itens_tabela)
            
            if texto_digitado in ['', ' ', None]:
                self._att_tabela(botao_selecionado)


       