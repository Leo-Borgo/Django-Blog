# Proyecto Django - Trabajo Práctico N°3

Este proyecto fue realizado como parte del Trabajo Práctico N°3 de la materia **Laboratorio de Algoritmos y Estructuras de Datos**. Consiste en una aplicación web desarrollada con el framework **Django**, donde se trabajó con bases de datos, vistas, templates, formularios, administración y lógica de backend.

## Documentacion DJANGO

Se siguió paso a paso el tutorial de Django desde la documentación oficial hasta la parte 8, realizando cada uno de los siguientes componentes:

1. **Inicio del proyecto Django**
2. **Creación de una app llamada "polls"**
3. **Definición de modelos de Preguntas y Opciones (Choices)**
4. **Migraciones y configuración de base de datos (SQLite)**
5. **Registro de modelos en el panel de administración**
6. **Creación de vistas y URLs para mostrar preguntas y votar**
7. **Templates para renderizar páginas con HTML dinámico**
8. **Formulario de votación y resultados**


---

## Estructura del Proyecto

mysite/
│
├── manage.py
├── db.sqlite3
├── mysite/ # Configuración principal del proyecto
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
└── polls/ # App de encuestas
├── migrations/
├── init.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── views.py
├── urls.py
└── templates/
└── polls/
├── index.html
├── detail.html
├── results.html


---

## Cómo correr el servidor 

Desde la terminal, estando en la carpeta del proyecto (donde está `manage.py`), ejecutar:

```bash
python manage.py runserver

