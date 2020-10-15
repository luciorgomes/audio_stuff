#! /usr/bin/python3
# audio_links_db.py - relação de rotinas

from tkinter import *
# import tkinter.font as ft
import os
import sqlite3
# from dict import apps_dict
# from dict import wine_dict


class App:
    def __init__(self, connection):
        self.root = Tk()
        '''Instancia o Frame com o Listbox com a relação de aplicativos'''
        self.cursor = connection.cursor()

        # create_widgets
        # primeira lista
        self.frame = Frame(self.root, bg='#2b4970', width=90)
        self.frame.pack()

        # list_font = ft.Font(family='Noto Sans', size=10, weight=ft.NORMAL)
        list_style = {'width': 30, 'height': 32, 'bg': '#31363b', 'fg': '#eff0f1', 'highlightbackground': '#125487',
                      'selectbackground': '#125487', 'selectforeground': 'orange', 'font': 'Ubuntu 11'}
        self.frame_amps = Frame(self.frame, bg='#2b4970')
        self.frame_amps.grid(row=0, column=0)
        Label(self.frame_amps, text='Apps', font='Ubuntu 12 bold',
              bg='#2b4970').grid(row=0, column=0)
        self.list_box_apps = Listbox(self.frame_amps, list_style)
        self.list_box_apps.grid(row=1, column=0, padx=(5,0), pady=2)
        self.scrollbar_apps = Scrollbar(self.frame_amps, relief=FLAT, bg='#2b4970', width=12, troughcolor='#2b4970')
        self.scrollbar_apps.grid(row=1, column=1, sticky=W + E + N + S)
        self.list_box_apps.config(yscrollcommand=self.scrollbar_apps.set)
        self.scrollbar_apps.config(command=self.list_box_apps.yview)

        # carrega a lista com as chaves do dicionário
        for key in self.cursor.execute('SELECT app FROM audio_links ORDER BY app'):
            self.list_box_apps.insert(END, key[0])

        Button(self.frame_amps, text='Run', command=self.choice_select_apps).grid(
            row=2, column=0, pady=3)
        # com um duplo clique chama a rotina correspondente.
        self.list_box_apps.bind("<Double-Button-1>", self.choice_select_apps)
        # com um Enter chama a rotina correspondente.
        self.list_box_apps.bind("<Return>", self.choice_select_apps)
        # com um Esc encera o programa
        self.list_box_apps.bind('<Escape>', self.exit)

        # segunda lista
        self.frame_wine = Frame(self.frame, bg='#2b4970')
        self.frame_wine.grid(row=0, column=1)
        Label(self.frame_wine, text='Wine', font='Ubuntu 12 bold',
              bg='#2b4970').grid(row=0, column=0)
        self.list_box_wine = Listbox(self.frame_wine, list_style)
        self.list_box_wine.grid(row=1, column=0, padx=(5, 0), pady=2)
        self.scrollbar_wine = Scrollbar(self.frame_wine, relief=FLAT, bg='#2b4970', width=12, troughcolor='#2b4970')
        self.scrollbar_wine.grid(row=1, column=1, sticky=W + E + N + S)
        self.list_box_wine.config(yscrollcommand=self.scrollbar_wine.set)
        self.scrollbar_wine.config(command=self.list_box_wine.yview)

        for key in self.cursor.execute('SELECT app FROM wine_links ORDER BY app'):
            self.list_box_wine.insert(END, key[0])

        Button(self.frame_wine, text='Run', command=self.choice_select_wine).grid(
            row=2, column=0, pady=3)
        # com um duplo clique chama a rotina correspondente.
        self.list_box_wine.bind("<Double-Button-1>", self.choice_select_wine)
        # com um Enter chama a rotina correspondente.
        self.list_box_wine.bind("<Return>", self.choice_select_wine)
        # com um Esc encera o programa
        self.list_box_wine.bind('<Escape>', self.exit)

        # terceira lista
        self.frame_songs = Frame(self.frame, bg='#2b4970')
        self.frame_songs.grid(row=0, column=2)
        Label(self.frame_songs, text='Banks / Songs', font='Ubuntu 12 bold',
              bg='#2b4970').grid(row=0, column=0)
        self.list_box_banks_songs = Listbox(self.frame_songs, list_style)
        self.list_box_banks_songs.grid(row=1, column=0, padx=(5, 0), pady=2)
        self.scrollbar_songs = Scrollbar(self.frame_songs, relief=FLAT, bg='#2b4970', width=12, troughcolor='#2b4970')
        self.scrollbar_songs.grid(row=1, column=1, sticky=W + E + N + S, padx=(0,5))
        self.list_box_banks_songs.config(yscrollcommand=self.scrollbar_songs.set)
        self.scrollbar_songs.config(command=self.list_box_banks_songs.yview)

        self.choices_banks_songs = ['Sons',
                                    'Sons - Base DB',
                                    'Modos - Calc',
                                    'Carla banks',
                                    'Helm banks',
                                    'LV2 plugins',
                                    'Rakarrack banks',
                                    'ZynAddSubFX banks']

        for item in self.choices_banks_songs:
            self.list_box_banks_songs.insert(END, item)

        Button(self.frame_songs, text='Run', command=self.choice_select_banks_songs).grid(
            row=2, column=0, pady=3)
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
        largura = 792
        altura = 645
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
        executable = self.cursor.execute('SELECT exec FROM audio_links WHERE app = ?', (choice,)).fetchone()
        os.system(executable[0] + ' &')  # recupera o comando do dicionário

    def choice_select_wine(self, event=None):
        '''Recupera o item selecionado no Listbox e chama o aplicativo'''
        choice = self.list_box_wine.get(ACTIVE)
        # self.root.destroy()
        print(choice)
        executable = self.cursor.execute('SELECT exec FROM wine_links WHERE app = ?', (choice,)).fetchone()
        # recupera o comando do dicionário
        os.system("wine '" + executable[0] + "' &")

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
        elif choice_b == 'Sons':
            import songs
            print('Executando songs')
            songs.songs()
        elif choice_b == 'Sons - Base DB':
            os.system("libreoffice '/mnt/HD Externo/Sons/Sons.odb' &")
        elif choice_b == 'Modos - Calc':
            os.system("libreoffice '/mnt/HD Externo/home/Documentos/Modos.ods' &")
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
    db = sqlite3.connect("audio.sqlite")
    # db.execute("CREATE TABLE IF NOT EXISTS audio_links (app TEXT PRIMARY KEY NOT NULL, exec TEXT NOT NULL)")
    # db.execute("CREATE TABLE IF NOT EXISTS wine_links (app TEXT PRIMARY KEY NOT NULL, exec TEXT NOT NULL)")
    # for key in sorted(apps_dict.keys()):
    #     print(key, apps_dict[key])
    #     db.execute("INSERT INTO audio_links VALUES(?, ?)", (key, apps_dict[key]))
    # for key in sorted(wine_dict.keys()):
    #     print(key, wine_dict[key])
    #     db.execute("INSERT INTO wine_links VALUES(?, ?)", (key, wine_dict[key]))
    app = App(db)
    # db.commit()
    db.close()



if __name__ == '__main__':  # executa se chamado diretamente
    audio_links()
