#!/usr/bin/env bash
set -e

REGISTRY_HOST="ghcr.io"
REGISTRY_USER="smashedr"
REGISTRY_REPO="flask-random-image"

#if [ -f ".env" ];then
#    echo "Sourcing Environment: .env"
#    source ".env"
#fi

if [ -z "${VERSION}" ]; then
    if [ -z "${1}" ]; then
        VERSION="latest"
        #read -rp "Version: [latest] " VERSION
        #if [ -z "${VERSION}" ];then
        #    VERSION="latest"
        #fi
    else
        VERSION="${1}"
    fi
fi

for NAME in app nginx; do
    echo "Building: ${REGISTRY_HOST}/${REGISTRY_USER}/${REGISTRY_REPO}-${NAME}:${VERSION}"

    docker build -t "${REGISTRY_HOST}/${REGISTRY_USER}/${REGISTRY_REPO}-${NAME}:${VERSION}" "${NAME}"

    #docker login --username "${USERNAME}" --password "${PASSWORD}" "${REGISTRY_HOST}"
    #docker push "${REGISTRY_HOST}/${REGISTRY_USER}/${REGISTRY_REPO}:${VERSION}"

    #docker buildx create --use --name builder
    #docker buildx build --platform linux/amd64,linux/arm64 --push  \
    #    -t "${REGISTRY_HOST}/${REGISTRY_USER}/${REGISTRY_REPO}:${VERSION}" .
done

#echo "docker stop django-files && docker rm django-files"
#echo "docker run --rm -p 80:80 -v ./django-files:/data/media --name django-files ghcr.io/django-files/django-files:latest"
