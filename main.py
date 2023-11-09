from tkinter import *

# janela do programa 
janela = Tk()

janela.title("alguem esteve aqui")

class App:
  def __init__ (self): 
    self.janela = janela 
    self.tela()
    self.frames_da_tela()
    self.botoes() 
    self.labels_entrys()
    janela.mainloop()
  
  def tela(self):
    # titulo da janela
    self.janela.title("Boruto uzumaki")

    # cor de fundo da janela
    self.janela.configure(background="#222")

    # tamanho da janela
    self.janela.geometry("700x500")

    # redimencionar a tela horizontal/vertical 
    self.janela.resizable(True, True)

    # minimo que poed redimenconar
    self.janela.minsize(width=400,height=300)

    # maximo que poed redimenconar
    #self.janela.maxsize(width=1280,height=720)

  def frames_da_tela(self):
    self.frame_1 = Frame(self.janela,    
      bd=4,  # criar borda
      bg='#dfe3ee',   # criar frame
      highlightbackground='#759fab',  # cor da borda
      highlightthickness=3,  # espessura da borda
    ) 
    self.frame_1.place(
      relx=0.02,rely=0.02,
      relwidth=0.96, relheight=0.46,
    ) 


    self.frame_2 = Frame(self.janela,    
      bd=4,  # criar borda
      bg='#dfe3ee',   # criar frame
      highlightbackground='#759fab',  # cor da borda
      highlightthickness=3,  # espessura da borda
    ) 
    self.frame_2.place(
      relx=0.02,rely=0.5,
      relwidth=0.96, relheight=0.46,
    ) 

    
  def botoes (self):
    # botao limpar
    self.btn_limpar = Button(self.frame_1, text='Limpar',  
    bd=2,                           #borda do botao
    bg='#107db2',                   # cor do botao 
    fg='white',                     #cor do texto
    font=('verdana',8 ,'bold')      #fonte,tamano do texto
    )
    self.btn_limpar.place(relx=0.2,rely=0.1,relwidth=0.1, relheight=0.15,)  

    # botao buscar
    self.btn_buscar = Button(self.frame_1, text="Buscar",
    bd=2,                           #borda do botao
    bg='#107db2',                   # cor do botao 
    fg='white',                     #cor do texto
    font=('verdana',8 ,'bold')      #fonte,tamano do texto

    )
    self.btn_buscar.place(relx=0.31,rely=0.1,relwidth=0.1, relheight=0.15)

    # Botão de novo
    self.btn_novo = Button(self.frame_1, text='Novo',
    bd=2,                           #borda do botao
    bg='#107db2',                   # cor do botao 
    fg='white',                     #cor do texto
    font=('verdana',8 ,'bold')      #fonte,tamano do texto
    )
    self.btn_novo.place(relx=0.6, rely=0.1,relwidth=0.1, relheight=0.15)

    # Botão de alterar
    self.btn_alterar = Button(self.frame_1, text='Alterar',
    bd=2,                           #borda do botao
    bg='#107db2',                   # cor do botao 
    fg='white',                     #cor do texto
    font=('verdana',8 ,'bold')      #fonte,tamano do texto
    )
    self.btn_alterar.place(relx=0.71, rely=0.1, relwidth=0.1, relheight=0.15)

    # Botão de apagar
    self.btn_apagar = Button(self.frame_1, text='Apagar',
    bd=2,                           #borda do botao
    bg='#107db2',                   # cor do botao 
    fg='white',                     #cor do texto
    font=('verdana',8 ,'bold')      #fonte,tamano do texto
    )
    self.btn_apagar.place(relx=0.82, rely=0.1, relwidth=0.1, relheight=0.15)


  def labels_entrys(self):
    self.lb_codigo = Label(self.frame_1, text='Codigo', bg='#dfe3ee', fg='#107db2')
    self.lb_codigo.place(relx=0.05, rely=0.05)
    self.codigo_entry = Entry(self.frame_1)
    self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)  

    self.lb_nome = Label(self.frame_1, text='Nome', bg='#dfe3ee', fg='#107db2')
    self.lb_nome.place(relx=0.05, rely=0.35)
    self.nome_entry = Entry(self.frame_1)
    self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.87)  

    self.lb_telefone = Label(self.frame_1, text='Telefone', bg='#dfe3ee', fg='#107db2')
    self.lb_telefone.place(relx=0.05, rely=0.65)
    self.telefone_entry = Entry(self.frame_1)
    self.telefone_entry.place(relx=0.05, rely=0.75, relwidth=0.40)  

    self.lb_cidade = Label(self.frame_1, text='Cidade', bg='#dfe3ee', fg='#107db2')
    self.lb_cidade.place(relx=0.52, rely=0.65)
    self.cidade_entry = Entry(self.frame_1)
    self.cidade_entry.place(relx=0.52, rely=0.75, relwidth=0.40) 
 
App()
        