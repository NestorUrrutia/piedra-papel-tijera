from tkinter import *
from tkinter import ttk, font
import random
from tkinter import messagebox

# Reinicia el tablero
def reinicia():
    partida1_user=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=10,column=1)
    partida2_user=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=10,column=2)
    partida3_user=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=10,column=3)
    partida4_user=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=10,column=4)
    partida5_user=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=10,column=5)
    partida6_user=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=10,column=6)
    partida7_user=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=10,column=7)
    partida8_user=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=10,column=8)
    partida9_user=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=10,column=9)
    partida10_user=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=10,column=10)

    partida1_com=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=11,column=1)
    partida2_com=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=11,column=2)
    partida3_com=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=11,column=3)
    partida4_com=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=11,column=4)
    partida5_com=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=11,column=5)
    partida6_com=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=11,column=6)
    partida7_com=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=11,column=7)
    partida8_com=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=11,column=8)
    partida9_com=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=11,column=9)
    partida10_com=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=11,column=10)


#devuelve quien es el ganador en cada partida
def piedra_papel_tijera(usuario,com):
    #1=piedra / 2=papel / 3=tijera
    #piedra / papel - papel/piedra - tijera/papel
    if(usuario==com):
        messagebox.showinfo(message="empataron", title="Título")
        return 0
    elif ((usuario==1) and (com==3))or((usuario==2) and (com==1))or((usuario==3) and (com==2)):
        messagebox.showinfo(message="ganó USER", title="Ganador")
        return 1
    else:
        messagebox.showinfo(message="Ganó COM", title="Ganador")
        return 2


#muestra la ventana final de quien fue el ganador
def muestraGanador():
    global partidasUsers, partidasCom

    if(partidasUsers>partidasCom):
        messagebox.showinfo(message="YOU WIN!!!!!!!",title="Piedra/Papel/Tijera")
    if(partidasUsers<partidasCom):
        messagebox.showinfo(message="YOU LOSE!!!!!!",title="Piedra/Papel/Tijera")
    if(partidasUsers==partidasCom):
        messagebox.showinfo(message="EMPATE!!!!!",title="Piedra/Papel/Tijera")

