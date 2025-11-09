#!/bin/sh

envsubst < /etc/nginx/templates/default.conf.template > /etc/nginx/conf.d/default.conf

sed -i "s/###/$/g" /etc/nginx/conf.d/default.conf

nginx -g 'daemon off;'

exec "$@"