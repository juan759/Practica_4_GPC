# Practica_4_GPC

## Reporte de creación de archivo Python.

El archivo httpClient.py es un script de python3 el cual requiere de parametros 6 cosas: un host, una IP o un dominio, el método HTTP para comunicarnos con el servidor, un recurso el cual pedir, un user agent de alguno de nuestra lista de user agents permitidos, el encoding que tendrá la petición y finalmente si se mantendrá la conexión despues de cumplida la petición o si se cerrará la conexión. 

Primero, se creó la función que procesa los parametros que se pasan al script mediante command line y son puestos en una lista global.
Luego se crea la función que crea o junta todos los headers, con su valor ya sea obtenido por usuario o fijo, y luego crea la petición. Con su método HTTP, versión, recurso y cualquier otra información relevante para poder usar el protocolo HTTP.
Luego, se creó la función que crea el socket, lo inicializa, hace que se conecté al puerto 80 de nuestro host o dominio y luego envía la petición creada con la función anterior. Así, al recibir una respuesta sin importar su código esta será impresa en pantalla y se cerrará la conexión del socket al cliente.

## Ejemplos de uso:
python3 httpCliente.py mail7.unam.mx GET / Motorola gzip Keep-Alive

## Preguntas

1 ¿Cuál es la función de los métodos de HTTP HEAD, GET, POST, PUT y DELETE? 
  - HEAD, se utiliza como GET pero no queremos que el servidor nos envíe contenido en su respuesta. Sólo probar si responde o no el servidor.
  - GET, es el método principal para la obtención de información y recursos de un servidor. Pide una representación seleccionada de un recurso actual.
  - POST, este método le pide al servidor que el recurso objetivo procese lo que le envíemos, información generalmente, a su propia semantica. Se usa para logins, por ejemplo.
  - PUT, se utiliza cuando queremos modificar o actualizar algún elemento que envíamos en nuestra petición.
  - DELETE, se utiliza cuando queremos eliminar o borrar algún recurso en el servidor.
1 ¿Investigue y enliste junto con su significado las categorías de códigos de estado que usa HTTP?
  - Informational responses (100 – 199). Estos códigos son para indicar que la petición fue recibida y se está continunado algún proceso sobre ella.
  - Successful responses (200 – 299). Estos códigos son para indicar que la petición fue recibida, entendida y aceptada.
  - Redirection messages (300 – 399). Estos códigos son para indicar que se necesitan más acciones o eventos para procesar y responder la petición.
  - Client error responses (400 – 499). Estos códigos son para indicar que la petición tiene mala sintaxis o que el recurso solicitado no existe.
  - Server error responses (500 – 599). Estos códigos son para indicar que el servidor no pudo completar o procesar una petición válida. 
1 ¿Para qué se usan los campos encoding y connection?
  - Connection: controla si la conexión se queda abierta o no cuando la petición original sea completada.
  - Encoding: controla qué codificaciones han sido aplicadas y en qué orden, a la representación actual del mensaje.

## Fuentes
https://httpwg.org/specs/rfc9110.html#status.codes
https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#information_responses
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Connection
