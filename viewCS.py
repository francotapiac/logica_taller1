from tkinter import *
import codigo
import subprocess


#Datos de back-end
preguntas = codigo.listaPreguntas()
fumador = codigo.listaFumador()
viejo = codigo.listaViejo()
joven = codigo.listaJoven()
sobrepeso = codigo.listaSobrePeso()
sinFactores = list(range(0,31))
sintomas = codigo.listaSimtomas()

#Datos actuales globales
edad=25
fuma=0
sobrepesoT=0
viejoT=0
jovenT=1
finalPreguntas = []

#Preguntas a realizar
textPreguntas = []

#Acion boton pregunta
indicePregunta = 0

#Sintomas confirmados
listaConfirmados = []

#sintomas no confirmados
listaNoConfirmados = []


#Accion aumentar edad

'''def sumar():
    global edad
    global edadC 
    canvas.delete(edadC)
    edad = edad + 1
    if edad > 99:
        edad = 99
    edadC = canvas.create_text(620,200,text = edad, font = ("Roboto",28, "bold"), fill="MediumOrchid3")'''

#Acccion disminuir edad
'''def restar():
    global edad
    global edadC 
    canvas.delete(edadC)
    edad = edad -  1
    if edad < 0:
        edad = 0
    edadC = canvas.create_text(620,200,text = edad, font = ("Roboto",28, "bold"), fill="MediumOrchid3")'''

#Checkbutton Configuracion
'''def setBoxF(event):
    global fuma
    global boxF
    canvas.delete(boxF)

    if fuma == 1:
        fuma = 0
        boxF = canvas.create_image(620,290,image=ino)
        canvas.tag_bind(boxF,"<Button-1>",setBoxF)
    else:
        fuma = 1
        boxF = canvas.create_image(620,290,image=isi)
        canvas.tag_bind(boxF,"<Button-1>",setBoxF)'''

#Checkbutton Configuracion
'''def setBoxS(event):
    global sobrepesoT
    global boxS
    canvas.delete(boxS)
    if sobrepesoT == 1:
        sobrepesoT = 0
        boxS = canvas.create_image(620,380,image=ino)
        canvas.tag_bind(boxS,"<Button-1>",setBoxS)
    else:
        sobrepesoT = 1
        boxS = canvas.create_image(620,380,image=isi)
        canvas.tag_bind(boxS,"<Button-1>",setBoxS)'''

#Lista de preguntas
'''def siguiente():
    canvas.delete("all")
    global finalPreguntas
    global textPreguntas
    global jovenT
    global viejoT
    global botonSig
    global mas
    global menos
    global bg
    global titulo
    global frame
    #global canvas2
    global label

    mas.place_forget()
    menos.place_forget()
    botonSig.place_forget()

    bg = canvas.create_image(450,300, image = fondo)
    titulo = canvas.create_image(450,50, image = tPregunta)

    botonSi.place(x=200,y=500)
    botonNo.place(x=570,y=500)

    frame.place(x=100,y = 80)
    #canvas2.place(x=0,y=0)

    #label.place(x=0,y=0)
    

    if edad >= 65:
        jovenT = 0
        viejoT = 1
    if (sobrepesoT + fuma) == 2 and jovenT == 1:
        finalPreguntas = codigo.mixOrder(fumador, codigo.mixOrder(joven, sobrepeso))
    elif (sobrepesoT + fuma) == 2 and viejoT == 1:
        finalPreguntas = codigo.mixOrder(fumador, codigo.mixOrder(viejo, sobrepeso))
    elif (sobrepesoT + fuma) == 1 and jovenT == 1:
        if sobrepesoT == 1:
            finalPreguntas = codigo.mixOrder(joven, sobrepeso)
        if fuma == 1:
            finalPreguntas = codigo.mixOrder(joven, fumador)
    elif (sobrepesoT + fuma) == 1 and viejoT == 1:
        if sobrepesoT == 1:
            finalPreguntas = codigo.mixOrder(viejo, sobrepeso)
        if fuma == 1:
            finalPreguntas = codigo.mixOrder(viejo, fumador)
    elif (sobrepesoT + fuma) == 0 and jovenT == 1:
        finalPreguntas = joven
    elif (sobrepesoT + fuma) == 0 and viejoT == 1:
        finalPreguntas = viejo
    
    for pos in finalPreguntas:
        textPreguntas.append(preguntas[pos])

    #label = canvas2.create_text(300,50,text = textPreguntas[indicePregunta], font = ("Roboto",15, "bold"))
    label.place(x=0,y=0)
    label["text"] = textPreguntas[indicePregunta]'''
    
    
