from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import filedialog
from tkinter import messagebox
import os
import re
import datetime
from PIL import Image, ImageTk
    
def registar():
    global ecra_registar 
    
    #registar mesmo utilizador tem que dar erro
    
    ecra_registar = Toplevel(window)
    ecra_registar.title("Registar")
    ecra_registar.geometry("500x500")

    global username, password, email, perfil, username_reg, password_reg, email_reg, perfil_reg
    
    username = StringVar()
    email = StringVar()
    password = StringVar()
    perfil = StringVar()

    #username
    username_reg_label = Label(ecra_registar, text="Username:")
    username_reg_label.place(x=50, y=50)
    username_reg = Entry(ecra_registar, textvariable=username)
    username_reg.place(x=120, y=50)

    #email
    email_reg_label = Label(ecra_registar, text="E-mail:")
    email_reg_label.place(x=50, y=100)
    email_reg = Entry(ecra_registar, textvariable=email)
    email_reg.place(x=120, y=100)

    #password
    password_reg_label = Label(ecra_registar, text="Password:")
    password_reg_label.place(x=50, y=150)
    password_reg = Entry(ecra_registar, textvariable=password, show="*")
    password_reg.place(x=120, y=150)
    
    #user
    perfil_reg_label = Label(ecra_registar, text="Perfil de utilziador:")
    perfil_reg_label.place(x=50, y= 200)
    lista=["User"]
        #adicionar a está lista o "admin" na pagina gerir (Admin = username:admin || password:admin)
    perfil_reg = Combobox(ecra_registar, state="readonly", values=lista, textvariable=perfil)
    perfil_reg.place(x=160, y=200)
    
    Button(ecra_registar, text="Registar", background="skyblue1", command = registar_user).place(x=50, y=250)
    
    Button(ecra_registar, text="Sair", background="skyblue1", command = close_window1).place(x=50, y=300)
    

def close_window1():
    ecra_registar.destroy()

def registar_user():

    username_info = username.get()  
    password_info = password.get()
    email_info = email.get()
    perfil_info = perfil.get()
    
    verificar=email_ver(email_info)

    if verificar==True:    
        messagebox.showinfo("Registo", "Registado com sucesso")
        file = open("utilizadores.txt", "a")
        file.write(username_info + ";")
        file.write(email_info + ";")
        file.write(password_info + ";")
        file.write(perfil_info + ";" + "\n")
        file.close()
    	
        #apagar da entry, combobox
        username_reg.delete(0, END)
        password_reg.delete(0, END)
        email_reg.delete(0, END)
        perfil_reg.delete(0, END)
        
        close_window1()
        login()
    else:
        messagebox.showinfo("Registo", "Registado sem sucesso, tente novamente")
        close_window1()

def email_ver(email_info):
    match = re.search(r"[\w.-]+@[\w.-]+.\w+", email_info)
    if match:
        return True
    else:
        messagebox.showerror("Erro", "E-mail inválido")

def login():
    
    window.destroy()

    global ecra_login, username_ver, password_ver, username_log, password_log #, perfil_log, perfil_ver
    ecra_login = Tk()
    ecra_login.title("Login")
    ecra_login.geometry("300x250")

    username_ver = StringVar()
    password_ver = StringVar()
    #perfil_ver = StringVar()

    username_log_label = Label(ecra_login, text="Username:")
    username_log_label.place(x=50, y=50)
    username_log = Entry(ecra_login, textvariable=username_ver)
    username_log.place(x=120, y=50)
    password_log_label = Label(ecra_login, text="Password:")
    password_log_label.place(x=50, y=100)
    password_log = Entry(ecra_login, textvariable=password_ver, show="*")
    password_log.place(x=120, y=100)

    btn1 = Button(ecra_login, text="Login", background="skyblue1", command = login_ver)
    btn1.place(x=200, y=200)
    
def login_ver():

    user1 = username_ver.get()
    pass1 = password_ver.get()
    #perfil1 = perfil_ver.get()
    username_log.delete(0, END)
    password_log.delete(0, END)
    #perfil_log.delete(0, END)

 
    file = open("utilizadores.txt", "r")
    lista_files = file.read()
    file.close()
    if user1 in lista_files:
        if pass1 in lista_files:
            login_sucess()
        else:
            password_errada()    
    else:
        user_errado()