#calcula el ganador y rellena el tableto de partida
def calcula_ganador(valor_usuario, valor_com):
    global partidas, partidasUsers,partidasCom

    ganador=piedra_papel_tijera(valor_usuario,valor_com)

    if(partidas==1):
        if(ganador==0):
            partida1_user=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=10,column=1)
            partida1_com=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=11,column=1)
            partidasCom+=1
            partidasUsers+=1
        if(ganador==1):
            partida1_user=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=10,column=1)
            partida1_com=Label(raiz,text="0",borderwidth=1,relief="solid",width=5).grid(row=11,column=1)
            partidasUsers+=1
        if(ganador==2):
            partida1_user=Label(raiz,text="0",borderwidth=1,relief="solid",width=5).grid(row=10,column=1)
            partida1_com=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=11,column=1)
            partidasCom+=1
    if(partidas==2):
        if(ganador==0):
            partida2_user=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=10,column=2)
            partida2_com=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=11,column=2)
            partidasCom+=1
            partidasUsers+=1
        if(ganador==1):
            partida2_user=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=10,column=2)
            partida2_com=Label(raiz,text="0",borderwidth=1,relief="solid",width=5).grid(row=11,column=2)
            partidasUsers+=1
        if(ganador==2):
            partida2_user=Label(raiz,text="0",borderwidth=1,relief="solid",width=5).grid(row=10,column=2)
            partida2_com=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=11,column=2)
            partidasCom+=1
    if(partidas==3):
        if(ganador==0):
            partida3_user=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=10,column=3)
            partida3_com=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=11,column=3)
            partidasCom+=1
            partidasUsers+=1
        if(ganador==1):
            partida3_user=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=10,column=3)
            partida3_com=Label(raiz,text="0",borderwidth=1,relief="solid",width=5).grid(row=11,column=3)
            partidasUsers+=1
        if(ganador==2):
            partida3_user=Label(raiz,text="0",borderwidth=1,relief="solid",width=5).grid(row=10,column=3)
            partida3_com=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=11,column=3)
            partidasCom+=1
    if(partidas==4):
        if(ganador==0):
            partida4_user=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=10,column=4)
            partida4_com=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=11,column=4)
            partidasCom+=1
            partidasUsers+=1
        if(ganador==1):
            partida4_user=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=10,column=4)
            partida4_com=Label(raiz,text="0",borderwidth=1,relief="solid",width=5).grid(row=11,column=4)
            partidasUsers+=1
        if(ganador==2):
            partida4_user=Label(raiz,text="0",borderwidth=1,relief="solid",width=5).grid(row=10,column=4)
            partida4_com=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=11,column=4)
            partidasCom+=1
    if(partidas==5):
        if(ganador==0):
            partida5_user=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=10,column=5)
            partida5_com=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=11,column=5)
            partidasCom+=1
            partidasUsers+=1
        if(ganador==1):
            partida5_user=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=10,column=5)
            partida5_com=Label(raiz,text="0",borderwidth=1,relief="solid",width=5).grid(row=11,column=5)
            partidasUsers+=1
        if(ganador==2):
            partida5_user=Label(raiz,text="0",borderwidth=1,relief="solid",width=5).grid(row=10,column=5)
            partida5_com=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=11,column=5)
            partidasCom+=1
    if(partidas==6):
        if(ganador==0):
            partida6_user=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=10,column=6)
            partida6_com=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=11,column=6)
            partidasCom+=1
            partidasUsers+=1
        if(ganador==1):
            partida6_user=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=10,column=6)
            partida6_com=Label(raiz,text="0",borderwidth=1,relief="solid",width=5).grid(row=11,column=6)
            partidasUsers+=1
        if(ganador==2):
            partida6_user=Label(raiz,text="0",borderwidth=1,relief="solid",width=5).grid(row=10,column=6)
            partida6_com=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=11,column=6)
            partidasCom+=1
    if(partidas==7):
        if(ganador==0):
            partida7_user=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=10,column=7)
            partida7_com=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=11,column=7)
            partidasCom+=1
            partidasUsers+=1
        if(ganador==1):
            partida7_user=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=10,column=7)
            partida7_com=Label(raiz,text="0",borderwidth=1,relief="solid",width=5).grid(row=11,column=7)
            partidasUsers+=1
        if(ganador==2):
            partida7_user=Label(raiz,text="0",borderwidth=1,relief="solid",width=5).grid(row=10,column=7)
            partida7_com=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=11,column=7)
            partidasCom+=1
    if(partidas==8):
        if(ganador==0):
            partida8_user=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=10,column=8)
            partida8_com=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=11,column=8)
            partidasCom+=1
            partidasUsers+=1
        if(ganador==1):
            partida8_user=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=10,column=8)
            partida8_com=Label(raiz,text="0",borderwidth=1,relief="solid",width=5).grid(row=11,column=8)
            partidasUsers+=1
        if(ganador==2):
            partida8_user=Label(raiz,text="0",borderwidth=1,relief="solid",width=5).grid(row=10,column=8)
            partida8_com=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=11,column=8)
            partidasCom+=1
    if(partidas==9):
        if(ganador==0):
            partida9_user=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=10,column=9)
            partida9_com=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=11,column=9)
            partidasCom+=1
            partidasUsers+=1
        if(ganador==1):
            partida9_user=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=10,column=9)
            partida9_com=Label(raiz,text="0",borderwidth=1,relief="solid",width=5).grid(row=11,column=9)
            partidasUsers+=1
        if(ganador==2):
            partida9_user=Label(raiz,text="0",borderwidth=1,relief="solid",width=5).grid(row=10,column=9)
            partida9_com=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=11,column=9)
            partidasCom+=1
    if(partidas==10):
        if(ganador==0):
            partida10_user=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=10,column=10)
            partida10_com=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=11,column=10)
            partidasCom+=1
            partidasUsers+=1
            muestraGanador()
            reinicia()
        if(ganador==1):
            partida10_user=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=10,column=10)
            partida10_com=Label(raiz,text="0",borderwidth=1,relief="solid",width=5).grid(row=11,column=10)
            partidasUsers+=1
            muestraGanador()
            reinicia()
        if(ganador==2):
            partida10_user=Label(raiz,text="0",borderwidth=1,relief="solid",width=5).grid(row=10,column=10)
            partida10_com=Label(raiz,text="1",borderwidth=1,relief="solid",width=5).grid(row=11,column=10)
            partidasCom+=1
            muestraGanador()
            reinicia()

    user_neutro=Label(raiz,image=imagen_neutro).grid(row=3, column=1, rowspan=6, columnspan=4)
    com_nuestro=Label(raiz,image=imagen_neutroCOM).grid(row=3, column=7, rowspan=6, columnspan=4)

#estable la imagen que muestra en ventana.
def tirar(valor_user):
    global partidas
    partidas+=1

    #user
    if (valor_user==1):
        img_user=Label(raiz,image=imagen_piedra)
    elif (valor_user==2):
        img_user=Label(raiz,image=imagen_papel)
    elif (valor_user==3):
        img_user=Label(raiz,image=imagen_tijera)

    img_user.grid(row=3, column=1, rowspan=6, columnspan=4)

    #com
    valor= random.randint(1,3)
    if valor==1:
        img_com=Label(raiz,image=imagen_piedra2)
    elif valor==2:
        img_com=Label(raiz,image=imagen_papel2)
    elif valor==3:
        img_com=Label(raiz,image=imagen_tijera2)

    img_com.grid(row=3, column=7, rowspan=6, columnspan=4)

    calcula_ganador(valor_user,valor)