def respuestaSi():
    global indicePregunta
    global textPreguntas
    global listaConfirmados
    global listaNoConfirmados
    global label
    global bg
    global titulo
    
    if (len(textPreguntas)-1) == indicePregunta:
        enfermedades = codigo.getEnfermedades(listaConfirmados,listaNoConfirmados)
        respuesta = "Se detectaron las siguientes enfermedades:\n"
        canvas.delete(bg)
        canvas.delete(titulo)
        bg = canvas.create_image(450,300, image = fondo3)
        titulo = canvas.create_image(450,50, image = palabra2)
        if len(enfermedades) == 0:
            label["text"] = "Lo sentimos, no hemos detectado tu posible enfermedad. Le recomendamos visitar un medico"
            botonNo.place_forget()
            botonSi.place_forget()
            botonFin.place(x=390,y=500)
        else:
            for enfermedad in enfermedades:
                respuesta+="*"+enfermedad+"\n"
            respuesta+="Se le recomienda ir al medico para más detalles"
            label.place_forget()
            label3 = Label(frame, text="", font= ("Roboto",15), width =73,anchor = "nw", justify="left" ,bg="lavender",wraplength=685,padx=15)
            label3.place(x=0,y=50)
            label3["text"] = respuesta
    else:
        pos = finalPreguntas[indicePregunta]
        listaConfirmados.append(sintomas[pos])
        indicePregunta+=1
        label["text"] = textPreguntas[indicePregunta]

def respuestaNo():
    global indicePregunta
    global textPreguntas
    global label
    global label3
    global listaNoConfirmados
    global listaConfirmados
    global finalPreguntas
    global bg
    global titulo

    if (len(textPreguntas)-1) == indicePregunta:
        enfermedades = codigo.getEnfermedades(listaConfirmados,listaNoConfirmados)
        respuesta = "Se detectaron las siguientes enfermedades:\n"
        canvas.delete(bg)
        canvas.delete(titulo)
        bg = canvas.create_image(450,300, image = fondo3)
        titulo = canvas.create_image(450,50, image = palabra2)
        if len(enfermedades) == 0:
            label["text"] = "Lo sentimos, no hemos detectado tu posible enfermedad. Le recomendamos visitar un medico"
            botonNo.place_forget()
            botonSi.place_forget()
            botonFin.place(x=390,y=500)
        else:
            for enfermedad in enfermedades:
                respuesta+="*"+enfermedad+"\n"
            respuesta+="Se le recomienda ir al medico para más detalles"
            label.place_forget()
            label3 = Label(frame, text="", font= ("Roboto",15), width =73,anchor = "nw", justify="left" ,bg="lavender",wraplength=685,padx=15)
            label3.place(x=0,y=50)
            label3["text"] = respuesta
                
        
    else:
        pos = finalPreguntas[indicePregunta]
        listaNoConfirmados.append(sintomas[pos])
        indicePregunta+=1
        label["text"] = textPreguntas[indicePregunta]

def finPreguntas():
    subprocess.Popen(["python", "viewMain.py"])
    welcome.destroy()

def tratamiento(lista):
    global bg
    global titulo
    canvas.delete(bg)
    canvas.delete(titulo)
    bg = canvas.create_image(450,300, image = fondo3)
    titulo = canvas.create_image(450,50, image = palabra2)
    enfermedad = lista[0]
    label2 = Label(frame, text="", font= ("Roboto",20, "bold"), width =34 ,anchor = "n", justify="center" ,bg="lavender",wraplength=685)
    label2.place(x=0,y=0)
    label2["text"] = enfermedad

    label3 = Label(frame, text="", font= ("Roboto",10), width =73,anchor = "nw", justify="left" ,bg="lavender",wraplength=685,padx=15)
    label3.place(x=0,y=50)
    label3["text"] = codigo.getTratamiento(enfermedad)
    
    label.place_forget()
    botonNo.place_forget()
    botonSi.place_forget()
    botonFin.place(x=390,y=500)
    

