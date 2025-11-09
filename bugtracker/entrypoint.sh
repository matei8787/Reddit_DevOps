#!/bin/bash
echo "Entrypoint run: "
which python
if [ "$ENV_TYPE" = "prod" ]; then
    echo "Waiting for postgres"
    while ! nc -z $DB_HOST $DB_PORT; do
        sleep 0.1
    done
    echo "Connection to database successfully establoshed"
fi

exec "$@"