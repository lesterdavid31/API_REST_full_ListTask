# ToDo List API - RESTful Application

Este proyecto es una API RESTful para la gestión de tareas pendientes (ToDo List), con funcionalidades de autenticación de usuarios, operaciones CRUD, paginación, y filtrado.

## Cracterísticas
  -  **Reistro de usuario**: Permite registrar nuevos usuarios en el sistema.
  -  **Inicio de sesión**: Autentica al usuario y genera un token para futuras solicitudes.
  -  **Operaciones CRUD**: Los usuarios pueden crear, leer, actualizar y eliminar sus tareas pendientes.
  -  **Autenticación**: Solo los usuarios autenticados pueden acceder y m anipular sus lista de tareas.
  -  **Paginación y filtrado**: Implementa paginación y filtrado para gestionar listas de tareas grandes.
  -  **Base de datos**: Utiliza SQLite3 como base de datos.
   
## Insalación
  1 Clona el repositorio:
  ~~~
  git clone https://github.com/lesterdavid31/Api_ListTask.git
  ~~~
    
  2 Instala las dependencias:
  ~~~
  pip install -r requirements.txt
  ~~~

 3 Realiza las migraciones de base de datos:
  ~~~
  python manage.py migrate
  ~~~

 4 : Crea un superusuario (opcional para acceder al panel de administración):
  ~~~
 python manage.py createsuperuser
  ~~~

 3 Ejecuta el servidor local::
  ~~~
 python manage.py runserver
  ~~~

## Endpoints

**Registro de Usuario**
  - **URL**: /register/
  - **Método**: POST
  - **Descripción**: Crea un nuevo usuario.
  - **Cuerpo de la solicitud**:

  ~~~

{
  "username": "usuario",
  "password": "contraseña"
  "email": "email@gmail.com"
}

  ~~~

 - **Respuesta**
  ~~~   
{
  "token": "token_del_usuario generado"
  "username": "usuario"
}
  ~~~


**Inicio de Sesión**
  - **URL**: /login/
  - **Método**: POST
  - **Descripción**: Autentica el usuario y genera un token.
  - **Cuerpo de la solicitud**:

  ~~~

{
  "username": "usuario",
  "password": "contraseña"
}

  ~~~

  - **Respuesta**
  ~~~   
{
  "token": "token_del_usuario"
}
  ~~~


**Crear Tarea**
  - **URL**: /createtask/
  - **Método**: POST
  - **Descripción**: Crear una nueva tarea.
  - **Cuerpo de la solicitud**:

  ~~~

{
  "title": "Comprar leche",
  "description": "Comprar leche y huevos",
  "completed": false
}

  ~~~

  - **Respuesta**
  ~~~   
{
  "message": "Tarea creada",
  "serializer": {
    "title": "Comprar leche",
    "description": "Comprar leche y huevos",
    "completed": false
  }
}
  ~~~



**Obtener Lista de Tareas Paginadas**
  - **URL**: /tasklist/
  - **Método**: GET
  - **Descripción**: Obtiene la lista de tareas del usuario autenticado, con paginación.

  - **Respuesta**
  ~~~   
{
  "data": [
    {
      "id": 1,
      "title": "Comprar leche",
      "description": "Comprar leche y huevos",
      "completed": false
    },
    {
      "id": 2,
      "title": "Pagar facturas",
      "description": "Pagar agua y luz",
      "completed": false
    }
  ],
  "page": 1,
  "limit": 10,
  "total": 2
}

  ~~~

**Actualizar Tarea**
  - **URL**: /updatetask/<task_id>/
  - **Método**: POST
  - **Descripción**: Actualiza los detalles de una tarea existente.
  - **Cuerpo de la solicitud**:

  ~~~

{
  "title": "Pagar facturas",
  "description": "Pagar agua y luz",
  "completed": true
}


  ~~~

  - **Respuesta**
  ~~~   
{
  "estatus": "Tarea actualizada",
  "data": {
    "title": "Pagar facturas",
    "description": "Pagar agua y luz",
    "completed": true
  }
}

  ~~~


**Eliminar Tarea**
  - **URL**: /deletetask/<task_id>/
  - **Método**: DELETE
  - **Descripción**: Elimina una tarea del sistema.
  - **Respuesta**
    -  **204 No Content**

   
**Filtrar y Ordenar Tareas**
  - **URL**: /taskfilter/?title=Estudiar&completed=false
  - **Método**: GET
  - **Descripción**:Filtra las tareas por título y estado de completado.
  - **Parámetros de consulta**:
    - title: Filtra por tareas cuyo título contenga el valor proporcionado.
    - completed: Filtra por tareas completadas o no.
  
  - **Respuesta**
  ~~~   
{
  "data": [
    {
      "id": 3,
      "title": "Estudiar Django",
      "description": "Terminar el proyecto de Django",
      "completed": false
    }
  ],
  "page": 1,
  "limit": 10,
  "total": 1
}
  ~~~

## Autenticación 
Todos los endpoints, excepto el registro y el inicio de sesión, requieren autenticación mediante token. El token debe enviarse en los encabezados de la solicitud:

**authorization: Token <tu_token>**

## Base de Datos:
La base de datos utilizada es SQLite3, ya que este proyecto es una prueba conceptual. Para implementaciones más robustas, se recomienda utilizar una base de datos como PostgreSQL o MySQL.

## Contribución
Si deseas contribuir a este proyecto, por favor abre un pull request o reporta un issue.


[Repo Github](https://github.com/lesterdavid31/API_REST_full_ListTask)  
