#!/bin/sh

set -e

COMPOSE_FILE="docker-compose.stage.yml"

echo "Getting current images ID"

IMAGES_ID=$(docker-compose -f "$COMPOSE_FILE" images --quiet)

echo "Pulling the latest images"

docker-compose -f "$COMPOSE_FILE" pull

NEW_IMAGES_ID=$(docker-compose -f "$COMPOSE_FILE" images --quiet)

if [ "$IMAGES_ID" != "$NEW_IMAGES_ID" ]; then
    echo "Images Changed"
    docker-compose -f "$COMPOSE_FILE" up -d 
fi