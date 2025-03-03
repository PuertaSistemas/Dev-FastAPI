# FastAPI - Backend development init

Éste paquete ha sido construído para facilitar elinicio de un proyecto com *FastAPI* e integrado con *PostgreSQL*.

El objetivo es cotar con una estructúra mínima de FastAPI y las librerías básicas para el uso de PostgreSQL. Todo combinado en un paquete de *docker compose* que facilita el lanzar nuevas instancias.

Para gestionar la base de datos durante el desarrollo se ha optado por *Adminer*, un frontend para la gestión de bases de datos basado en WEB.

## Configuración de entorno con ".env"

En el archivo *.env* que se encuentra en la raíz del proyecto. Contiene la información necesaria para la imagen de Docker/Postgre para la comfiguración inicial del motor de base de datos.

'''
POSTGRES_USER= 'postgres'
POSTGRES_PASSWORD= 'example'
POSTGRES_PORT= 5432
POSTGRES_DB= 'testing'
'''

En el archivo *.env* que se encuentra dentro de *backend*, se configura las variables de entorno de FastAPI para la conexión a la base de datos.

'''
DATABASE_URL = 'postgresql://postgres:example@db:5432/testing'
'''

Se configura variables de entorno útiles para el futuro uso de librerias de JWT.

'''
SECRET_KEY = '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

'''

## Iniciar el proyecto

Para iniciar el proyecto se lanza desde el comando

'''
docker comose up -d
'''
