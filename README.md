# Portfolio Personal con Blog - Django

Este proyecto consiste en un sitio web personal que integra un portfolio profesional con un sistema de blog funcional, desarrollado completamente en Django.

## Características principales

### Portfolio
- Diseño moderno y responsive con sidebar fijo
- Sistema de temas claro/oscuro con persistencia
- Secciones: Sobre mí, Experiencia, Proyectos y Blog
- Animaciones suaves de scroll
- Enlaces a redes sociales
- Navegación smooth scroll

### Blog
- Sistema de posts con texto e imágenes
- Comentarios con sistema de aprobación por administrador
- Solo usuarios autenticados pueden crear posts
- Administradores pueden eliminar comentarios
- Orden cronológico de entradas
- Integración visual con el portfolio
- Formularios estilizados con validación

## Estructura del proyecto
mysite/
├── blog/                   # Aplicación del blog
├── portfolio/              # Aplicación del portfolio
├── templates/              # Templates globales
├── static/                 # Archivos estáticos
├── media/                  # Archivos subidos
└── mysite/                 # Configuración principal