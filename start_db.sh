#!/bin/bash

# Config
export PG_CONTAINER_NAME="pg_test_instance"
export PG_PORT=5432
export PG_DB="mydb"
export PG_USER="myuser"
export PG_PASSWORD="mysecretpassword"

# Stop and remove if it already exists
if [ "$(docker ps -aq -f name=$PG_CONTAINER_NAME)" ]; then
    echo "Removing existing container..."
    docker stop $PG_CONTAINER_NAME >/dev/null
    docker rm $PG_CONTAINER_NAME >/dev/null
fi

# Start Postgres
echo "Starting Postgres container..."
docker run -d \
  --name $PG_CONTAINER_NAME \
  -e POSTGRES_PASSWORD=$PG_PASSWORD \
  -e POSTGRES_USER=$PG_USER \
  -e POSTGRES_DB=$PG_DB \
  -p $PG_PORT:5432 \
  postgres:15 -c max_connections=200


echo "PostgreSQL started at localhost:$PG_PORT"
echo "Run your Python script in this terminal to inherit env vars."