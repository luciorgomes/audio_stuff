#! /usr/bin/python3
# audio_links.py - relação de rotinas

from tkinter import *
import os

class App:
    def __init__(self):
        self.root = Tk()
        '''Instancia o Frame com o Listbox com a relação de aplicativos'''
        self.choices_apps = ['Cadence Logs',
                        'Cadence Jack Meter',
                        'Cadence XY Controller',
                        'Cadence Render'
                        ]
        self.choices_apps = sorted(self.choices_apps)
        self.choices_banks_songs = ['Carla banks',
                        'Sons - Musescore / Ardour / Mixbus',
                        'Sons - Base DB']
        self.choices_banks_songs = sorted(self.choices_banks_songs)

        # create_widgets
        self.frame = Frame(self.root, bg='#2b4970', width=90)
        self.frame.pack()
        Label(self.frame, text='Apps', font='Ubuntu 11 bold', bg='#2b4970').grid(row=0, column=0)
        self.list_box_apps = Listbox(self.frame, width=37, height=25, bg='#31363b', fg='#eff0f1',
                                highlightbackground='#125487', selectbackground='#125487',
                                selectforeground='orange')
        self.list_box_apps.grid(row=1, column=0, padx=5, pady=2)
        for item in self.choices_apps:
            self.list_box_apps.insert(END, item)

        self.list_box_apps.bind("<Double-Button>",
                           self.choice_select_apps)  # com um duplo clique chama a rotina correspondente.
        self.list_box_apps.bind("<Return>", self.choice_select_apps)  # com um Enter chama a rotina correspondente.
        self.list_box_apps.bind('<Escape>', self.exit)  # com um Esc encera o programa

        Label(self.frame, text='Banks / Songs', font='Ubuntu 11 bold', bg='#2b4970').grid(row=0, column=1)
        self.list_box_banks_songs = Listbox(self.frame, width=37, height=25, bg='#31363b', fg='#eff0f1',
                                 highlightbackground='#125487', selectbackground='#125487',
                                 selectforeground='orange')
        self.list_box_banks_songs.grid(row=1, column=1, padx=5, pady=2)
        for item in self.choices_banks_songs:
            self.list_box_banks_songs.insert(END, item)
        self.list_box_banks_songs.bind("<Double-Button>",
                           self.choice_select_banks_songs)  # com um duplo clique chama a rotina correspondente.
        self.list_box_banks_songs.bind("<Return>", self.choice_select_banks_songs)  # com um Enter chama a rotina correspondente.
        self.list_box_banks_songs.bind('<Escape>', self.exit)  # com um Esc encera o programa

        self.list_box_apps.focus()  # define o foco para o listbox
        self.define_raiz()
        self.root.mainloop()

    def define_raiz(self):
        '''Define caracterísicas da janela'''
        self.root.title('Audio Links')
        self.root.resizable(False, False)
        #self.root.iconphoto(False, PhotoImage(file='Python-icon.png'))
        # dimensões da janela
        largura = 620
        altura = 530
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
            print('Executando carla_banks')
            carla_banks.carla_banks()
        elif choice == 'Sons - Musescore / Ardour / Mixbus':
            import songs
            print('Executando songs')
            songs.songs()
        elif choice == 'Sons - Base DB':
            os.system("libreoffice '/mnt/HD Externo/Sons/Sons.odb'")

    def choice_select_apps(self, event):
        '''Recupera o item selecionado no Listbox e chama o método chama_rotina()'''
        self.ch = self.list_box_apps.get(ACTIVE)
        #self.root.destroy()
        self.chama_rotina(self.ch)

    def choice_select_banks_songs(self, event):
        '''Recupera o item selecionado no Listbox e chama o método chama_rotina()'''
        self.ch = self.list_box_banks_songs.get(ACTIVE)
        #self.root.destroy()
        self.chama_rotina(self.ch)

    def exit(self,event=None):
        self.root.destroy()

def audio_links():
    app = App()

if __name__ == '__main__': # executa se chamado diretamente
    audio_links()