def login_sucess():
    messagebox.showinfo("Login", "Login realizado com sucesso")
    ecra_login.destroy()

    #perfil = user 
    tarefas_screen()
    #senão
        #gerir

def password_errada():
    messagebox.showinfo("Login", "Password errada")
    ecra_login.destroy()

def user_errado():
    messagebox.showinfo("Login", "Username errado ou inexistente")
    ecra_login.destroy()

def main_account_screen():
    global window
    window=Tk()
    window.geometry("300x250")
    window.title("Login")
    window.configure(background='white')

    btnlogin = Button(text="Login", height="2", width="30", background="skyblue1", command = login)
    btnlogin.place(x=50, y=50)
    btnregistar = Button(text="Registar", height="2", width="30", background="skyblue1", command = registar)
    btnregistar.place(x=50, y=100)

    window.mainloop()

def tarefas_screen():
 
    global ecra_tarefas

    ecra_tarefas=Tk()
    ecra_tarefas.title("Tarefas")
    ecra_tarefas.geometry("800x600")
    ecra_tarefas.resizable(1,0)
    lbl = Label(ecra_tarefas, text = "To-Do List", font = ("Helvetica", 25))
    lbl.place(x=330, y=35)

    canvas_logo = Canvas(ecra_tarefas, width = 420, height = 250, bd = 4, relief = "sunken")
    canvas_logo.place(x=180, y=150)

    img_logo = Image.open("imagens\Abstract Blue Color Digital Particles Wave With Bokeh And Light.jpg")
    img_logo = ImageTk.PhotoImage(img_logo)

    canvas_logo.create_image(0, 0, anchor='nw', image=img_logo)

    #Implementar menu
    barra_menu = Menu(ecra_tarefas)
    
    #Menu da consulta das atividades agendadas com diversos filtros
    barra_menu.add_command(label = "Consultar Tarefas", command= consul_tarefas)
    ecra_tarefas.config(menu= barra_menu)

    #Menu das tarefas
    tarefaMenu = Menu(barra_menu, tearoff=0)
    tarefaMenu.add_command(label = "Nova tarefa", command= ntarefas)
    tarefaMenu.add_command(label = "Editar tarefa", command= etarefas)
    tarefaMenu.add_command(label = "Remover tarefa", command= removtaf)
    barra_menu.add_cascade(label = "Tarefas", menu = tarefaMenu)
    
    #Menu de produtividade
    barra_menu.add_command(label = "Produtividade", command= produt)
    ecra_tarefas.config(menu = barra_menu)

    #Menu da conta do utilizador
    contaMenu = Menu(barra_menu, tearoff = 0)
    contaMenu.add_command(label = "Editar conta", command = edit_conta)
    contaMenu.add_separator()
    contaMenu.add_command(label = "Log out", command = logout)
    barra_menu.add_cascade(label = "Conta", menu = contaMenu)

    ecra_tarefas.mainloop()
