from tkinter import *
import codigo
import subprocess

#Acciones de los botones

#Ventana consulta regular
def consultaRegular():
    subprocess.Popen(["python", "viewCR.py"])
    welcome.destroy()
def consultaSintoma():
    subprocess.Popen(["python", "viewCS.py"])
    welcome.destroy()

#Ventana de inicio
welcome = Tk()
welcome.title("Bienvenida")
welcome.resizable(width=False, height=False)  # welcome.resizable(0, 0)
welcome.geometry("900x600")
welcome.config(bg="lightblue",
                cursor="heart")

#Diseño del fondo
fondo = PhotoImage(file="imagenes/fondo.png")
palabra = PhotoImage(file="imagenes/texto.png")
simbolo = PhotoImage(file="imagenes/simbolo.png")
bCR = PhotoImage(file="imagenes/botonCR.png")
bCS = PhotoImage(file="imagenes/botonCS.png")
palabra2 = PhotoImage(file="imagenes/texto2.png")
fondo2 = PhotoImage(file="imagenes/fondo2.png")
sig = PhotoImage(file="imagenes/button_siguiente.png")

canvas = Canvas(welcome,width=900, height=600)
canvas.place(x=0,y=0)
bg = canvas.create_image(450,300, image = fondo)
titulo = canvas.create_image(450,100, image = palabra)
simb =canvas.create_image(450,300, image = simbolo)

#Botones
botonCR = Button(canvas, image=bCR, text="", command = consultaRegular)
botonCR.place(x=70,y=500)
botonCR["border"]="0"

botonCS = Button(canvas,image=bCS ,text="",command = consultaSintoma)
botonCS.place(x=570,y=500)
botonCS["border"]="0"

welcome.mainloop()
