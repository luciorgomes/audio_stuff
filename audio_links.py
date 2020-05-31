#! /usr/bin/python3
# audio_links.py - relação de rotinas

from tkinter import *
import tkinter.font as ft
import os
from dict import apps_dict
from dict import wine_dict


class App:
    def __init__(self):
        self.root = Tk()
        '''Instancia o Frame com o Listbox com a relação de aplicativos'''

        # create_widgets
        # primeira lista
        self.frame = Frame(self.root, bg='#2b4970', width=90)
        self.frame.pack()

        # list_font = ft.Font(family='Noto Sans', size=10, weight=ft.NORMAL)
        list_style = {'width': 29, 'height': 21, 'bg': '#31363b', 'fg': '#eff0f1', 'highlightbackground': '#125487',
                      'selectbackground': '#125487', 'selectforeground': 'orange'}

        Label(self.frame, text='Apps', font='Ubuntu 11 bold',
              bg='#2b4970').grid(row=0, column=0)
        self.list_box_apps = Listbox(self.frame, list_style)
        self.list_box_apps.grid(row=1, column=0, padx=5, pady=2)

        # carrega a lista com as chaves do dicionário
        for key in sorted(apps_dict.keys()):
            self.list_box_apps.insert(END, key)

        Button(self.frame, text='Run', command=self.choice_select_apps).grid(
            row=2, column=0, pady=3)
        # com um duplo clique chama a rotina correspondente.
        self.list_box_apps.bind("<Double-Button-1>", self.choice_select_apps)
        # com um Enter chama a rotina correspondente.
        self.list_box_apps.bind("<Return>", self.choice_select_apps)
        # com um Esc encera o programa
        self.list_box_apps.bind('<Escape>', self.exit)

        # segunda lista
        Label(self.frame, text='Wine', font='Ubuntu 11 bold',
              bg='#2b4970').grid(row=0, column=1)
        self.list_box_wine = Listbox(self.frame, list_style)
        self.list_box_wine.grid(row=1, column=1, padx=5, pady=2)

        for item in sorted(wine_dict.keys()):
            self.list_box_wine.insert(END, item)

        Button(self.frame, text='Run', command=self.choice_select_wine).grid(
            row=2, column=1, pady=3)
        # com um duplo clique chama a rotina correspondente.
        self.list_box_wine.bind("<Double-Button-1>", self.choice_select_wine)
        # com um Enter chama a rotina correspondente.
        self.list_box_wine.bind("<Return>", self.choice_select_wine)
        # com um Esc encera o programa
        self.list_box_wine.bind('<Escape>', self.exit)
        # terceira lista
        Label(self.frame, text='Banks / Songs', font='Ubuntu 11 bold',
              bg='#2b4970').grid(row=0, column=2)
        self.list_box_banks_songs = Listbox(self.frame, list_style)
        self.list_box_banks_songs.grid(row=1, column=2, padx=5, pady=2)

        self.choices_banks_songs = ['Carla banks',
                                    'Helm banks',
                                    'LV2 plugins',
                                    'Sons - Musescore / Ardour / Mixbus',
                                    'Sons - Base DB',
                                    'Rakarrack banks',
                                    'ZynAddSubFX banks']

        for item in sorted(self.choices_banks_songs):
            self.list_box_banks_songs.insert(END, item)

        Button(self.frame, text='Run', command=self.choice_select_banks_songs).grid(
            row=2, column=2, pady=3)
        # com um duplo clique chama a rotina correspondente.
        self.list_box_banks_songs.bind(
            "<Double-Button-1>", self.choice_select_banks_songs)
        # com um Enter chama a rotina correspondente.
        self.list_box_banks_songs.bind(
            "<Return>", self.choice_select_banks_songs)
        # com um Esc encera o programa
        self.list_box_banks_songs.bind('<Escape>', self.exit)

        self.list_box_apps.focus()  # define o foco para o listbox
        self.define_raiz()  # define raiz
        self.root.mainloop()

    def define_raiz(self):
        '''Define caracterísicas da janela'''
        self.root.title('Audio Links')
        self.root.resizable(False, False)
        #self.root.iconphoto(False, PhotoImage(file='Python-icon.png'))
        # dimensões da janela
        largura = 740
        altura = 488
        # resolução da tela
        largura_screen = self.root.winfo_screenwidth()
        altura_screen = self.root.winfo_screenheight()
        # posição da janela
        posx = largura_screen / 2 - largura / 2  # meio da tela
        posy = altura_screen / 2 - altura / 2  # meio da primeira tela
        # dimensões + posição inicial
        self.root.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))

    def choice_select_apps(self, event=None):
        '''Recupera o item selecionado no Listbox e chama o aplicativo'''
        choice = self.list_box_apps.get(ACTIVE)
        # self.root.destroy()
        print(choice)
        os.system(apps_dict[choice] + ' &')  # recupera o comando do dicionário

    def choice_select_wine(self, event=None):
        '''Recupera o item selecionado no Listbox e chama o aplicativo'''
        choice = self.list_box_wine.get(ACTIVE)
        # self.root.destroy()
        print(choice)
        # recupera o comando do dicionário
        os.system("wine '" + wine_dict[choice] + "' &")

    def choice_select_banks_songs(self, event=None):
        '''Recupera o item selecionado no Listbox e chama o banco ou música'''
        choice_b = self.list_box_banks_songs.get(ACTIVE)
        # self.root.destroy()
        if choice_b == 'Carla banks':
            import carla_banks
            print('Executando carla_banks')
            carla_banks.carla_banks()
        elif choice_b == 'Helm banks':
            import helm_banks
            print('Executando helm_banks')
            helm_banks.helm_banks()
        elif choice_b == 'LV2 plugins':
            import lv2_plugins
            print('Executando lv2_plugins')
            lv2_plugins.lv2_plugins()
        elif choice_b == 'Sons - Musescore / Ardour / Mixbus':
            import songs
            print('Executando songs')
            songs.songs()
        elif choice_b == 'Sons - Base DB':
            os.system("libreoffice '/mnt/HD Externo/Sons/Sons.odb' &")
        elif choice_b == 'Rakarrack banks':
            import raka_banks
            print('Rakarrack banks')
            raka_banks.raka_banks()
        elif choice_b == 'ZynAddSubFX banks':
            import zyn_banks
            print('Executando zyn_banks')
            zyn_banks.zyn_banks()

    def exit(self, event=None):
        self.root.destroy()


def audio_links():
    app = App()


if __name__ == '__main__':  # executa se chamado diretamente
    audio_links()