def consul_tarefas():
    ecra_tarefas.withdraw() # Fecha window do menu
    global ecra_consul, newtask_des, ntdes, newtask_cat, ntcat, categoria, einicial, newtask_ei

    ecra_consul = Tk()
    ecra_consul.title("Consultar Tarefas")
    ecra_consul.geometry("800x600")
    ecra_consul.resizable(1,0)

    #frame onde vai aparecer as tarefas
    frame_tarefas = LabelFrame( ecra_consul, text = "Tarefas", width = "300", height = "450", relief = "sunken", bd = "2")
    frame_tarefas.place(x=425, y=20)
    lbl_tarefas= Listbox(frame_tarefas, width = 44, height = 25, relief = "sunken", bd = 3)
    lbl_tarefas.place(x=5, y=5)
    
    #frame dos filtros de pesquisa de uma tarefa
    frame_filtros = LabelFrame( ecra_consul, text = "Filtros de pesquisa", width = "300", height = "100")
    frame_filtros.place(x=50, y=20)

    #Filtros de pesquisa
    hoje = StringVar()
    categoria = IntVar()
    ptarefas = IntVar()
    estadotarefas = IntVar()

    check1 = Checkbutton(frame_filtros, text = "Hoje",variable = hoje)
    check1.place(x=15, y=15)

    check2 = Checkbutton(frame_filtros, text = "Por categoria", variable = categoria)
    check2.place(x=145, y=15)

    check3 = Checkbutton(frame_filtros, text = "Próximas tarefas", variable = ptarefas)
    check3.place(x=15, y=45)

    check4 = Checkbutton(frame_filtros, text = "Estado das tarefas", variable = estadotarefas)
    check4.place(x=145, y=45)

    #Frame filtro por categoria
    frame_categorias = LabelFrame( ecra_consul, text = "Categorias", width = "300", height = "100")
    frame_categorias.place(x=50, y=135)

    #Filtros de categoria
    important = IntVar()
    trabalho = IntVar()
    pessoal = IntVar()
    outros = IntVar()

    check5 = Checkbutton(frame_categorias, text = "Importante", variable = important)
    check5.place(x=15, y=15)

    check6 = Checkbutton(frame_categorias, text = "Trabalho", variable = trabalho)
    check6.place(x=145, y=15)

    check7 = Checkbutton(frame_categorias, text = "Pessoal", variable = pessoal)
    check7.place(x=15, y=45)

    check8 = Checkbutton(frame_categorias, text = "Outros", variable = outros)
    check8.place(x=145, y=45)

    #Frame filtro Estado de tarefas
    frame_estado = LabelFrame( ecra_consul, text = "Estado de tarefa", width = "300", height = "100")
    frame_estado.place(x=50,y=250)

    #Filtros de Estado de tarefas
    concluidas = IntVar()
    desenvolvimento = IntVar()
    atraso = IntVar()

    check9 = Checkbutton(frame_estado,text = "Concluídas", variable = concluidas)
    check9.place(x=15, y=15)

    check10 = Checkbutton(frame_estado, text = "Em desenvolvimento", variable = desenvolvimento)
    check10.place(x=145, y=15)

    check11 = Checkbutton(frame_estado, text = "Em atraso", variable = atraso)
    check11.place(x=15, y=45)

    #Frames de filtros de próximas tarefas
    frame_proximas = LabelFrame( ecra_consul, text="Próximas Tarefas", width = "300", height = "100")
    frame_proximas.place(x=50,y=365)

    #Filtros de Próximas Tarefas
    amanha = IntVar()
    esemana = IntVar()
    psemana = IntVar()
    pmes = IntVar()

    check12 = Checkbutton(frame_proximas, text = "Amanhã", variable = amanha)
    check12.place(x=15, y=15)

    check13 = Checkbutton(frame_proximas, text = "Esta semana", variable = esemana)
    check13.place(x=145, y=15)

    check14 = Checkbutton(frame_proximas, text = "Próxima semana", variable = psemana)
    check14.place(x=15, y=45)

    check15 = Checkbutton(frame_proximas, text = "Próximo mês", variable = pmes)
    check15.place(x=145, y=45)

    btn = Button( ecra_consul, text="Voltar", background="skyblue1", command = voltar2)
    btn.place(x=60, y=500)

def voltar2():
    ecra_consul.destroy()
    ecra_tarefas.update()
    ecra_tarefas.deiconify()

def ntarefas():
    ecra_tarefas.withdraw()
    
    global ecra_ntarefas, newtask_des, ntdes, newtask_cat, ntcat, categoria, einicial, newtask_ei
    categoria = StringVar()
    einicial = StringVar()

    ecra_ntarefas=Tk()
    ecra_ntarefas.title("Nova Tarefas")
    ecra_ntarefas.geometry("800x600")
    ecra_ntarefas.resizable(1,0)

    #escrever nova tarefa
    #-----------------Nova Tarefa---------------
    lbl_novatarefa = Label(ecra_ntarefas, text="Tarefa Nova:", font=("Helvetica", 10))
    lbl_novatarefa.place(x=20, y=60)
    text_novatarefa = Text(ecra_ntarefas, width=30, height=3, relief="sunken", bd=2)
    text_novatarefa.place(x=120, y=45)
    #--------------Comentário-------------
    lbl_comentário = Label(ecra_ntarefas, text="Comentário:", font=("Helvetica",10))
    lbl_comentário.place(x=20, y=140)
    text_comentário = Text(ecra_ntarefas, width=30, height=3, relief="sunken", bd=2)
    text_comentário.place(x=120, y=125)
    #------------Combobox------------
    lbl_categoria = Label(ecra_ntarefas, text="Categoria :", font=("Helvetica",10))
    lbl_categoria.place(x=20, y=220)
    cb_categoria = Combobox(ecra_ntarefas, text="Categorias")
    cb_categoria.place(x=120, y=220)
    
    lista2 = ["Não realizado", "Em desenvolvimento", "Finalizado"]

    lbl_estado= Label(ecra_ntarefas, text="Estado inicial:", font=("Helvetica",10))
    lbl_estado.place(x=20, y=260)
    cb_estado = Combobox(ecra_ntarefas, state="readonly", values=lista2, textvariable=einicial)
    cb_estado.place(x=120, y=260)
    #----Adicionar nova tarefa-------
    newcategory= StringVar()

    lbl_nvcategoria= Label(ecra_ntarefas, text=" Nova categoria:", font=("Helvetica",10))
    lbl_nvcategoria.place(x=370,y=220)
    txt_nvcategoria= Entry(ecra_ntarefas, textvariable= newcategory)
    txt_nvcategoria.place(x=470, y=220)
    #------Botão adicionar tarefa----------
    btn_novatarefa = Button(ecra_ntarefas, text="Adicionar tarefa", relief="raised", width=20, height=2, bd=3)
    btn_novatarefa.place(x=60, y=350)

    btn = Button(ecra_ntarefas, text="Voltar", background="skyblue1", command = voltar)
    btn.place(x=110, y=400)

