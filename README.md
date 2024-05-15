# VeredaAlerta

VeredaAlerta es una aplicación web diseñada para alertar a la comunidad en una vereda sobre eventos importantes mediante mensajes de alerta. La aplicación permite a los usuarios registrados crear, visualizar, actualizar y eliminar alertas, filtrarlas por nivel de importancia, y gestionar sus cuentas de usuario.

## Características

- **Registro e Inicio de Sesión:** Los usuarios pueden registrarse con un nombre de usuario, correo electrónico y contraseña. También pueden iniciar sesión y cerrar sesión.
- **Gestión de Alertas:** Los usuarios pueden agregar alertas con un mensaje y nivel de importancia (Alto, Medio, Bajo). Las alertas se pueden actualizar y eliminar.
- **Filtrado de Alertas:** Las alertas se pueden filtrar por nivel de importancia.
- **Persistencia de Datos:** Las alertas y la información de los usuarios se almacenan en una base de datos MongoDB.
- **Tiempo de Inactividad:** La sesión del usuario se cierra automáticamente después de 5 minutos de inactividad.

## Tecnologías Utilizadas

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask (Python)
- **Base de Datos:** MongoDB
- **Otros:** Flask-PyMongo, Flask-Bcrypt

## Requisitos Previos

- Python 3.7 o superior
- MongoDB
- Node.js y npm

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/veredaalerta.git
cd veredaalerta
