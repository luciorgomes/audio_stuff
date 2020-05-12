#! /usr/bin/python3
# carla_banks.py - Bancos do Carla

from tkinter import *
import tkinter.ttk as ttk
import os

CARLA_FOLDER = '/mnt/HD Externo/Bancos e Patches/Carla/'
CARLA_AMP_FOLDER = '/mnt/HD Externo/Bancos e Patches/Carla/Guitar Amps/'
CARLA_SYNTH_FOLDER = '/mnt/HD Externo/Bancos e Patches/Carla/Instrumentos/'

class App:

    def __init__(self):
        self.root = Tk()
        '''Instancia o Frame com o Listbox com a relação de aplicativos'''
        self.define_raiz()

        # menus
        self.menu = Menu(self.root)
        self.menu_itens = Menu(self.menu, tearoff=0)
        self.menu_itens.add_command(label='Audio Links',  font='Helvetiva 10', command=self.abre_audio_links)
        self.menu_itens.add_command(label='Songs',  font='Helvetiva 10', command=self.abre_songs)
        self.menu.add_cascade(label='Outros', font='Helvetiva 10', menu=self.menu_itens)
        self.root.config(menu=self.menu)

        # create_widgets:
        '''Cria os Listbox e inclui os itens da lista self.choices...'''
        self.frame1=Frame(self.root, bg='#3e0000') ##3877ad
        self.frame1.pack()
        Label(self.frame1, text='Amps', bg='#3e0000', fg='#c2c2c2', font='Arial 11 bold', pady=3).pack()
        self.list_amps = Listbox(self.frame1, width=75, height=11, bg='#31363b', fg='#eff0f1',
                                 highlightbackground='#125487', selectbackground='#125487',
                                 selectforeground='orange')
        self.list_amps.pack(padx=7)
        self.list_amps.bind("<Return>", self.choice_select_amp)  # com um Enter chama a rotina correspondente.
        self.list_amps.bind('<Escape>', self.exit)  # com um Esc encera o programa
        Button(self.frame1, text='Run', command=self.choice_select_amp).pack()
        ttk.Separator(self.frame1, orient=HORIZONTAL).pack(pady=2, fill='x')

        self.frame2=Frame(self.root, bg='#002839')
        self.frame2.pack()
        Label(self.frame2, text='Synth', bg='#002839', fg='#c2c2c2', font='Arial 11 bold', pady=3).pack()
        self.list_synth = Listbox(self.frame2, width=75, height=11, bg='#31363b', fg='#eff0f1',
                                 highlightbackground='#125487', selectbackground='#125487',
                                 selectforeground='orange')
        self.list_synth.pack(padx=7)
        self.list_synth.bind("<Return>", self.choice_select_synth)  # com um Enter chama a rotina correspondente.
        self.list_synth.bind('<Escape>', self.exit)  # com um Esc encera o programa
        Button(self.frame2, text='Run', command=self.choice_select_synth).pack()
        ttk.Separator(self.frame2, orient=HORIZONTAL).pack(pady=2, fill='x')

        self.frame3=Frame(self.root, bg='#202d39')
        self.frame3.pack()
        Label(self.frame3, text='Todos', bg='#202d39', fg='#c2c2c2', font='Arial 11 bold', pady=3).pack()
        self.list_outros = Listbox(self.frame3, width=75, height=14, bg='#31363b', fg='#eff0f1',
                                 highlightbackground='#125487', selectbackground='#125487',
                                 selectforeground='orange')
        self.list_outros.pack(padx=7)
        self.list_outros.bind("<Return>", self.choice_select_outros)  # com um Enter chama a rotina correspondente.
        self.list_outros.bind('<Escape>', self.exit)  # com um Esc encera o programa
        Button(self.frame3, text='Run', command=self.choice_select_outros).pack()
        ttk.Separator(self.frame3, orient=HORIZONTAL).pack(pady=2, fill='x')
        # atualiza list outros
        self.atualiza_listas()

        self.list_amps.select_set(0)
        self.list_amps.focus()  # define o foco para o listbox

        self.root.mainloop()

    def define_raiz(self):
        '''Define caracterísicas da janela'''
        self.root.title('Carla Banks')
        #self.root.iconphoto(False, PhotoImage(file='Python-icon.png'))
        # dimensões da janela
        largura = 620
        altura = 926
        # resolução da tela
        largura_screen = self.root.winfo_screenwidth()
        altura_screen = self.root.winfo_screenheight()
        # posição da janela
        posx = largura_screen / 2 - largura / 2  # meio da tela
        posy = altura_screen / 2 - altura / 2  # meio da primeira tela
        self.root.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))  # dimensões + posição inicial

    def abre_audio_links(self):
        import audio_links
        audio_links.audio_links()

    def abre_songs(self):
        import songs
        songs.songs()

    def atualiza_listas(self):
        list_carla_amp=[]
        for foldername, subfolders, filenames in os.walk(CARLA_AMP_FOLDER):
            for filename in filenames:
                if filename.endswith('.carxp'):
                    list_carla_amp.append(os.path.join(foldername[len(CARLA_AMP_FOLDER):], filename[:-6]))
        list_carla_amp = sorted(list_carla_amp)
        for item in list_carla_amp:
            self.list_amps.insert(END, item)
        list_carla_syn=[]
        for foldername, subfolders, filenames in os.walk(CARLA_SYNTH_FOLDER):
            for filename in filenames:
                if filename.endswith('.carxp'):
                    list_carla_syn.append(os.path.join(foldername[len(CARLA_SYNTH_FOLDER):], filename[:-6]))
        list_carla_syn = sorted(list_carla_syn)
        for item in list_carla_syn:
            self.list_synth.insert(END, item)

        list_carla=[]
        for foldername, subfolders, filenames in os.walk(CARLA_FOLDER):
            for filename in filenames:
                if filename.endswith('.carxp'):
                    list_carla.append(os.path.join(foldername[len(CARLA_FOLDER):], filename[:-6]))
        list_carla = sorted(list_carla)
        for item in list_carla:
            self.list_outros.insert(END, item)

    def choice_select_amp(self, event=None):
        '''Recupera o item selecionado no Listbox e chama o método chama_rotina()'''
        choice_amp = self.list_amps.get(ACTIVE)
        print(f'Executando carla {choice_amp}')
        # self.root.destroy()
        os.system(f"carla '{CARLA_AMP_FOLDER}{choice_amp}.carxp' &")

    def choice_select_synth(self, event=None):
        '''Recupera o item selecionado no Listbox e chama o método chama_rotina()'''
        choice_syn = self.list_synth.get(ACTIVE)
        print(f'Executando carla {choice_syn}')
        # self.root.destroy()
        os.system(f"carla '{CARLA_SYNTH_FOLDER}{choice_syn}.carxp' &")

    def choice_select_outros(self, event=None):
        '''Recupera o item selecionado no Listbox e chama o método'''
        choice = self.list_outros.get(ACTIVE)
        print(f'Executando carla {choice}')
        # self.root.destroy()
        os.system(f"carla '{CARLA_FOLDER}{choice}.carxp' &")


    def exit(self,event=None):
        self.root.destroy()

def carla_banks():
    app = App()

if __name__ == '__main__': # executa se chamado diretamente
   carla_banks()