def voltar():
    ecra_ntarefas.destroy()
    ecra_tarefas.update()
    ecra_tarefas.deiconify()
    
def etarefas():
    ecra_tarefas.withdraw()  

    global ecra_etarefas, newtask_des, ntdes, newtask_cat, ntcat, categoria, einicial, newtask_ei
    ecra_etarefas=Tk()
    ecra_etarefas.title("Editar Tarefas")
    ecra_etarefas.geometry("800x600")
    ecra_etarefas.resizable(1,0)

    #Data da tarefa
    lbl_data = Label(ecra_etarefas, text="Data :", font=("Helvetica", 10))
    lbl_data.place(x=20, y=20)
    text_data = Entry(ecra_etarefas)
    text_data.place(x=120, y=20)
    #-----------------Editar Tarefa---------------
    lbl_tarefa = Label(ecra_etarefas, text="Tarefa :", font=("Helvetica", 10))
    lbl_tarefa.place(x=20, y=60)
    text_tarefa = Entry(ecra_etarefas, state="disable")
    text_tarefa.place(x=120, y=60)
    #--------------Comentário-------------
    lbl_comentário = Label(ecra_etarefas, text="Comentário:", font=("Helvetica",10))
    lbl_comentário.place(x=20, y=140)
    text_comentário = Text(ecra_etarefas, width=30, height=3, relief="sunken", bd=2)
    text_comentário.place(x=120, y=125)
    #------------Combobox------------
    lbl_categoria = Label(ecra_etarefas, text="Categoria :", font=("Helvetica",10))
    lbl_categoria.place(x=20, y=220)
    cb_categoria = Combobox(ecra_etarefas, text="Categorias")
    cb_categoria.place(x=120, y=220)
    lbl_estado= Label(ecra_etarefas, text="Estado:", font=("Helvetica",10))
    lbl_estado.place(x=20, y=260)
    cb_estado = Combobox(ecra_etarefas, text="Estado inicial")
    cb_estado.place(x=120, y=260)
    #----Adicionar nova tarefa-------
    newcategory= StringVar()

    lbl_nvcategoria= Label(ecra_etarefas, text=" Nova categoria:", font=("Helvetica",10))
    lbl_nvcategoria.place(x=370,y=220)
    txt_nvcategoria= Entry(ecra_etarefas, textvariable= newcategory)
    txt_nvcategoria.place(x=470, y=220)
    #Atribuir tarefa-----
    lbl_atribuir= Label(ecra_etarefas, text=" Atribuir tarefa:", font=("Helvetica",15))
    lbl_atribuir.place(x=100, y=350)
    lbl_utilizador= Label(ecra_etarefas, text=" Utilizador:", font=("Helvetica",10))
    lbl_utilizador.place(x=20, y=390)
    text_utilizador = Entry(ecra_etarefas, text="")
    text_utilizador.place(x=120, y=390)
    #------Botão adicionar tarefa----------
    btn_edtarefa = Button(ecra_etarefas, text="Editar tarefa", relief="raised", width=20, height=2, bd=3)
    btn_edtarefa.place(x=530, y=400)
    btn_associar = Button(ecra_etarefas, text="Atribuir tarefa", relief="raised", width=20, height=2, bd=3)
    btn_associar.place(x=530, y=450)
    btn = Button(ecra_etarefas, text="Voltar", background="skyblue1", command = voltar1)
    btn.place(x=600, y=500)

