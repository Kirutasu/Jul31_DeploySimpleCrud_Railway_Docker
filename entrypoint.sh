#!/bin/sh

# Espera a que el servicio de la base de datos esté listo
# Usamos 'nc' (netcat) para probar la conexión al host y puerto de la DB
# El bucle se repite hasta que la conexión sea exitosa
while ! nc -z $DB_HOST $DB_PORT; do
  echo "Esperando a la base de datos en $DB_HOST:$DB_PORT..."
  sleep 1
done

echo "La base de datos está lista. Aplicando migraciones..."

# Ejecuta las migraciones de Django
python manage.py migrate

# Inicia el servidor de Django
python manage.py runserver 0.0.0.0:8000