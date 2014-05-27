#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import * 
import urllib2
import re 


def mostrar(window): 
	 window.deiconify()
def ocultar(window):
	 window.withdraw()
def ejecutar(f): 
	 ventana.after(0,f)
def crawler(web):
	 try: 
	 	 respuesta = urllib2.Request(web) 
 	 	 pagina = urllib2.urlopen(respuesta).read()
 	 	 if pagina: 
	 	 	 #esto complia la exprsion siguiente
 	 	 	 patron = re.compile("[-a-zA-Z0-9._]+@[-a-zA-Z0-9_]+.[a-zA-Z0-9_.]+")
	 	 	 #se explica por si mismo 
	 	 	 smails = re.findall(patron,pagina)
	 	 	 listaemails = open ('listaemail.txt', 'a+')
	 	 	 d2 = str(smails)
	 	 	 listaemails.write(d2)
	 	 	 listaemails.close()
		 	 label3=Label(ventana, bg='white' ,text=" URL valida  ")
		 	 label3.grid(row=5, column=2) 
	 	 	 ejecutar(mostrar(ventana1))

	 except: 	
	 	 label3=Label(ventana, bg='white' ,text=" Pon una URL ")
		 label3.grid(row=5, column=2)


#Configuración ventanas

if __name__ == "__main__":

	 ventana = Tk()
	 ventana1 = Toplevel(ventana)
	 ventana.title('HTML Email Extractor')
	 ventana.config(bg='white')
	 ventana1.config(bg='white')
#ventana

	 label1=Label(ventana, bg='white',text="StateX Email Extractor", font= (16) )
	 label1.grid(row=1, column=2)
	 label2=Label(ventana,bg='white' ,text="Pon una URL:")
	 label2.grid(row=2,column =2)
	 caja = Entry(ventana)
	 caja.grid(row=3, column=2)
	 boton1 = Button(ventana, text="Start", bg='white', command=lambda: crawler(caja.get()))
	 boton1.grid(row=4, column=2)
	 
#ventana 1

	 label4=Label(ventana1, bg ='white', text = "Correos almacenados con éxito") 
	 label4.grid(row=1, column=2)
	 boton2 = Button(ventana1, bg='white', text="Seguir",command= lambda: ejecutar(mostrar(ventana)) or caja.delete(0,END))
	 boton2.grid(row=3, column=2)
	 boton3 =  Button(ventana1, bg='white', text="Salir", command=  ventana.destroy)
	 boton3.grid(row=4, column=2)

#Estado inicial de las ventanas

	 ventana1.withdraw()
	 ventana.mainloop()

	