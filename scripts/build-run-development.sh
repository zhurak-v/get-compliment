#!/bin/bash

set -e

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
APP_PATH="$PROJECT_ROOT/src"

export PYTHONPYCACHEPREFIX="$PROJECT_ROOT/__pycache__"

export APP_ENV="development"

export PYTHONPATH="$APP_PATH:$PYTHONPATH"

cd "$APP_PATH"

python -m application.main