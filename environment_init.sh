#!/usr/bin/sh

echo "Creating environment"
pyenv install -s 3.11
pyenv local 3.11
poetry env use 3.11
poetry install --no-root

if git rev-parse --is-inside-work-tree > /dev/null 2>&1; then
    echo "Initializing pre-commit"
    poetry run pre-commit install --config configs/pre-commit/.pre-commit-config.yaml
    poetry run pre-commit autoupdate --config configs/pre-commit/.pre-commit-config.yaml
else
    echo "Folder is not a git repository: pre-commit not initialized"
fi