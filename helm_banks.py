#! /usr/bin/python3
# helm_banks.py - Bancos do Helm

from tkinter import *
import tkinter.ttk as ttk
import os

HELM_FOLDER = '/mnt/HD Externo/Bancos e Patches/Helm/'
EXTENSAO = '.helm'


class App:

    def __init__(self):
        self.root = Tk()
        '''Instancia o Frame com o Listbox com a relação de aplicativos'''
        self.define_raiz()

        # create_widgets:
        '''Cria os Listbox e inclui os itens da lista self.choices...'''
        self.frame1 = Frame(self.root, bg='#1b7bcf')  # 3877ad
        self.frame1.pack()

        # menus
        self.menu = Menu(self.root)
        self.menu_itens = Menu(self.menu, tearoff=0)
        self.menu_itens.add_command(
            label='Audio Links',  font='Helvetiva 10', command=self.abre_audio_links)
        self.menu.add_cascade(
            label='Outros', font='Helvetiva 10', menu=self.menu_itens)
        self.root.config(menu=self.menu)

        # demais widgets
        Label(self.frame1, text='Helm', bg='#1b7bcf', fg='black', font='Arial 11 bold',
              pady=3).grid(row=0, column=0)
        self.list_helm = Listbox(self.frame1, width=85, height=18, bg='#31363b', fg='#eff0f1',
                                 highlightbackground='#125487', selectbackground='#125487',
                                 selectforeground='orange')
        self.list_helm.grid(row=1, column=0, padx=7)
        # com um Enter chama a rotina correspondente.
        self.list_helm.bind("<Double-Button-1>", self.choice_select_helm)
        # com um Enter chama a rotina correspondente.
        self.list_helm.bind("<Return>", self.choice_select_helm)
        # com um Esc encera o programa
        self.list_helm.bind('<Escape>', self.exit)
        Button(self.frame1, text='Run',
               command=self.choice_select_helm).grid(row=2, column=0)
        ttk.Separator(self.frame1, orient=HORIZONTAL).grid(
            row=3, column=0, columnspan=2, sticky='we')

        self.atualiza_listas()

        self.root.mainloop()

    def define_raiz(self):
        '''Define caracterísicas da janela'''
        self.root.title('Banks')
        self.root.resizable(False, False)
        #self.root.iconphoto(False, PhotoImage(file='Python-icon.png'))
        # dimensões da janela
        largura = 700
        altura = 425
        # resolução da tela
        largura_screen = self.root.winfo_screenwidth()
        altura_screen = self.root.winfo_screenheight()
        # posição da janela
        posx = largura_screen / 2 - largura / 2  # meio da tela
        posy = altura_screen / 2 - altura / 2  # meio da primeira tela
        # dimensões + posição inicial
        self.root.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))

    def abre_audio_links(self):
        import audio_links
        audio_links.audio_links()

    def atualiza_listas(self):
        list = []
        for foldername, subfolders, filenames in os.walk(HELM_FOLDER):
            for filename in filenames:
                if filename.endswith(EXTENSAO):
                    # Nome sem extensão e caminho
                    list.append(os.path.join(
                        foldername[len(HELM_FOLDER):], filename[:-5]))
        list_m = sorted(list)
        for item in list_m:
            self.list_helm.insert(END, item)

    def choice_select_helm(self, event=None):
        '''Recupera o item selecionado no Listbox e chama o método chama_rotina()'''
        choice = self.list_helm.get(ACTIVE)
        print(f'Executando Helm {choice}')
        # self.root.destroy()
        os.system(f"Helm '{HELM_FOLDER}{choice}{EXTENSAO}' &")

    def exit(self, event=None):
        self.root.destroy()


def helm_banks():
    app = App()


if __name__ == '__main__':  # executa se chamado diretamente
    helm_banks()