def voltar1():
    ecra_etarefas.destroy()
    ecra_tarefas.update()
    ecra_tarefas.deiconify()

def removtaf():
    ecra_tarefas.withdraw()
    global ecra_remover, newtask_des, ntdes, newtask_cat, ntcat, categoria, einicial, newtask_ei
    ecra_remover=Tk()
    ecra_remover.title("Remover Tarefa")
    ecra_remover.geometry("800x600")

    #Categoria da tarefa
    lbl_categoria = Label(ecra_remover, text="Categoria:", font=("Helvetica", 10))
    lbl_categoria.place(x=20, y=20)
    cb_categoria = Combobox(ecra_remover, text="Categorias")
    cb_categoria.place(x=120, y=20)

    #listbox com as tarefas dessa categia
    Frame1 = LabelFrame(ecra_remover, width = 300, height=340, bd="3", relief= "sunken")
    Frame1.place(x= 290, y=80)
    texto = StringVar()#variavel que se vai associar ao componente text
    lbox_tarefas=Listbox(Frame1, width = 43, height = 20, relief = "sunken", bd = 3)
    lbox_tarefas.place(x=5, y=5)
    #remover tarefa
    btn2=Button(ecra_remover, text="Remover", width = 20, height = 2, bd=3, state="active")
    btn2.place(x=40, y=220)
    btn = Button(ecra_remover, text="Voltar", background="skyblue1", command = voltar5)
    btn.place(x=100, y=300)

def voltar5():
    ecra_remover.destroy()
    ecra_tarefas.update()
    ecra_tarefas.deiconify()

def produt():
    ecra_tarefas.withdraw()
    global ecra_produtividade, newtask_des, ntdes, newtask_cat, ntcat, categoria, einicial, newtask_ei
    ecra_produtividade=Tk()
    ecra_produtividade.title("Produtividade")
    ecra_produtividade.geometry("800x600")

    concluias_lb= Label(ecra_produtividade, text="Tarefas concluídas: ")
    concluias_lb.place(x=20, y=20)
    num_concluidas= Entry(ecra_produtividade, text="", width=5, font = ("Helvetica", 12))
    num_concluidas.place(x=130, y=20)
    criadas_lb= Label(ecra_produtividade, text="Tarefas criadas: ")
    criadas_lb.place(x=20, y=55)
    num_criadas= Entry(ecra_produtividade, text="", width=5, font = ("Helvetica", 12))
    num_criadas.place(x=130, y=55)

    btn_estado= Button(ecra_produtividade, text="Nº tarefas por estado", width=18,height=3, font=("Helvetica", "10"))
    btn_estado.place(x=20, y=120)

    btn_categoria= Button(ecra_produtividade, text="Nº tarefas por categoria", width=18,height=3, font=("Helvetica", "10"))
    btn_categoria.place(x=20, y=190)

    btn_semana= Button(ecra_produtividade, text="Nº tarefas por semana", width=18,height=3, font=("Helvetica", "10"))
    btn_semana.place(x=20, y=260)

    btn_mes= Button(ecra_produtividade, text="Nº tarefas por mês", width=18,height=3, font=("Helvetica", "10"))
    btn_mes.place(x=20, y=330)

    #Panel para o nº por estados 
    panel1 = PanedWindow(ecra_produtividade, width=540, height=400, bd="3", relief="sunken")
    panel1.place(x= 220, y=40)

    num_estados= Label(panel1, text="Nº de tarefas por estado", font=("Helvetica", "15"))
    num_estados.place(x=150, y=40)

    tree = ttk.Treeview(panel1, columns = ("Estado", "Nº tarefas"), show = "headings", height = 5, selectmode = "browse")
    tree.column("Estado", width = 200, anchor = "c")
    tree.column("Nº tarefas", width = 200, anchor = "c")
    tree.heading("Estado", text = "Estado")
    tree.heading("Nº tarefas", text = "Nº de tarefas")
    tree.place(x=60, y=140)

    #panel para nº por categoria
    panel2 = PanedWindow(ecra_produtividade, width=540, height=400, bd="3", relief="sunken")
    panel2.place(x= 220, y=40)

    num_categorias= Label(panel2, text="Nº de tarefas por categoria", font=("Helvetica", "15"))
    num_categorias.place(x=150, y=40)

    tree = ttk.Treeview(panel2, columns = ("Categoria", "Nº tarefas"), show = "headings", height = 5, selectmode = "browse")
    tree.column("Categoria", width = 200, anchor = "c")
    tree.column("Nº tarefas", width = 200, anchor = "c")
    tree.heading("Categoria", text = "Categoria")
    tree.heading("Nº tarefas", text = "Nº de tarefas")
    tree.place(x=60, y=140)

    #panel para nº/semana
    panel3 = PanedWindow(ecra_produtividade, width=540, height=400, bd="3", relief="sunken")
    panel3.place(x= 220, y=40)

    num_semana= Label(panel3, text="Nº de tarefas por semana", font=("Helvetica", "15"))
    num_semana.place(x=150, y=40)

    tree = ttk.Treeview(panel3, columns = ("Semana", "Nº tarefas"), show = "headings", height = 5, selectmode = "browse")
    tree.column("Semana", width = 200, anchor = "c")
    tree.column("Nº tarefas", width = 200, anchor = "c")
    tree.heading("Semana", text = "Semana")
    tree.heading("Nº tarefas", text = "Nº de tarefas")
    tree.place(x=60, y=140)

    #panel para nº/mês
    panel4 = PanedWindow(ecra_produtividade, width=540, height=400, bd="3", relief="sunken")
    panel4.place(x= 220, y=40)

    num_mes= Label(panel4, text="Nº de tarefas por mês", font=("Helvetica", "15"))
    num_mes.place(x=150, y=40)

    tree = ttk.Treeview(panel4, columns = ("Mês", "Nº tarefas"), show = "headings", height = 5, selectmode = "browse")
    tree.column("Mês", width = 200, anchor = "c")
    tree.column("Nº tarefas", width = 200, anchor = "c")
    tree.heading("Mês", text = "Mês")
    tree.heading("Nº tarefas", text = "Nº de tarefas")
    tree.place(x=60, y=140)

    btn = Button( ecra_produtividade, text="Voltar", background="skyblue1", command = voltar4)
    btn.place(x=700, y=500)

