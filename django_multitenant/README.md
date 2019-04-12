# Django Multitenant

Vamos a reconstruir una aplicación para que sea una aplicación Multitenant. Usaremos la aplicación de encuestas de Django ligeramente modificada como nuestra base.

Existen múltiples enfoques para la multitenant. Los cuatro más comunes son:

1. Shared database with shared schema
2. Shared database with isolated schema (Vamos a usar este enfoque)
3. Isolated database with a shared app server
4. Completely isolated tenants using Docker

## Base de datos compartida con esquema aislado

Una sola base de datos mantiene los datos de cada inquilino. Los datos de cada inquilino están en un esquema separado dentro de la base de datos única. El esquema identifica al arrendatario y los datos presentados no tienen un FK para el arrendatario.


