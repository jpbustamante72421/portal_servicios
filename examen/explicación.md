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

# Evidencias e interpretación de resultados
## Portal de Servicios

El presente documento contiene las evidencias de funcionamiento de las calculadoras desarrolladas en el proyecto Portal de Servicios, así como una breve interpretación de los resultados obtenidos.

## 1. Calculadora de Compra

**Datos de entrada:**
- Cantidad de artículos: 5
- Precio unitario: $250.00

**Resultados obtenidos:**
- Subtotal: $1,250.00
- Descuento del 10%: $125.00
- Total: $1,125.00

**Evidencia:**

[Ver evidencia de compra con descuento](evidencias/compra.png)

**Interpretación:**

El sistema multiplica la cantidad de artículos por el precio unitario para obtener un subtotal de $1,250.00. Debido a que el subtotal supera los $1,000.00, se aplica un descuento del 10%, equivalente a $125.00. Finalmente, se obtiene un total de $1,125.00.

### Prueba sin descuento

**Datos de entrada:**
- Cantidad de artículos: 2
- Precio unitario: $200.00

**Resultados obtenidos:**
- Subtotal: $400.00
- Descuento: $0.00
- Total: $400.00

**Evidencia:**

[Ver evidencia de compra sin descuento](evidencias/compra_sin_descuento.png)

**Interpretación:**

Como el subtotal no supera los $1,000.00, el sistema no aplica ningún descuento y conserva el importe original de la compra.

## 2. Calculadora de Salario

**Datos de entrada:**
- Horas trabajadas: 45
- Pago por hora: $100.00

**Resultados obtenidos:**
- Horas normales: 40
- Horas extra: 5
- Pago normal: $4,000.00
- Pago de horas extra: $1,000.00
- Salario total: $5,000.00

**Evidencia:**

[Ver evidencia de salario con horas extra](evidencias/salario.png)

**Interpretación:**

El sistema identifica que se trabajaron 45 horas. Las primeras 40 se pagan a la tarifa normal de $100.00, mientras que las 5 horas adicionales se pagan al doble, es decir, a $200.00 cada una. El salario total obtenido es de $5,000.00.

### Prueba sin horas extra

**Datos de entrada:**
- Horas trabajadas: 35
- Pago por hora: $100.00

**Resultados obtenidos:**
- Horas normales: 35
- Horas extra: 0
- Salario total: $3,500.00

**Evidencia:**

[Ver evidencia de salario sin horas extra](evidencias/salario_sin_horas_extra.png)

**Interpretación:**

El sistema determina que las 35 horas trabajadas se encuentran dentro del límite de 40 horas normales. Por lo tanto, no se generan horas extra y el salario corresponde a $3,500.00.

## 3. Conversor de Temperatura

**Dato de entrada:**
- Temperatura: 25 °C

**Resultados obtenidos:**
- Fahrenheit: 77 °F
- Kelvin: 298.15 K

**Evidencia:**

[Ver evidencia de conversión de temperatura](evidencias/temperatura.png)

**Interpretación:**

El sistema recibe la temperatura en grados Celsius y realiza las conversiones correspondientes utilizando las fórmulas matemáticas de Fahrenheit y Kelvin. Para una temperatura de 25 °C, se obtiene un resultado de 77 °F y 298.15 K.

## 4. Conclusión

El proyecto Portal de Servicios cumple con la implementación de tres calculadoras mediante Flask, utilizando formularios HTML con el método POST para recibir los datos y procesarlos mediante Python.

Los resultados son enviados a las plantillas HTML utilizando Jinja2, permitiendo visualizar tanto los datos capturados como los resultados de cada operación.

Además, se implementó una navegación común mediante una plantilla base, así como componentes de Bootstrap para mejorar la presentación y organización de la aplicación.