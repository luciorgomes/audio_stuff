#! /usr/bin/python3
# zyn_banks.py - Bancos do Helm

from tkinter import *
import tkinter.ttk as ttk
import os
import time

ZYN_FOLDER = '/mnt/HD Externo/Bancos e Patches/Zynaddsubfx/'
EXTENSAO = '.xiz'


class App:

    def __init__(self):
        self.root = Tk()
        '''Instancia o Frame com o Listbox com a relação de aplicativos'''
        self.define_raiz()
        self.recupera_nome_keyboard()
        # create_widgets:
        '''Cria os Listbox e inclui os itens da lista self.choices...'''
        self.frame1 = Frame(self.root, bg='#00818e')  # 3877ad
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
        self.frame_zyn = Frame(self.root, bg='#00818e')
        self.frame_zyn.pack()
        Label(self.frame_zyn, text='ZynAddSubFX', bg='#00818e', fg='black', font='Ubuntu 11 bold',
              pady=3).grid(row=0, column=0)
        style_combo = ttk.Style()
        style_combo.configure('combo.TCombobox', selectforeground='orange', selectbackground='#125487',
                              background='#002839', foreground='black')
        self.dir_combo = ttk.Combobox(
            self.frame_zyn, justify=CENTER, state='readonly', style='combo.TCombobox', width=45)
        self.dir_combo.grid(row=1, column=0)
        self.dir_combo.bind('<<ComboboxSelected>>', self.atualiza_listas_combo)
        self.list_zyn = Listbox(self.frame_zyn,  width=85, height=18, bg='#31363b', fg='#eff0f1',
                                highlightbackground='#125487', selectbackground='#125487',
                                selectforeground='orange', font='Ubuntu 11')
        self.list_zyn.grid(row=2, column=0, padx=(7,0))
        # com um Enter chama a rotina correspondente.
        self.list_zyn.bind("<Double-Button-1>", self.choice_select)
        # com um Enter chama a rotina correspondente.
        self.list_zyn.bind("<Return>", self.choice_select)
        # com um Esc encera o programa
        self.list_zyn.bind('<Escape>', self.exit)
        self.scrollbar = Scrollbar(self.frame_zyn, relief=FLAT, bg='#00818e', width=12, troughcolor='#00818e')
        self.scrollbar.grid(row=2, column=1, sticky=W + E + N + S, padx=(0, 7))
        self.list_zyn.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.list_zyn.yview)
        Button(self.frame_zyn, text='Run',
               command=self.choice_select).grid(row=3, column=0)
        ttk.Separator(self.frame_zyn, orient=HORIZONTAL).grid(
            row=4, column=0, columnspan=2, sticky='we')

        self.atualiza_listas()

        self.root.mainloop()

    def define_raiz(self):
        '''Define caracterísicas da janela'''
        self.root.title('Banks')
        self.root.resizable(False, False)
        #self.root.iconphoto(False, PhotoImage(file='Python-icon.png'))
        # dimensões da janela
        largura = 710
        altura = 407
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
        list, list_dirs = [], []
        for foldername, subfolders, filenames in os.walk(ZYN_FOLDER):
            list_dirs.append(foldername[len(ZYN_FOLDER):])
            for filename in filenames:
                if filename.endswith(EXTENSAO):
                    # Nome sem extensão e caminho
                    list.append(os.path.join(
                        foldername[len(ZYN_FOLDER):], filename[:-4]))
        list_m = sorted(list)
        for item in list_m:
            self.list_zyn.insert(END, item)
        self.dir_combo['values'] = sorted(list_dirs)

    def atualiza_listas_combo(self, event=None):  # atualiza a lista pelo combobox
        list_combo = []
        self.instr_folder = self.dir_combo.get()
        self.list_zyn.delete(0, END)
        for foldername, subfolders, filenames in os.walk(ZYN_FOLDER + self.instr_folder):
            for filename in filenames:
                if filename.endswith(EXTENSAO):
                    list_combo.append(os.path.join(
                        foldername[len(ZYN_FOLDER + self.instr_folder):], filename[:-4]))
        list_combo = sorted(list_combo)
        for item in list_combo:
            self.list_zyn.insert(END, item)

    def recupera_nome_keyboard(self):
        # lê as portas do jack e grava em um arquivo temporário
        os.system("jack_lsp >> lsp")
        with open('lsp', 'r') as ports:
            lsp_ports = ports.read().split('\n')  # gera uma lista
            sub = '(capture): Keystation 49e MIDI 1'  # final do nome da porta
            # localiza o item na lista
            self.midi_port = next((s for s in lsp_ports if sub in s), None)
            os.unlink('lsp')  # deleta o arquivo temporário

    def choice_select(self, event=None):
        '''Recupera o item selecionado no Listbox e chama o método chama_rotina()'''
        choice = self.list_zyn.get(ACTIVE)
        print(f'Executando zynaddsubfx {choice}')
        if self.dir_combo.get():  # se selecionado item do combobox
            os.system(
                f"zynaddsubfx -a -L '{ZYN_FOLDER}{self.dir_combo.get()}/{choice}{EXTENSAO}' &")
            print(
                f"zynaddsubfx -a -L '{ZYN_FOLDER}{self.dir_combo.get()}/{choice}{EXTENSAO}' &")
        else:
            os.system(f"zynaddsubfx -a -L '{ZYN_FOLDER}{choice}{EXTENSAO}' &")
        time.sleep(1)
        os.system(
            f"jack_connect '{self.midi_port}' 'zynaddsubfx:midi_input' &")

    def exit(self, event=None):
        self.root.destroy()


def zyn_banks():
    app = App()


if __name__ == '__main__':  # executa se chamado diretamente
    zyn_banks()
