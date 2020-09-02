#! /usr/bin/python3
# songs.py - Bancos do Carla

from tkinter import *
# import tkinter.font as ft
import tkinter.ttk as ttk
import os

MUSESCORE_FOLDER = '/mnt/HD Externo/Musescore/'
ARDOUR_FOLDER = '/mnt/HD Externo/Projetos/'


class App:

    def __init__(self):
        self.root = Tk()
        '''Instancia o Frame com o Listbox com a relação de aplicativos'''
        self.define_raiz()

        # create_widgets:
        '''Cria os Listbox e inclui os itens da lista self.choices...'''
        self.frame1 = Frame(self.root, bg='#2b355a')  # 3877ad
        self.frame1.pack()

        # menus
        self.menu = Menu(self.root)
        self.menu_itens = Menu(self.menu, tearoff=0)
        self.menu_itens.add_command(
            label='Audio Links',  font='Helvetiva 10', command=self.abre_audio_links)
        self.menu_itens.add_command(
            label='Carla Banks',  font='Helvetiva 10', command=self.abre_carla_banks)
        self.menu.add_cascade(
            label='Outros', font='Helvetiva 10', menu=self.menu_itens)
        self.root.config(menu=self.menu)

        # demais widgets
        Label(self.frame1, text='Musescore', bg='#2b355a', fg='#c2c2c2', font='Ubuntu 11 bold',
              pady=3).grid(row=0, column=0, columnspan=2)

        # list_font = ft.Font(family='Noto Sans', size=10, weight=ft.NORMAL)
        list_style = {'width': 85, 'height': 18, 'bg': '#31363b', 'fg': '#eff0f1', 'highlightbackground': '#125487',
                      'selectbackground': '#125487', 'selectforeground': 'orange', 'font':'Ubuntu 11'}

        self.list_muse = Listbox(self.frame1, list_style)
        self.list_muse.grid(row=1, column=0, padx=(7,0))
        # com um Enter chama a rotina correspondente.
        self.list_muse.bind("<Double-Button-1>", self.choice_select_muse)
        # com um Enter chama a rotina correspondente.
        self.list_muse.bind("<Return>", self.choice_select_muse)
        # com um Esc encera o programa
        self.list_muse.bind('<Escape>', self.exit)
        self.scrollbar_muse = Scrollbar(self.frame1, relief=FLAT, bg='#2b355a', width=12, troughcolor='#2b355a')
        self.scrollbar_muse.grid(row=1, column=1, sticky=W+E+N+S, padx=(0, 7))
        self.list_muse.config(yscrollcommand=self.scrollbar_muse.set)
        self.scrollbar_muse.config(command=self.list_muse.yview)
        Button(self.frame1, text='Run',
               command=self.choice_select_muse).grid(row=2, column=0, columnspan=2)
        ttk.Separator(self.root, orient=HORIZONTAL).pack(fill=BOTH, pady=(3,0))

        self.frame2 = Frame(self.root, bg='#3d3d3d')
        self.frame2.pack()
        Label(self.frame2, text='Ardour / Mixbus', bg='#3d3d3d', fg='#c2c2c2', font='Ubuntu 11 bold',
              pady=3).grid(row=0, column=0, columnspan=2, pady=(3,0))
        self.list_ard_mix = Listbox(self.frame2, list_style)
        self.list_ard_mix.grid(row=1, column=0, padx=(7, 0))
        # com um Enter chama a rotina correspondente.
        self.list_ard_mix.bind("<Double-Button-1>", self.choice_select_mixbus)
        # com um Enter chama a rotina correspondente.
        self.list_ard_mix.bind("<Return>", self.choice_select_mixbus)
        # com um Esc encera o programa
        self.list_ard_mix.bind('<Escape>', self.exit)
        self.scrollbar_ard_mix = Scrollbar(self.frame2, relief=FLAT, bg='#3d3d3d', width=12, troughcolor='#3d3d3d')
        self.scrollbar_ard_mix.grid(row=1, column=1, sticky=W + E + N + S, padx=(0, 7))
        self.list_ard_mix.config(yscrollcommand=self.scrollbar_ard_mix.set)
        self.scrollbar_ard_mix.config(command=self.list_ard_mix.yview)
        self.frame3 = Frame(self.root, bg='#3d3d3d')
        self.frame3.pack(fill=BOTH, expand=1)
        Button(self.frame3, text='Run Ardour',
               command=self.choice_select_ardour).grid(row=0, column=0, sticky=E, padx=129)
        Button(self.frame3, text='Run Mixbus',
               command=self.choice_select_mixbus).grid(row=0, column=1, sticky=W, padx=129)
        ttk.Separator(self.frame3, orient=HORIZONTAL).grid(
            row=3, column=0, columnspan=2, sticky='we', pady=(3,0))

        self.atualiza_listas()

        self.root.mainloop()

    def define_raiz(self):
        '''Define caracterísicas da janela'''
        self.root.title('Sons')
        self.root.resizable(False, False)
        #self.root.iconphoto(False, PhotoImage(file='Python-icon.png'))
        # dimensões da janela
        largura = 710
        altura = 780
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

    def abre_carla_banks(self):
        import carla_banks
        carla_banks.carla_banks()

    def atualiza_listas(self):
        list_m = []
        for foldername, subfolders, filenames in os.walk(MUSESCORE_FOLDER):
            for filename in filenames:
                if filename.endswith('.mscz'):
                    # Nome sem extensão e caminho
                    list_m.append(os.path.join(
                        foldername[len(MUSESCORE_FOLDER):], filename[:-5]))
        list_m = sorted(list_m)
        for item in list_m:
            self.list_muse.insert(END, item)

        list_ar_mix = []
        for foldername, subfolders, filenames in os.walk(ARDOUR_FOLDER):
            for filename in filenames:
                if filename.endswith('.ardour'):
                    list_ar_mix.append(os.path.join(
                        foldername[len(ARDOUR_FOLDER):], filename[:-7]))
        list_ar_mix = sorted(list_ar_mix)
        for item in list_ar_mix:
            self.list_ard_mix.insert(END, item)

    def choice_select_muse(self, event=None):
        '''Recupera o item selecionado no Listbox e chama o método chama_rotina()'''
        choice_muse = self.list_muse.get(ACTIVE)
        print(f'Executando musescore {choice_muse}')
        # self.root.destroy()
        os.system(f"env BAMF_DESKTOP_FILE_HINT="
                  f"/var/lib/snapd/desktop/applications/musescore_musescore.desktop "
                  f"/snap/bin/musescore.mscore '{MUSESCORE_FOLDER}{choice_muse}.mscz' &")

    def choice_select_ardour(self, event=None):
        '''Recupera o item selecionado no Listbox e chama o método chama_rotina()'''
        choice_ard = self.list_ard_mix.get(ACTIVE)
        print(f'Executando ardour {choice_ard}')
        # self.root.destroy()
        os.system(f"ardour '{ARDOUR_FOLDER}{choice_ard}.ardour' &")

    def choice_select_mixbus(self, event=None):
        '''Recupera o item selecionado no Listbox e chama o método'''
        choice_mix = self.list_ard_mix.get(ACTIVE)
        print(f'Executando mixbus {choice_mix}')
        # self.root.destroy()
        os.system(f"Mixbus6 '{ARDOUR_FOLDER}{choice_mix}.ardour' &")

    def exit(self, event=None):
        self.root.destroy()


def songs():
    app = App()


if __name__ == '__main__':  # executa se chamado diretamente
    songs()