# VENTANA
# ---------------------------------------------------------------------------------------------

#Conf ventana
raiz = Tk()
raiz.title("Piedra Papel Tijera")
raiz.geometry("500x400")
raiz.resizable(0,0)
raiz.iconbitmap("./img/icono.ico")
raiz.config(bg="#1ABC9C")

#variables globales
partidas=0
partidasUsers=0
partidasCom=0

# Conf USER Y COM
nombre_user=Label(text="USER")
nombre_user.config(bg="#1ABC9C",font=("Arial",14,"bold"))
nombre_user.grid(row=0, column=2, rowspan=2, columnspan=2)

nombre_com=Label(text="COM")
nombre_com.config(bg="#1ABC9C",font=("Arial",14,"bold"))
nombre_com.grid(row=0, column=8, rowspan=2, columnspan=2)

# establece a imagen neutra de ambos jugadores.
imagen_neutro=PhotoImage(file="./img/neutro_user.png")
user_ppt=Label(image=imagen_neutro).grid(row=3, column=1, rowspan=6, columnspan=4)

imagen_neutroCOM=PhotoImage(file="./img/neutro_com.png")
com_ppt=Label(image=imagen_neutroCOM).grid(row=3, column=7, rowspan=6, columnspan=4)

#tablero de partida vacio, solo estructura.
nombre=Label(raiz,text="YOU")
nombre.config(bg="#1ABC9C", font=("Arial",13,"bold"))
nombre.grid(row=10,column=0, pady=10)
partida1_user=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=10,column=1)
partida2_user=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=10,column=2)
partida3_user=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=10,column=3)
partida4_user=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=10,column=4)
partida5_user=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=10,column=5)
partida6_user=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=10,column=6)
partida7_user=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=10,column=7)
partida8_user=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=10,column=8)
partida9_user=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=10,column=9)
partida10_user=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=10,column=10)

com=Label(raiz,text="COM")
com.config(bg="#1ABC9C", font=("Arial",13,"bold"))
com.grid(row=11,column=0, pady=1)
partida1_com=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=11,column=1)
partida2_com=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=11,column=2)
partida3_com=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=11,column=3)
partida4_com=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=11,column=4)
partida5_com=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=11,column=5)
partida6_com=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=11,column=6)
partida7_com=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=11,column=7)
partida8_com=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=11,column=8)
partida9_com=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=11,column=9)
partida10_com=Label(raiz,text="",borderwidth=1,relief="solid",width=5).grid(row=11,column=10)

#imagenes fijas que se muestra al final de la ventana
imagen_piedra_fija=PhotoImage(file="./img/piedra-user.png")
imagen_piedra_fija= imagen_piedra_fija.subsample(2)
piedra=Label(raiz,image=imagen_piedra_fija).grid(row=14, column=0, rowspan=7, columnspan=3)

imagen_papel_fija=PhotoImage(file="./img/papel-user.png")
imagen_papel_fija= imagen_papel_fija.subsample(2)
papel=Label(raiz,image=imagen_papel_fija).grid(row=14, column=4, rowspan=7, columnspan=3)

imagen_tijera_fija=PhotoImage(file="./img/tijera-user.png")
imagen_tijera_fija= imagen_tijera_fija.subsample(2)
tijera=Label(raiz,image=imagen_tijera_fija).grid(row=14, column=8, rowspan=7, columnspan=3,pady=20)

#imagenes de piedra/papel y tijera que son usadas en funciones tanto user como com
imagen_piedra=PhotoImage(file="./img/piedra-usuario.png")
imagen_papel=PhotoImage(file="./img/papel-usuario.png")
imagen_tijera=PhotoImage(file="./img/tijera-usuario.png")

imagen_piedra2=PhotoImage(file="./img/piedra-com.png")
imagen_papel2=PhotoImage(file="./img/papel-com.png")
imagen_tijera2=PhotoImage(file="./img/tijera-com.png")

#botones
btn_piedra=Button(text="Piedra", command=lambda:tirar(1)).grid(row=22, column=1,rowspan=2,columnspan=1)
btn_papel=Button(text="Papel",command=lambda:tirar(2)).grid(row=22, column=5,rowspan=2,columnspan=1)
btn_tijera=Button(text="Tijera",command=lambda:tirar(3)).grid(row=22, column=9,rowspan=2,columnspan=1)

raiz.mainloop()


