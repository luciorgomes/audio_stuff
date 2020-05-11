#! /usr/bin/python3
# audio_file.py - relação de rotinas

from tkinter import *
import os

class App:
    def __init__(self):
        self.root = Tk()
        '''Instancia o Frame com o Listbox com a relação de aplicativos'''
        self.choices = ['Cadence Logs',
                        'Cadence Jack Meter',
                        'Cadence XY Controller',
                        'Cadence Render',
                        'Carla banks',
                        'Sons: Musescore - Ardour / Mixbus',
                        'Sons: DB']
        self.choices = sorted(self.choices)
        self.define_raiz()
        self.create_widgets()
        self.root.mainloop()

    def define_raiz(self):
        '''Define caracterísicas da janela'''
        self.root.title('Audio Links')
        #self.root.iconphoto(False, PhotoImage(file='Python-icon.png'))
        # dimensões da janela
        largura = 300
        altura = 500
        # resolução da tela
        largura_screen = self.root.winfo_screenwidth()
        altura_screen = self.root.winfo_screenheight()
        # posição da janela
        posx = largura_screen / 2 - largura / 2  # meio da tela
        posy = altura_screen / 2 - altura / 2  # meio da primeira tela
        self.root.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))  # dimensões + posição inicial

    def chama_rotina(self, choice):
        '''Chama a rotina selecionada no Listbox'''
        print(choice)
        if choice is None:
            print('Tchau!')
        elif choice == 'Cadence Logs':
            os.system('cadence-logs')
        elif choice == 'Cadence Jack Meter':
            os.system('cadence-jackmeter')
        elif choice == 'Cadence XY Controller':
            os.system('cadence-xycontroller')
        elif choice == 'Cadence Render':
            os.system('cadence-render')
        elif choice == 'Cadence Render':
            os.system('cadence-render')
        elif choice == 'Carla banks':
            import carla_banks
            print('Executando carla_banke')
            carla_banks.carla_banks()
        elif choice == 'Sons: Musescore - Ardour / Mixbus':
            import songs
            print('Executando songs')
            songs.songs()
        elif choice == 'Sons: DB':
            os.system("libreoffice '/mnt/HD Externo/Sons/Sons.odb'")

    def choice_select(self, event):
        '''Recupera o item selecionado no Listbox e chama o método chama_rotina()'''
        self.ch = self.list_box.get(ACTIVE)
        self.root.destroy()
        self.chama_rotina(self.ch)


    def create_widgets(self):
        '''Cria o Listbox e inclui os itens da lista self.choices'''
        self.list_box = Listbox(self.root, width=500, height=500, bg='#31363b', fg='#eff0f1',
                                highlightbackground='#125487',selectbackground='#125487',selectforeground='orange')
        self.list_box.pack()
        for item in self.choices:
            self.list_box.insert(END, item)
        self.list_box.select_set(0)
        self.list_box.focus() # define o foco para o listbox
        # self.list_box.bind("<Button>", self.choice_select) # com um duplo clique chama a rotina correspondente.
        self.list_box.bind("<Double-Button>", self.choice_select) # com um duplo clique chama a rotina correspondente.
        self.list_box.bind("<Return>", self.choice_select)  # com um Enter chama a rotina correspondente.
        self.list_box.bind('<Escape>', self.exit) # com um Esc encera o programa

    def exit(self,event=None):
        self.root.destroy()

def audio_file():
    app = App()

if __name__ == '__main__': # executa se chamado diretamente
    audio_file()

