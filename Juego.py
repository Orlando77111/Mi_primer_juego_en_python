from tkinter import *
import random

#...................
# variables globales
#...................

X = 660
Y = 460
radio = 10
desplazamiento_x = 1
desplazamiento_y = 1
intervalo = 2

centro_x = random.randint(radio, X)
centro_y = random.randint(radio, Y)

def Jugar():
    global desplazamiento_x, desplazamiento_y
    
    x0, y0, x1, y1 = c.coords(carrojo)
    if x0 < 0 or x1 > X: 
        desplazamiento_x = -desplazamiento_x
    if y0 < 0 or y1 > Y: 
        desplazamiento_y = -desplazamiento_y
    c.move(carrojo, desplazamiento_x, desplazamiento_y)
    ventana_principal.after(intervalo, Jugar)

#Crear una ventana 
ventana_principal = Tk()
ventana_principal.title("Graficas 2D")
ventana_principal.resizable(False,False)
ventana_principal.geometry("700x600")
ventana_principal.config(bg="black")

#frame

graf = Frame(ventana_principal)
graf.config(width=680, height=580, bg="red")
graf.place(x=10,y=10)

# Canvas

c = Canvas(graf,width=X, height=Y)
c.config(bg="black")
c.place(x=10,y=10)

# Boton jugar
bt_jugar = Button(graf)
bt_jugar.config(width=20, height=5, text="Vamos a Jugar", command=Jugar)
bt_jugar.place(x=250,y=480)

# Rectangulos salida y meta

rect_3 = c.create_rectangle(X/2-230,Y/2+200,X/2-150,Y/2-230, fill="gray10")
rect_4 = c.create_rectangle(X/2+290,Y/2+200,X/2+210,Y/2-290, fill="gray10")

# Salida , Meta

s = c.create_text(X/2-190,Y/2-130, anchor="center", text="S", font=("Arial", 18, "bold"), fill="blue violet", activefill="yellow")
a = c.create_text(X/2-190,Y/2-80, anchor="center", text="a", font=("Arial", 18, "bold"), fill="blue violet", activefill="yellow")
l = c.create_text(X/2-190,Y/2-30, anchor="center", text="l", font=("Arial", 18, "bold"), fill="blue violet", activefill="yellow")
i = c.create_text(X/2-190,Y/2+20, anchor="center", text="i", font=("Arial", 18, "bold"), fill="blue violet", activefill="yellow")
d = c.create_text(X/2-190,Y/2+70, anchor="center", text="d", font=("Arial", 18, "bold"), fill="blue violet", activefill="yellow")
a2 = c.create_text(X/2-190,Y/2+120, anchor="center", text="a", font=("Arial", 18, "bold"), fill="blue violet", activefill="yellow")

m = c.create_text(X/2+250,Y/2-80, anchor="center", text="M", font=("Arial", 18, "bold"), fill="red", activefill="blue")
e = c.create_text(X/2+250,Y/2-30, anchor="center", text="e", font=("Arial", 18, "bold"), fill="red", activefill="blue")
t = c.create_text(X/2+250,Y/2+20, anchor="center", text="t", font=("Arial", 18, "bold"), fill="red", activefill="blue")
a3 = c.create_text(X/2+250,Y/2+70, anchor="center", text="a", font=("Arial", 18, "bold"), fill="red", activefill="blue")



# Pasto :)
rect_1 = c.create_rectangle(X/2-340,Y/2+155,X/2+340,Y/2+230, fill="green")
rect_2 = c.create_rectangle(X/2-340,Y/2-155,X/2+340,Y/2-240, fill="green")

# Lineas de la carretera

rect_5 = c.create_rectangle(X/2-100,Y/2-10,X/2+170,Y/2+10, fill="white")
rect_6 = c.create_rectangle(X/2-350,Y/2-10,X/2-250,Y/2+10, fill="white")
rect_7 = c.create_rectangle(X/2+350,Y/2-10,X/2+300,Y/2+10, fill="white")

# carros

img_carrojo = PhotoImage(file="img/carro1.png")
carrojo = c.create_image(X/2-260,Y/2-80,image=img_carrojo)

img_carranja = PhotoImage(file="img/carro2.png")
carranja = c.create_image(X/2-260,Y/2+60,image=img_carranja)


ventana_principal.mainloop()