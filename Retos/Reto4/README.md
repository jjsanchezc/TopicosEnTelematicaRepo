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
 3.4. [Security Groups](#Security)
 3.5. [EFS](#EFS)
 3.6. [RDS](#RDS)
 3.7. [AMI](#AMI)
 3.8. [Instance Template](#Template)
 3.9. [Target Groups](#Target)
 3.10. [LoadBalancer](#LoadBalancer)
 3.11. [Autoscaling Groups](#Autoscaling)
4. [Instancia](#Instancia)
<br>

***

<div id='Introduccion'>

## 1 Introducción

***

<div id='Estructura'/>

## 2 Estructura

![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103778710496215141/image.png)

***

<div id='AWS'/>

## 3 AWS
En esta sección se mostrará la configuración de cada una de las tecnologías que se usaron para poder realizar este reto

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

## 2.3 RDS

![image](https://cdn.discordapp.com/attachments/1101910712651096197/1103777289390526474/image.png)

***

<div id='AMI'/>

## 3.4 AMI

***

<div id='Template'/>

## 3.5 Instance Template

***

<div id='Target'/>
imagen del dc

***

<div id='LoadBalancer'>
kk

***


<div id='Autoscaling'>
kk

***

<div id='Instancia'>

## Configuración de Instancia


***
