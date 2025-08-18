#!/bin/bash

set -e

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
APP_PATH="$PROJECT_ROOT/src"

export PYTHONPYCACHEPREFIX="$(dirname "$APP_PATH")/__pycache__"
export APP_ENV="development"

cd "$APP_PATH"

python -m application.main