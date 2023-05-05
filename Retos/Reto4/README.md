# **Reto 4**
**Curso:** Tópicos Especiales en Telemática <br>
**Título:** <br>
**Autores:** Juan José Sánchez Cortés - Estudiante de la Universidad EAFIT - [jjsanchezc](https://gist.github.com/jjsanchezc) <br>
 Jose Manuel Fonseca -

***

**Tabla de Contenido**

1. [Introducción](#Introduccion)
2. [Estrucutra](#Estructura)
3. [AWS](#AWS)
 3.1. [Security Groups](#Security)
 3.2. [EFS](#EFS)
 3.3. [RDS](#RDS)
 3.4. [AMI](#AMI)
 3.5. [Instance Template](#Template)
 3.6. [Target Groups](#Target)
 3.7. [LoadBalancer](#LoadBalancer)
 3.8. [Autoscaling Groups](#Autoscaling)
4. [Instancia](#Instancia)
<br>

***

<div id='Introduccion'>

## 1 Introducción
 
El objetivo de este reto es migrar, re-diseñar e implementar la aplicación Moodle en un ambiente escalable y robusto que garantice la alta disponibilidad y rendimiento requeridos por la universidad. Para ello, se utilizarán los servicios administrados de AWS
***

<div id='Estructura'/>

## 2 Estructura

 Una aproximación cercana a nuestro trabajo:
 
![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103750661406990396/image.png)

***

<div id='AWS'/>

## 3 AWS
En esta sección se mostrará la configuración de cada una de las tecnologías de AWS que se usaron para poder realizar este reto

***


<div id='Security'/>

## 3.1 Security Groups

En las siguientes imagenes se muestra el proceso para la creación de los Security groups
![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103753186432528505/image.png)

en la primera imagen podemos ver como se configuran los puertos necesarios para poder usar HTTP, HTTPS y SSH. Tambien permitimos el trafico de todas partes sin restrcción alguna

![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103753400446894190/image.png)

Despues creamos un Security group para el EFS para permitir el acceso al purto 2049, la diferencia con el otro grupo es que en este grupo la destinación va directamente a las instancias que tengan el primer security group

***

<div id='EFS'/>

## 3.2 EFS


![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103753767779844217/image.png)

Se da el nombre al EFS y luego se crea el EFS

![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103754007064871053/image.png)

![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103754045530853376/image.png)

Despues se tiene que entrar a la configuración del EFS, esto mostrará todas las availability zones con sus Security Groups, AWS no configura automaticamente los Security groups que creamos con el EFS, por lo tanto toca buscar y seleccionarlos




***

<div id='RDS'/>

## 3.3 RDS

 Para la creación de la base de datos en RDS es completar las opciones que nos pide el AWS, en este caso base de datos MySQL y Template Free tier, seguimos con la info de las imagenes:
![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103755234188198098/image.png)
 ![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103755292631629885/image.png)
 ![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103755339935002657/image.png)
 ![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103755387078967507/image.png)
 
 Seleccionamos el Security group que creamos:
 
  ![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103755427902132274/image.png)
 ![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103755469832593449/image.png)
 
 El resultado debería quedar así: 
 
  ![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103777289390526474/image.png)
 
 Nota: el Endpoint nos servirá para la conexión

***

<div id='AMI'/>

## 3.4 AMI
Se crea una instancia en EC2 con una imagen de Ubuntu 22.04 con las siguientes configuraciones:
![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103778710496215141/image.png)
![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103778790896836718/image.png)
Se utiliza el segurity group reto4-sg creado previamente
![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103778873335873687/image.png)
Luego se ingresa a la instancia y se corren los siguientes comandos:
```sh
$sudo apt update
$sudo apt install docker.io -y
$sudo apt install docker-compose -y

$sudo systemctl enable docker
$sudo systemctl start docker
```
Estos comandos son para actualizar el docker
Luego procedemos instalar el docker de moodle con los siguientes comandos:
```sh
 $ sudo nano docker-compose.yml
```
Esto creara un archivo docker compose vacio en el cual agregaremos lo siguiente 
![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103793035617259631/image.png)
Luego subimos el docker
```sh
 $ sudo docker-compose up
```
Verificamos que este corriendo en la instancia, y cuando lo hagamos procedemos a settear el EFS en la instancia.
Esto se hace con los siguientes comandos:
```sh
 $sudo apt-get -y update
 $sudo apt-get -y install nfs-common
 $sudo mkdir -p /mnt/moodle
 $sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fs-04d475e35629ec77a.efs.us-east-1.amazonaws.com:/ /mnt/moodle
```
Esto permitira instalar el nfs-common en el cliente. Luego crea una carpeta con el nombre /mnt/moodle y luego se hace el mount y se enlaza la carpeta en con el efs-server.

Luego corremos el comando
```sh
 $df -h
```
Para verificar que se haya montado correctamente y deberiamos ver esto:
![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103797059145961482/image.png)
```sh
 $sudo nano /etc/fstab
```
![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103798354816815205/image.png)
Deberia aparecer este archivo y se agregara la linea:
```sh
 fs-04d475e35629ec77a.efs.us-east-1.amazonaws.com:/ /mnt/moodle nfs4 default 0 0
```
Para que asi se monte el efs immediatamente se cree la instancia.
Ya podemos cerrar la instancia.
Luego, le damos click derecho a la instancia y creamos una imagen a partir de esta.
![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103799683740086302/image.png)
La creamos con las siguientes configuracione
![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103805887317024818/image.png)
***

<div id='Template'/>

## 3.5 Instance Template

Ya luego procedemos a crear el template, es una configuración corta ya que la mayor parte de esta estuvo incluida en la creación de la imagen.
Primero nos dirigimos a launch template y le damos a crear. Nos deberia salir una ventana la cual configuraremos con la siguiente información:
![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103806251084812318/image.png)
Luego damos click en My AMIs, seleccionamos la opción "owned by me" y seleccionamos la imagen creada.
![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103806374695153755/image.png)
Luego seguimos con las siguientes configuraciones
![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103806533470519357/image.png)
Ya por ultimo, configuramos el grupo de seguridad para que sea el mismo que habiamos seleccionado previamente.
![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103806611094511667/image.png)

***

<div id='Target'/>

 ## 3.6 Target
 
 La configuración de esta es corta, simplemente se define que se quiere crear un target group de instancias y se le da el nombre y el puerto 
 ![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103807186360074260/image.png)
 ![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103807420741992488/image.png)
***

<div id='LoadBalancer'>

 ## 3.7 Load Balancer
 
 Para la confiugración del Load Balancer se configura como Application Load Balancer 
 ![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103808021873823785/image.png)
 Algo a resaltar es que se activan todos los mappings para que el balanceador de cargas funcione en todas las subredes posibles.
 ![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103807648543015012/image.png)
 ![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103807757141942452/image.png)
 Se seleccionan los security groups que se crearon y se configura que el puerto 80 haga un fordward to al target group que creamos
 ![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103807850091917363/image.png)
 
 

***


<div id='Autoscaling'>

 ## 3.8 Autoscaling group

Para el proceso de la configuración del autoscaling group, es muy sencillo, como se ve en la imagen, seleccionamos el template creado:
 ![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103808250194972703/image.png)
 
Luego llamamos al VPC y a las Availability Zones
 ![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103808401248628827/image.png)
 
 Para la configuración del Load balancer, damos la opción para escoger el load balancer target groups y seleccionamos el que creamos anteriormente
 ![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103808627095109733/image.png)
 
Lo ultimo en configurar son los Scaling policies, en este se colocará que al momento de que se utilice el 50% de la CPU se aumente automaticamente el numero de instancias
 ![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103809019715526676/image.png)
 
***

<div id='Instancia'>

## Configuración de Instancia
Se inicia la instancia 
 
```
 sudo apt update
sudo apt install docker.io -y
sudo apt install docker-compose -y
 sudo systemctl enable docker
sudo systemctl start docker
```
 Se abre el docker-compose.yml
 ```
sudo nano docker-compose.yml
 ```
  esto es lo que se ve al abrir el docker-compose:
 
 ![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103793035617259631/image.png)
 
Como se puede ver, tenemos el endpoint del RDS como host para nuestra base de datos, tambien comparte el nombre con el RDS, con esta configuración ya está conectandose a la base de datos creada con RDS. 
 Tambien se puede evidenciar en la ultima linea de volumenes se escribió  /mnt/moodle:/var/www/html para decir que en esta ruta habrá una carpeta de archivos compartidos 
 
 
 Despues de cerrar el docker-compose.yml se hace el siguiente comando para correrlo 
  ```
 sudo docker-compose up
  ```
luego los siguientes comandos son para montar el nfs y conectarlo con AWS:
```
sudo apt-get -y update
sudo apt-get -y install nfs-common
sudo mkdir -p /mnt/moodle
sudo mount -t nfs4 -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport fs-04d475e35629ec77a.efs.us-east-1.amazonaws.com:/ /mnt/moodle
```
Al escribir:
 ```
 df -h
 ```
muestra: 
 
 ![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103797059145961482/image.png)
 
 Se ejecuta:
```
 sudo nano /etc/fstab
fs-04d475e35629ec77a.efs.us-east-1.amazonaws.com:/ /mnt/moodle nfs4 default 0 0
```
 
 
 
 
***
