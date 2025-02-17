FROM python:3.11-alpine AS base

ENV TZ=UTC
ENV PYTHONDONTWRITEBYTECODE=1

COPY requirements.txt .
RUN python3 -m pip install --no-cache-dir --upgrade pip  &&\
    python3 -m pip install --no-cache-dir -r requirements.txt


FROM python:3.11-alpine

LABEL org.opencontainers.image.source="https://github.com/smashedr/flask-random-image"
LABEL org.opencontainers.image.description="Flask Random Image"
LABEL org.opencontainers.image.authors="smashedr"

ENV TZ=UTC
ENV PYTHONUNBUFFERED=1

COPY --from=base /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY --from=base /usr/local/bin/ /usr/local/bin/

RUN addgroup -g 1000 app  &&\
    adduser -S -H -h /app -s /sbin/nologin -u 1000 -G app app  &&\
    mkdir -p /app /data  &&  chown app:app /app /data  &&\
    apk add --no-cache curl

WORKDIR /app
COPY --chown=app:app . .
USER app
ENTRYPOINT ["sh", "docker-entrypoint.sh"]
