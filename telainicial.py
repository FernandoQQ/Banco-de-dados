from tkinter import *
import sqlite3

class Principal:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")

        self.Container1 = Frame(master)
        self.Container1["pady"] = 10
        self.Container1["bg"] = ("light green")
        self.Container1.pack()

        self.Container2 = Frame(master)
        self.Container2["padx"] = 20
        self.Container2["bg"] = ("light green")
        self.Container2.pack()

        self.Container3 = Frame(master)
        self.Container3["padx"] = 20
        self.Container3["bg"] = ("light green")
        self.Container3.pack()

        self.Container4 = Frame(master)
        self.Container4["pady"] = 20
        self.Container4["bg"] = ("light green")
        self.Container4.pack()

        self.Container5 = Frame(master)
        self.Container5["pady"] = 20
        self.Container5["bg"] = ("light green")
        self.Container5.pack()
####
        self.titulo = Label(self.Container1, text= "Dados do Usuário", font=self.fontePadrao)
        self.titulo["bg"] = ("light green")
        self.titulo.pack()

        self.nomeLabel = Label(self.Container2, text= "Usuário", font=self.fontePadrao)
        self.nomeLabel["bg"] = ("light green")
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.Container2)
        self.nome.focus
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.senhaLabel = Label(self.Container3, text= "Senha  ", font=self.fontePadrao)
        self.senhaLabel["bg"] = ("light green")
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.Container3)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "●"  #simbolo de senha
        self.senha.pack(side=LEFT)

        
        self.autenticar = Button(self.Container4)

        self.autenticar["width"] = 10
        self.autenticar["text"] = "AUTENTICAR"
        self.autenticar["font"] = ("Calibri","10","bold")
        self.autenticar["bg"] = "white"
        self.autenticar["command"] = self.ConsultaUsuario
        self.autenticar.pack()  #botaoautenticarocultado

        self.sair = Button(self.Container4)
        self.sair["width"] = 5
        self.sair["text"] = "SAIR"
        self.sair["font"] = ("Calibri","10","bold")
        self.sair["bg"] = "white"
        self.sair["command"] = quit
        self.sair.pack(side=BOTTOM)
#### BOTOES ####
        self.consultar = Button(self.Container4)
                
        self.consultar["width"] = 10
        self.consultar["text"] = "CONSULTAR"
        self.consultar["font"] = ("Calibri","10","bold")
        self.consultar["bg"] = "white"
        #self.consultar["command"] = self.ConsultarBanco   #comando de consulta
        self.consultar.pack(side=RIGHT)

        self.criar = Button(self.Container4)

        self.criar["text"] = "CRIAR"
        self.criar["font"] = ("Calibri","10","bold")
        self.criar["bg"] = "white"
        self.criar["command"] = self.IncluirUsuario
        self.criar.pack(side=RIGHT)

        self.excluir = Button(self.Container4)

        self.excluir["width"] = 10
        self.excluir["text"] = "EXCLUIR"
        self.excluir["font"] = ("Calibri","10","bold")
        self.excluir["bg"] = "white"
        self.excluir["command"] = self.ExcluirUsuario #excluir usuario
        self.excluir.pack(side=RIGHT)

        self.alterar = Button(self.Container4)

        self.alterar["width"] = 10
        self.alterar["text"] = "ALTERAR"
        self.alterar["font"] = ("Calibri","10","bold")
        self.alterar["bg"] = "white"
        self.alterar.pack(side=RIGHT)
        self.alterar["command"] = self.AlterarUsuario
        
####
        self.mensagem= Label(self.Container5, text= "", font=self.fontePadrao)
        self.mensagem["bg"] = ("light green")
        self.mensagem.pack(side=LEFT)
        
    #Autentica usuário através de consulta ao banco de dados
    def ConsultaUsuario(self):
        conn = sqlite3.connect("empresa.db")

        vnome = self.nome.get()
        vsenha = self.senha.get()

        cursor = conn.cursor()
        cursor.execute('SELECT * FROM usuario WHERE nome = "%s" AND senha = "%s";'% (vnome, vsenha))

        vautentica = 0

        for i in cursor.fetchall():
            self.mensagem["text"] = "AUTENTICADO"
            self.nome["fg"] = "gray"
            self.senha["fg"] = "gray"
            self.sair.focus_force()
            vautentica = 1

        
        if vautentica == 0:
            self.mensagem["text"] = "Usuário e/ou senha inválidos."

### def para incluir
    def  IncluirUsuario(self):
        conn = sqlite3.connect("empresa.db")
        
        vnome = self.nome.get()
        vsenha = self.senha.get()

        cursor = conn.cursor()
        cursor.execute('Insert into usuario (nome, senha) values( "%s", "%s"); ' % (vnome, vsenha))
        conn.commit()

        print("Usuário e senha criados com sucesso.")

        self.mensagem["text"] = "Usuário e senha criado."

#def para excluir
    def ExcluirUsuario(self):
        conn = sqlite3.connect("empresa.db")
        
        vnome = self.nome.get()
        vsenha = self.senha.get()
        
        cursor = conn.cursor()
        cursor.execute('delete FROM usuario WHERE nome=("%s");' %(vnome))
        conn.commit()
        print("Usuário e senha excluídos.")
        self.mensagem["text"] = "Usuário e senha excluídos."

#def para alterar
    def AlterarUsuario(self):
            conn = sqlite3.connect("empresa.db")

            vnome = self.nome.get()
            vsenha = self.senha.get()

            cursor = conn.cursor()
            cursor.execute("UPDATE usuario SET senha = '%s' WHERE nome = '%s';" % (vsenha, vnome))

            conn.commit()
            self.mensagem["text"] = "Usuário e/ou senha alterado(s)."
            print("Dados alterados com sucesso.")
            conn.close()
        
tela = Tk()
tela.title("Tela de Login")
tela["bg"] = ("light green")
tela.geometry("500x280")
Principal(tela)
tela.mainloop()
