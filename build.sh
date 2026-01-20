#!/usr/bin/env bash
set -e

# Force Python 3.11
export PYENV_VERSION=3.11.7

python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt

echo "Build complete!"
