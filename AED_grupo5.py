from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import os
import re
    
def registar():
    global ecra_registar 


    #bfnd s,m.<dvbdxc
    
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
    lista=["Admin","User"]
    perfil_reg = Combobox(ecra_registar, state="readonly", values=lista, textvariable=perfil)
    perfil_reg.place(x=160, y=200)
    
    Button(ecra_registar, text="Registar", background="blue", command = registar_user).place(x=50, y=250)
    
    Button(ecra_registar, text="Sair", background="blue", command = close_window1).place(x=50, y=300)
    

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
        messagebox.showinfo("Regsito", "Registado sem sucesso, tente novamente")
        close_window1()

def email_ver(email_info):
    match = re.search(r"[\w.-]+@[\w.-]+.\w+", email_info)
    if match:
        return True
    else:
        messagebox.showerror("Erro", "E-mail inválido")

def login():
    
    global ecra_login, username_ver, password_ver, username_log, password_log
    ecra_login = Toplevel(window)
    ecra_login.title("Login")
    ecra_login.geometry("300x250")

    username_ver = StringVar()
    password_ver = StringVar()

    username_log_label = Label(ecra_login, text="Username:")
    username_log_label.place(x=50, y=50)
    username_log = Entry(ecra_login, textvariable=username_ver)
    username_log.place(x=120, y=50)
    password_log_label = Label(ecra_login, text="Password:")
    password_log_label.place(x=50, y=100)
    password_log = Entry(ecra_login, textvariable=password_ver, show="*")
    password_log.place(x=120, y=100)
    Button(ecra_login, text="Login", background="blue", command = login_ver).place(x=200, y=150)

def login_ver():

    user1 = username_ver.get()
    pass1 = password_ver.get()
    username_log.delete(0, END)
    password_log.delete(0, END)
 
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
    
    #perfil = admin -> pagina gerir || perfil = user -> tarefas
    
    tarefas_screen()

def password_errada():
    messagebox.showinfo("Login", "Password errada")
    ecra_login.destroy()

def user_errado():
    messagebox.showinfo("Login", "Username errado")
    ecra_login.destroy()

def main_account_screen():
    global window
    window=Tk()
    window.geometry("300x250")
    window.title("Login")
    window.configure(background='white')

    Button(text="Login", height="2", width="30", background="blue", command = login).place(x=50, y=50)
    Button(text="Registar", height="2", width="30", background="blue", command = registar).place(x=50, y=100)

    window.mainloop()

def tarefas_screen():
    ecra_tarefas=Tk()
    ecra_tarefas.title("Tarefas")
    ecra_tarefas.geometry("700x500")
    ecra_tarefas.resizable(1,0)
    
    #Implementar menu
    barra_menu = Menu(ecra_tarefas)
    
    #Implementar menu
    barra_menu = Menu(ecra_tarefas)
    #Menu da conta do utilizador
    contaMenu = Menu(barra_menu, tearoff=0)
    contaMenu.add_command(label="Editar conta")
    contaMenu.add_command(label="Abrir")
    contaMenu.add_separator()
    contaMenu.add_command(label="Log out")
    barra_menu.add_cascade(label="Conta", menu=contaMenu)

    #Menu das tarefas
    tarefaMenu = Menu(barra_menu, tearoff=0)
    tarefaMenu.add_command(label="Nova tarefa")
    tarefaMenu.add_command(label="Editar tarefa")
    barra_menu.add_cascade(label="Tarefas", menu= tarefaMenu)
    
    #Menu de produtividade
    barra_menu.add_command(label="Produtividade")

    #Menu da consulta das atividades agendadas com diversos filtros
    cons_tafMenu = Menu(barra_menu, tearoff=0)
    cons_tafMenu.add_command(label="Hoje")
    cons_tafMenu.add_command(label="Por categoria")
    cons_tafMenu.add_command(label="Próximas tarefas")
    cons_tafMenu.add_command(label="Estado das tarefas")
    barra_menu.add_cascade(label="Consultar Tarefas", menu=cons_tafMenu)

    ecra_tarefas.config(menu= barra_menu)
    ecra_tarefas.mainloop()

def Consultar_tarefas():
    ecra_consultartarefas=Tk()
    ecra_consultartarefas.title("Tarefas")
    ecra_consultartarefas.geometry("700x500")
    ecra_consultartarefas.resizable(1,0)

    #frame onde vai aparecer as tarefas
    frame_tarefas = LabelFrame(ecra_consultartarefas, text="Tarefas", width="225", height="450", relief="sunken", bd="2")
    frame_tarefas.place(x=425, y=20)

    #frame dos filtros de pesquisa de uma tarefa
    frame_filtros = LabelFrame(ecra_consultartarefas, text="Filtros de pesquisa", width="300", height="100")
    frame_filtros.place(x=50, y=20)

    #Filtros de pesquisa
    val = IntVar(0)

    check1 = Checkbutton(frame_filtros, text="Hoje", variable=val)
    check1.place(x=15, y=15)

    check2 = Checkbutton(frame_filtros, text="Por categoria", variable=val)
    check2.place(x=145, y=15)

    check3 = Checkbutton(frame_filtros, text="Próximas tarefas", variable=val)
    check3.place(x=15, y=45)

    check4 = Checkbutton(frame_filtros, text="Estado das tarefas", variable=val)
    check4.place(x=145, y=45)

    #Frame filtro por categoria
    frame_categorias = LabelFrame(ecra_consultartarefas, text="Categorias", width="300", height="100")
    frame_categorias.place(x=50, y=135)

    #Filtros de categoria
    val1 = IntVar(0)

    check5 = Checkbutton(frame_categorias, text="Importante", variable=val1)
    check5.place(x=15, y=15)

    check6 = Checkbutton(frame_categorias, text="Trabalho", variable=val1)
    check6.place(x=145, y=15)

    check7 = Checkbutton(frame_categorias, text="Pessoal", variable=val1)
    check7.place(x=15, y=45)

    check8 = Checkbutton(frame_categorias, text="Outros", variable=val1)
    check8.place(x=145, y=45)

    #Frame filtro Estado de tarefas
    frame_estado = LabelFrame(ecra_consultartarefas, text="Estado de tarefa", width="300", height="100")
    frame_estado.place(x=50,y=250)

    #Filtros de Estado de tarefas
    val2 = IntVar(0)

    check9 = Checkbutton(frame_estado,text="Concluídas", variable=val2)
    check9.place(x=15, y=15)

    check10 = Checkbutton(frame_estado, text="Em desenvolvimento", variable=val2)
    check10.place(x=145, y=15)

    check11 = Checkbutton(frame_estado, text="Em atraso", variable=val2)
    check11.place(x=15, y=45)

    #Frames de filtros de próximas tarefas
    frame_proximas = LabelFrame(ecra_consultartarefas, text="Próximas Tarefas", width="300", height="100")
    frame_proximas.place(x=50,y=365)

    #Filtros de Próximas Tarefas
    val3 = IntVar(0)

    check12 = Checkbutton(frame_proximas, text="Amanhã", variable=val3)
    check12.place(x=15, y=15)

    check13 = Checkbutton(frame_proximas, text="Esta semana", variable=val3)
    check13.place(x=145, y=15)

    check14 = Checkbutton(frame_proximas, text="Próxima semana", variable=val3)
    check14.place(x=15, y=45)

    check15 = Checkbutton(frame_proximas, text="Próximo mês", variable=val3)
    check15.place(x=145, y=45)
    ecra_consultartarefas.mainloop()

main_account_screen() 