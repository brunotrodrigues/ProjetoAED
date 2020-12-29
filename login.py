from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import os

#coisas que ainda faltam fazer
    #validar e-mail
    #login_ver não funciona direito
    
def registar():
    global ecra_registar 
    
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
    perfil_reg = Combobox(ecra_registar, values=lista, textvariable=perfil)
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
    
    file = open("utilizadores.txt", "a")
    file.write(username_info + ";")
    file.write(email_info + ";")
    file.write(password_info + ";")
    file.write(perfil_info + ";" + "\n")
    file.close()

    #apagar da entry combobox
    username_reg.delete(0, END)
    password_reg.delete(0, END)
    email_reg.delete(0, END)
    perfil_reg.delete(0, END)

    messagebox.showinfo("Regsito", "Registado com sucesso")
    close_window1()

def login():
    
    global ecra_login, username_ver, password_ver, username_log, password_log, email_log, perfil_log
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
 
    lista_files = os.listdir()
    if user1 in lista_files:
        file = open("utilizadores.txt", "r")
        verify = file.read()
        if pass1 in verify:
            login_sucess()
        else:
            password_errada()
    else:
        user_errado()        

def login_sucess():
    messagebox.showinfo("Login", "Login realizado com sucesso")
    ecra_login.destroy()

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


main_account_screen() 