def voltar4():
    ecra_produtividade.destroy()
    ecra_tarefas.update()
    ecra_tarefas.deiconify()


def edit_conta():
    ecra_tarefas.withdraw()
    global ecra_editconta, newtask_des, ntdes, newtask_cat, ntcat, categoria, einicial, newtask_ei
    ecra_editconta=Tk()
    ecra_editconta.title("Editar Conta")
    ecra_editconta.geometry("600x400")
    ecra_editconta.resizable(1,0)

    canvas_perfil = Canvas(ecra_editconta, width=110, height=120, bd=2, relief = "sunken")
    canvas_perfil.place(x=20, y=20)
    btn3 = Button(ecra_editconta, text="Selecione imagem", width=14, font=("Helvetica", "10"))
    btn3.place(x=20, y=160)


    nome_username_lb = Label(ecra_editconta, text="Username: ")
    nome_username_lb.place(x=180, y=40)
    nome_username = Entry(ecra_editconta, text="", state = "disabled", font = ("Helvetica", "12"))
    nome_username.place(x=300, y=40)

    email_lb= Label(ecra_editconta, text="E-mail: ")
    email_lb.place(x=180, y=80)
    email = Entry(ecra_editconta, text="", state = "disabled", font = ("Helvetica", "12"))
    email.place(x=300, y=80)

    perfil_lb= Label(ecra_editconta, text="Perfil de Utilizador: ")
    perfil_lb.place(x=180, y=120)
    perfil_txt = Entry(ecra_editconta, text="Utilizador", state = "disabled", font = ("Helvetica", "12"))
    perfil_txt.place(x=300, y=120)

    btn_guardar = Button(ecra_editconta, text = "Guardar configurações", width = 20, height = 3)
    btn_guardar.place(x=400, y=270)
    btn_voltar = Button(ecra_editconta, text="Voltar", background="skyblue1", command = voltar3)
    btn_voltar.place(x=505, y=350)

def voltar3():
    ecra_editconta.destroy()
    ecra_tarefas.update()
    ecra_tarefas.deiconify()


def logout():
    ecra_tarefas.destroy()


def notifications():
    
    ecra_popup=Tk()
    ecra_popup.title("Notificações")
    ecra_popup.geometry("200x200")
    ecra_popup.resizable(1,0)


main_account_screen() 