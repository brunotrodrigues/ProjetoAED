from tkinter import *
from tkinter.ttk import Combobox
from tkinter import filedialog
from tkinter import messagebox
import os
import re
import datetime
    
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
    ecra_tarefas.geometry("1000x1000")
    ecra_tarefas.resizable(1,0)

    #Implementar menu
    barra_menu = Menu(ecra_tarefas)
    
    #Menu da consulta das atividades agendadas com diversos filtros
    cons_tafMenu = Menu(barra_menu, tearoff = 0)
    barra_menu.add_cascade(label = "Consultar Tarefas", menu = cons_tafMenu)

    #Menu das tarefas
    tarefaMenu = Menu(barra_menu, tearoff=0)
    tarefaMenu.add_command(label = "Nova tarefa", command = ntarefas)
    tarefaMenu.add_command(label = "Editar tarefa", command = etarefas)
    barra_menu.add_cascade(label = "Tarefas", menu = tarefaMenu)
    
    #Menu de produtividade
    barra_menu.add_command(label = "Produtividade")
    ecra_tarefas.config(menu = barra_menu)

    #Menu da conta do utilizador
    contaMenu = Menu(barra_menu, tearoff = 0)
    contaMenu.add_command(label = "Editar conta")
    contaMenu.add_command(label = "Abrir")
    contaMenu.add_separator()
    contaMenu.add_command(label = "Log out", command = logout)
    barra_menu.add_cascade(label = "Conta", menu = contaMenu)
    
    #frame onde vai aparecer as tarefas
    frame_tarefas = LabelFrame(ecra_tarefas, text = "Tarefas", width = "225", height = "450", relief = "sunken", bd = "2")
    frame_tarefas.place(x=425, y=20)
    
    #frame dos filtros de pesquisa de uma tarefa
    frame_filtros = LabelFrame(ecra_tarefas, text = "Filtros de pesquisa", width = "300", height = "100")
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
    frame_categorias = LabelFrame(ecra_tarefas, text = "Categorias", width = "300", height = "100")
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
    frame_estado = LabelFrame(ecra_tarefas, text = "Estado de tarefa", width = "300", height = "100")
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
    frame_proximas = LabelFrame(ecra_tarefas, text="Próximas Tarefas", width = "300", height = "100")
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

    ecra_tarefas.mainloop()

def logout():
    ecra_tarefas.destroy()

def ntarefas():
    ecra_tarefas.withdraw()
    
    global ecra_ntarefas, newtask_des, ntdes, newtask_cat, ntcat, categoria, einicial, newtask_ei
    categoria = StringVar()
    einicial = StringVar()

    ecra_ntarefas=Tk()
    ecra_ntarefas.title("Nova Tarefas")
    ecra_ntarefas.geometry("1000x1000")
    ecra_ntarefas.resizable(1,0)

    ntdes = StringVar()
    ntcat = StringVar()

    newtask_label_des = Label(ecra_ntarefas, text="Designação:")
    newtask_label_des.place(x=50, y=50)
    newtask_des = Entry(ecra_ntarefas, textvariable=ntdes)
    newtask_des.place(x=120, y=50)

    lista1 = ["Importante", "Trabalho", "Outros", "Pessoal"]

    newtask_label_cat = Label(ecra_ntarefas, text="Categoria:")
    newtask_label_cat.place(x=50, y=100)
    newtask_cat = Combobox(ecra_ntarefas, state="readonly", values=lista1, textvariable=categoria)
    newtask_cat.place(x=120, y=100)

    lista2 = ["Não realizado", "Em desenvolvimento", "Finalizado"]

    newtask_label_ei = Label(ecra_ntarefas, text="Estado inicial:")
    newtask_label_ei.place(x=50, y=150)
    newtask_ei = Combobox(ecra_ntarefas, state="readonly", values=lista2, textvariable=einicial)
    newtask_ei.place(x=130, y=150)

def etarefas():
    
    ecra_tarefas.withdraw()  

    ecra_etarefas=Tk()
    ecra_etarefas.title("Editar Tarefas")
    ecra_etarefas.geometry("1000x1000")
    ecra_etarefas.resizable(1,0)

def notifications():
    
    ecra_popup=Tk()
    ecra_popup.title("Notificações")
    ecra_popup.geometry("200x200")
    ecra_popup.resizable(1,0)

def gerir():
    
    #só admins podem aceder a está pagina

    ecra_gerir=Tk()
    ecra_gerir.title("Gerir")
    ecra_gerir.geometry("1000x1000")
    ecra_gerir.resizable(1,0)


main_account_screen() 