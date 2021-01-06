#Tarefas


from tkinter import *

#janela 
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