#Ventana de inicio
welcome = Tk()
welcome.title("Consulta Regular")
welcome.resizable(width=False, height=False)  # welcome.resizable(0, 0)
welcome.geometry("900x600")
welcome.config(bg="lightblue",
                cursor="heart")

#Diseño del fondo
palabra = PhotoImage(file="imagenes/titulo2.png")
tPregunta = PhotoImage(file="imagenes/sintomas.png")
fondo = PhotoImage(file="imagenes/fondo.png")
fondo3 = PhotoImage(file="imagenes/fondo2.png")
sig = PhotoImage(file="imagenes/siguiente.png")
iedad = PhotoImage(file="imagenes/edad.png")
ifuma = PhotoImage(file="imagenes/fuma.png")
isobrepeso = PhotoImage(file="imagenes/sobrepeso.png")
isi = PhotoImage(file="imagenes/si3.png")
ino = PhotoImage(file="imagenes/no3.png")
imas = PhotoImage(file="imagenes/mas.png")
imenos = PhotoImage(file="imagenes/menos.png")
imagenSi = PhotoImage(file="imagenes/button_si.png")
imagenNo = PhotoImage(file="imagenes/button_no.png")
bFinalizar = PhotoImage(file="imagenes/button_finalizar.png")
fondo2 = PhotoImage(file="imagenes/fondo3.png")
palabra2 = PhotoImage(file="imagenes/resultado.png")

canvas = Canvas(welcome,width=900, height=600)
canvas.place(x=0,y=0)
bg = canvas.create_image(450,300, image = fondo)
titulo = canvas.create_image(450,50, image = tPregunta)

#Diseño factor de Reisgo
#canvas.create_image(270,200,image=iedad)
#canvas.create_image(270,300,image=ifuma)
#canvas.create_image(320,400,image=isobrepeso)
#edadC = canvas.create_text(620,200,text = edad, font = ("Roboto",28, "bold"), fill="MediumOrchid3")
#boxF = canvas.create_image(620,290,image=ino)
#boxS = canvas.create_image(620,380,image=ino)
#canvas.tag_bind(boxF,"<Button-1>",setBoxF)
#canvas.tag_bind(boxS,"<Button-1>",setBoxS)

#Espacio para las preguntas

finalPreguntas = sinFactores

for pos in finalPreguntas:
    textPreguntas.append(preguntas[pos])


frame = Frame(canvas, width=700, height = 400, bg="lavender", relief="solid", bd = 1)
frame.place_forget()
label = Label(frame, text="", font= ("Roboto",25, "bold"), anchor = "center", width = 26, justify="center" ,bg="lavender", wraplength=685)
label.place(x=0,y=0)
label["text"] = textPreguntas[indicePregunta]
frame.place(x=100,y = 80)


'''#Botones Factor riesgo
botonSig = Button(welcome, image=sig, text="", command = siguiente)
botonSig.place(x=390,y=500)
botonSig["border"]="0"

mas = Button(welcome, text="", image=imas, command = sumar, font = ("Roboto",17, "bold"))
mas.place(x= 700,y=175)
mas["border"]="0"

menos= Button(welcome, text="-", image=imenos , command = restar, font = ("Roboto",17, "bold"))
menos.place(x=500,y=175)
menos["border"]="0"'''



#Botones preguntas
botonSi = Button(welcome, image=imagenSi, text="", command = respuestaSi)
botonSi["border"] = "0"
botonSi.place(x=200,y=500)


botonNo = Button(welcome, image=imagenNo, text="", command = respuestaNo)
botonNo.place(x=570,y=500)
botonNo["border"] = "0"

botonFin = Button(welcome, image=bFinalizar, text="", command=finPreguntas)
botonFin.place_forget()
botonFin["border"] = "0"

welcome.mainloop()