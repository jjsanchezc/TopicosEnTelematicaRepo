# Middleware Orientado a Mensajes (MOM)

Un middleware orientado a mensajes es un componente de software que facilita la comunicación entre aplicaciones distribuidas al establecer una capa intermedia de comunicación. En este proyecto se realizará un middleware que se encargará de la gestión de mensajes entre las aplicaciones, lo que permite una comunicación más eficiente y escalable, ya que en lugar de tener que establecer conexiones directas entre aplicaciones, las aplicaciones pueden enviar mensajes a través del middleware, que los enruta a su destino apropiado. Esto permite una comunicación más independiente y flexible, permitiendo una mayor modularidad y reutilización del código.

## Documento Requerimientos -

Para el análisis, diseño e implementación de un Middleware de Mensajería, se tuvo en cuenta la siguiente arquitectura

<p align="center">
  <img src="https://user-images.githubusercontent.com/68908889/231040390-8567b1ba-24bf-495e-b852-b3345c09745b.png" alt="Arquitectura" width="600" height="300" style="display: block; margin: auto;">
</p>

## Documento Diseño detallado desde el sistema distribuido y software -

Para el diseño detallado del sistema se realizó una estructura de desglose de trabajo en donde se tuvieron en cuenta los siguientes requerimientos de diseño:

- La conexión / desconexión, se hace con usuarios autenticados
- Solo puede borrar canales o colas de los usuarios que los crearon.
 - ¿Qué pasaría con los mensajes existentes en un canal o una cola? Se creo un JSON para estos mensajes existentes 
-  El envío y recepción de mensajes identifica los usuarios.
- Todos los servicios están expuestos a través de un API REST hacia los Clientes.
- La interacción entre mensajes es asincrónica.
- Se maneja el termino de sesión
- Existen niveles de transparencia.
-Se consideraron temas de multiusuario


## Documento de detalles/dependencia de implementación, instalación y ejecución - 

Para la ejecución de nuestro proyecto se deben seguir los siguientes comandos


## Mejoras

- El transporte de los mensajes debería ser encriptada así como el servicio de autenticación.
- Modelo de manejo de fallos.
- Modelo de seguridad.
