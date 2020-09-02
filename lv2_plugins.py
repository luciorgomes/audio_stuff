#! /usr/bin/python3
# lv2_plugins.py - Plugins lv2

from tkinter import *
import tkinter.ttk as ttk
import os
import time
import subprocess

class App:

    def __init__(self):
        self.root = Tk()
        '''Instancia o Frame com o Listbox com a relação de aplicativos'''
        self.define_raiz()
        self.lv2_dict ={}
        # self.recupera_nome_keyboard()
        # create_widgets:
        '''Cria os Listbox e inclui os itens da lista self.choices...'''
        self.frame1 = Frame(self.root, bg='#ca7d64')  # 3877ad
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
        self.frame_lv2 = Frame(self.root, bg='#ca7d64')
        self.frame_lv2.pack()
        Label(self.frame_lv2, text='Lv2', bg='#ca7d64', fg='black', font='Ubuntu 11 bold',
              pady=3).grid(row=0, column=0)

        self.list_lv2 = Listbox(self.frame_lv2,  width=85, height=18, bg='#31363b', fg='#eff0f1',
                                highlightbackground='#125487', selectbackground='#125487',
                                selectforeground='orange', font='Ubuntu 11')
        self.list_lv2.grid(row=1, column=0, padx=(7,0))
        # com um Enter chama a rotina correspondente.
        self.list_lv2.bind("<Double-Button-1>", self.choice_select)
        # com um Enter chama a rotina correspondente.
        self.list_lv2.bind("<Return>", self.choice_select)
        # com um Esc encera o programa
        self.list_lv2.bind('<Escape>', self.exit)
        self.scrollbar = Scrollbar(self.frame_lv2, relief=FLAT, bg='#ca7d64', width=12, troughcolor='#ca7d64')
        self.scrollbar.grid(row=1, column=1, sticky=W + E + N + S, padx=(0, 7))
        self.list_lv2.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.list_lv2.yview)
        Button(self.frame_lv2, text='Run',
               command=self.choice_select).grid(row=2, column=0)
        ttk.Separator(self.frame_lv2, orient=HORIZONTAL).grid(
            row=3, column=0, columnspan=2, sticky='we')

        self.atualiza_listas()

        self.root.mainloop()

    def define_raiz(self):
        '''Define caracterísicas da janela'''
        self.root.title('Banks')
        self.root.resizable(False, False)
        #self.root.iconphoto(False, PhotoImage(file='Python-icon.png'))
        # dimensões da janela
        largura = 710
        altura = 385
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
        # recupera o nome do plugin
        lv2_plugins_name = subprocess.run(['lv2ls', '-n'], capture_output=True, text=True)
        # gera uma lista com os nomes
        lv2_names = lv2_plugins_name.stdout.split('\n')
        # recupera a uri do plugin
        lv2_plugins_uri = subprocess.run(['lv2ls'], capture_output=True, text=True)
        # gera uma lista com os uri
        lv2_uri = lv2_plugins_uri.stdout.split('\n')
        # gera um dicionário com nome e uri
        self.lv2_dict = dict(zip(lv2_names, lv2_uri))
        # print(self.lv2_dict)
        for key in sorted(self.lv2_dict.keys()):
             self.list_lv2.insert(END, key)

    def choice_select(self, event=None):
        '''Recupera o item selecionado no Listbox e chama o aplicativo'''
        choice = self.list_lv2.get(ACTIVE)
        # self.root.destroy()
        print(choice)
        os.system('jalv.gtk3 ' + self.lv2_dict[choice] + ' &')  # recupera o comando do dicionário

    def exit(self, event=None):
        self.root.destroy()


def lv2_plugins():
    app = App()


if __name__ == '__main__':  # executa se chamado diretamente
    lv2_plugins()

