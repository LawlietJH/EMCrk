# EMCrk

## Obten Contraseñas de Cuentas de Correo por Fuerza Bruta.

1. Crea tu diccionario personalizado o Crea el archivo ***pwd.zion*** en donde deberas agregar todas las palabras que desees utilizar.
2. Al abrir el ***script*** coloca el nombre completo del correo victima (ejemplo@gmail.com, ejemplo@hotmail.com, etc.).
3. Puedes Colocar el nombre de tu diccionario al abrir el ***Script*** o simplemente precionar ***Enter*** y se tomara el diccionario por defecto: ***pwd.zion***

- - -

**Modo de uso: `EMCrk.py [-v][-s] | [-a] | [-h]`**
+ Para ver la ***Versión***, la ***Lista de Servicios de Correos*** y correr el ***Script***, se debe añadir el argumento __[-a] | [--all]__
  + **`EMCrk.py -a`**
   
+ Para ver el ***Modo De Uso***, se debe añadir el argumento __[-h] | [--help]__ En Consola.
  + **`EMCrk.py -h`**
   
+ Para ver la ***Lista de Servicios de Correo*** soportados, se debe añadir el argumento __[-s] | [--serv]__ En Consola.
  + **`EMCrk.py -s`**
   
+ Para ver la versión del ***Script*** se debe añadir el argumento __[-v] | [--version]__ En Consola.
  + **`EMCrk.py -v`**
   
+ Para ver la ***Version*** y La ***Lista de Servicios De Correos***, se debe añadir el argumento __[-s]__ y __[-v]__ juntos En Consola.
  + **`EMCrk.py -s -v`**
  + **`EMCrk.py -v -s`**
   
+ O simplemente ejecuta el ***Script*** sin ningun argumento.
  + **`EMCrk.py`**

- - -

## Tipos De Correos Soportados En Este Script:

### Comprobados [_02_]:

***gmail.com*** y ***hotmail.com***

### Aún en prubas [_33_]:

_mail.com,          **yahoo.com,**          ymail.com,         **roketmail.com,**     gmx.es,
**zoho.com,**          fastmail.com,       **hushmail.com,**      live.com,          **aol.com,**
airmail.net,       **1and1.com,**          att.net,           **bluewin.ch,**        btconnect.com,
**earthlink.net,**     hotpop.com,         **inbox.com,**         libero.it,         **lycos.com,**
o2.com,            **orange.com,**         terra.com,         **tiscali.co.uk,**     virgin.net,
**wanadoo.fr,**        housemusic.com,     **web.de,***            verizon.net,       **comcast.net,**
upla.cl,           **udec.cl,**            rediffmail.com_
 
- - -
 
## [ ! ] Nota:

### EL Proceso de obtención de contraseñas es algo lento...

***Los Correos como Hotmail, se han comprobado que se podran obtener sus contraseñas sin ningun problema, si en el diccionario se encuentra la contraseña correcta, claro está.***

### En Gmail:
Este ***Script*** Funcionará realmente para obtener las Contraseñas de Cuentas de correo Gmail, si y sólo si el correo de la víctima tiene activada la opción ***Acceso de aplicaciones menos seguras***.

Si esta opción está desactivada, el ***Script*** al estar probando palabras con el diccionario pasara por alto la contraseña correcta (y al mismo tiempo, le llegará un correo a la cuenta de la víctima por parte de su mismo servicio de correos, diciendo: ***"	Revisa el intento de inicio de sesión bloqueado"***) y seguirá probando las siguientes palabras hasta terminar de leer todo el Diccionario.

Si la opción está activada, el ***Script*** mostrara la contraseña correcta en el momento que dé con ella y la guardara en un archivo llamado **CC.zion** (Correo y Contraseña - **CC**).
