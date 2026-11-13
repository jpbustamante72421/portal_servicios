# Portal de Servicios

## 1. Propósito del proyecto

El proyecto **Portal de Servicios** consiste en una aplicación web desarrollada con Python, Flask y Bootstrap.

Su propósito es ofrecer diferentes herramientas y servicios mediante una interfaz web sencilla y accesible.

La aplicación cuenta con las siguientes secciones:

- **Inicio:** presentación del portal y carrusel de imágenes.
- **Compra:** cálculo de subtotal, descuento y total de una compra.
- **Salario:** cálculo del salario considerando horas normales y horas extra.
- **Temperatura:** conversión de grados Celsius a Fahrenheit y Kelvin.
- **Empresa:** descripción, misión y visión.
- **Servicios:** presentación de las herramientas disponibles.
- **Contacto:** información de contacto de la empresa.

## 2. Requisitos para la ejecución

Para ejecutar el proyecto se necesita:

- Python 3.10 o superior.
- Visual Studio Code (recomendado).
- Navegador web.
- Conexión a Internet para cargar Bootstrap desde CDN.

## 3. Creación del entorno virtual

Primero, abrir una terminal en la carpeta principal del proyecto.

Ejecutar el siguiente comando para crear el entorno virtual:

```bash
python -m venv venv
```

### Activación en Windows

```bash
venv\Scripts\activate
```

### Activación en Linux o macOS

```bash
source venv/bin/activate
```

## 4. Instalación de dependencias

Con el entorno virtual activado, instalar las dependencias utilizando el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

## 5. Ejecución del proyecto

Para iniciar la aplicación, ejecutar el siguiente comando desde la carpeta principal:

```bash
python app.py
```

Una vez iniciada la aplicación, abrir el siguiente enlace en el navegador:

**http://127.0.0.1:5000**

## 6. Tecnologías utilizadas

- **Python:** lenguaje utilizado para desarrollar la lógica de la aplicación.
- **Flask:** framework utilizado para crear las rutas y gestionar las solicitudes.
- **HTML5:** estructura de las páginas web.
- **CSS3:** personalización de los estilos.
- **Bootstrap 5:** diseño adaptable y componentes visuales.
- **Jinja2:** integración de datos dinámicos en las plantillas HTML.

## 7. Estructura del proyecto

```text
Portal de Servicios/
│
├── examen/
│   ├── explicacion.md
│   └── evidencias/
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── compra.html
│   ├── salario.html
│   ├── temperatura.html
│   ├── empresa.html
│   ├── servicios.html
│   └── contacto.html
│
├── static/
│   ├── css/
│   │   └── estilos.css
│   └── img/
│
├── app.py
├── requirements.txt
└── README.md
```

## 8. Autor

Juan Pablo Bustamante Martínez.