# Menu Restaurant
Version python 3.10.12
## Objetivo
Esta aplicacion es diseñada con el objetivo de 
a facilitar la gestión y administración de las empresas que
tengan giro comercial restaurantero.
Cuenta con una interfaz gráfica que permitirá a los empleados
y administradores a tener un control sobre la venta de mercancia a clientes
que gocen del servicio
Tendrá indicadores que permitirá el uso de mesas y control sobre las notas de venta
que realizan los empleados  (meseros) al momento de dar el servicio. 
## Instalar las  siguientes librerías para su ejecución 
Ejuctar script de la terminal ==> pip install -r requirements.txt
version de python compatible 3.10 (estable)
- customtkinter
- PIL
- sqlite3
- numpy
- pandas
- matplotlib
- scipy
- lxml
- pdfkit

## Como funciona

Sistema de registro de usuarios para poder realizar seguimiento a las ordenes de comida 
incluyendo la funcionalidad de un carrito de compras, del mismo modo se crea la base de datos
de forma automatica así como las relaciones que tiene entre ellos las tablas en una 
carpeta dentro del proyecto

El sistema funciona por medio de roles, dependiendo del rol que tenga el usuario
son las funciones que puede alcanzar. Para este caso existe 2 roles, el administrador
y el empleado que tiene las funciones básicas de agregar ordenes, visualizar sus ordenes
agregar a su carrito de compras productos y solicitar confirmaciones de pago
al igual que las notas de pago. Mientras que el administrador puede visualizar las ordenes
de todos los empleados, modificarlos y acceso a demás funcionalidades como modificar datos
y permisos de los usuarios. 


