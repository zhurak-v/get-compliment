#!/bin/bash

APP_PATH="$(cd "$(dirname "$0")/../src" && pwd)"

export APP_PATH
export PYTHONPYCACHEPREFIX="$(dirname "$APP_PATH")/__pycache__"
export APP_ENV="development"

cd "$APP_PATH"

python -m application.main