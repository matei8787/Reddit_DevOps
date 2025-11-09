FROM nginx:alpine

RUN apk add --no-cache gettext

COPY entrypoint.sh /entrypoint.sh
COPY default.conf.template /etc/nginx/templates/default.conf.template

RUN chmod +x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]