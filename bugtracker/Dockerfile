FROM python:3.12-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app


RUN apt update && apt install -y build-essential

COPY req.txt .
RUN pip install --upgrade pip && \
    pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r req.txt


FROM python:3.12-slim

ENV HOME=/home/app
ENV APP_HOME=/home/app/web

COPY --from=builder /usr/src/app/wheels /wheels
RUN apt update && apt install -y netcat-openbsd && \
    pip install --upgrade pip && \
    pip install --no-cache /wheels/*

# Create necessary users and directories
RUN adduser --system --group app && \
    mkdir -p ${APP_HOME} \
    mkdir -p ${APP_HOME}/staticfiles

WORKDIR ${APP_HOME}

COPY . ${APP_HOME}

RUN chown -R app:app ${HOME}

USER app 

RUN sed -i 's/\r$//g'  ${APP_HOME}/entrypoint.sh && \
    chmod +x ${APP_HOME}/entrypoint.sh

ENTRYPOINT [ "/home/app/web/entrypoint.sh" ]

