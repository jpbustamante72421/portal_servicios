# Recorrido de la aplicación de compra

Bueno, cuando el empleado escribe la dirección de la aplicación en el navegador, este funciona como **cliente** ya que la dirección identifica el equipo donde se ejecuta la aplicación: si se usa un nombre de dominio este es una **dirección IP**, la URL indica el **puerto** al que debe conectarse el navegador.

El navegador inicia la comunicación mediante **HTTP** y envía una **request** (petición) al servidor. En la primera visita normalmente solicita la página con el método GET. El servidor ejecuta la aplicación escrita en **Python** y atendida por **Flask**. Flask compara la dirección solicitada y el método con una **ruta** definida en la aplicación; para esa primera visita, la ruta prepara la página del formulario.

La aplicación devuelve una **response** (respuesta) con el formulario. Flask puede construirla usando un **template**: una plantilla que combina la estructura de la página con los datos que la aplicación le entrega. El navegador recibe el **HTML** y lo interpreta para mostrar los campos donde se capturan cantidad y precio. Esa parte que el empleado ve e interactúa en el navegador es el **frontend**. Las reglas **CSS** controlan la presentación visual; si el proyecto incluye **Bootstrap**, sus estilos también pueden ayudar a organizar y dar formato a los controles. En este recorrido no se necesita **JavaScript** para enviar el formulario ni calcular el importe: el empleado lo envía y el cálculo ocurre en el servidor.

Después de escribir la cantidad y el precio, el empleado envía el formulario. El navegador manda esos valores en una nueva petición **HTTP** usando el método **POST**, que incluye los datos del formulario en el cuerpo de la petición. El **backend** recibe la petición en la ruta de Flask que acepta POST. Allí, el código **Python** obtiene los valores, los convierte a números y calcula el importe multiplicando la cantidad por el precio.

Con el resultado, Flask genera otra respuesta, normalmente al renderizar un **template** con el importe calculado. El servidor la devuelve al cliente como una **response** que contiene **HTML**. Finalmente, el navegador interpreta ese HTML y presenta el importe al empleado, aplicando los estilos **CSS** y **Bootstrap** si están incluidos y enlazados en la página.

## Diagrama de comunicación

```mermaid
sequenceDiagram
    actor Empleado
    participant Cliente as Navegador (cliente)
    participant Servidor as Servidor Flask (IP:puerto)

    Empleado->>Cliente: Escribe la dirección de la aplicación
    Cliente->>Servidor: HTTP GET a la ruta del formulario
    Servidor-->>Cliente: HTTP response con HTML del formulario
    Cliente-->>Empleado: Muestra los campos de cantidad y precio
    Empleado->>Cliente: Captura los valores y envía el formulario
    Cliente->>Servidor: HTTP POST con cantidad y precio
    Note over Servidor: Flask enruta la petición; Python procesa los datos y calcula cantidad × precio
    Servidor-->>Cliente: HTTP response con HTML y el importe
    Cliente-->>Empleado: Presenta el resultado
```

En el diagrama, el **cliente** es el navegador y el **servidor** es el proceso donde corre Flask, accesible mediante su **IP:puerto**. Primero el navegador solicita el formulario; luego envía una petición **POST** con los datos. Flask los procesa en el **backend** y retorna el **HTML** actualizado, que el navegador muestra al empleado.