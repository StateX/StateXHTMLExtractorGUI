import urllib2
import re

def Guardar():
	 #esto complia la exprsion siguiente
	 patron = re.compile("[-a-zA-Z0-9._]+@[-a-zA-Z0-9_]+.[a-zA-Z0-9_.]+")
	 smails = re.findall(patron,pagina)
	 listaemails = open ('listaemail.txt', 'a+')
	 d2 = str(smails)
	 listaemails.close()
	 print "e-mails guadados con exito"

#e-mails sacados de http://pastebin.com/ajaYnLYc

web =  raw_input("pega aqui la Url: ")

respuesta = urllib2.Request(web)
pagina = urllib2.urlopen(respuesta).read()
return Guardar()



