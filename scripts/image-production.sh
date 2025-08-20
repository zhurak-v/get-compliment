#!/bin/bash

set -e

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DOCKER_DIR="$PROJECT_ROOT/docker"

GIT_HASH=$(git -C "$PROJECT_ROOT" rev-parse --short HEAD)
TAG="python-get-compliment-image:$GIT_HASH"

docker build -t "$TAG" -f "$DOCKER_DIR/dockerfiles/Development.Dockerfile" "$PROJECT_ROOT"

if [ "$(docker ps -aq -f name=python-get-compliment)" ]; then
  docker stop python-get-compliment
  docker rm python-get-compliment
fi

docker run -d -p 7777:7777 --name python-get-compliment "$TAG"