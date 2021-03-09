#!/usr/bin/env bash

set -euxo pipefail

echo "Running linters and formatters..."

isort democritus_csv/ tests/

black democritus_csv/ tests/

mypy democritus_csv/ tests/

pylint --fail-under 9 democritus_csv/*.py

flake8 democritus_csv/ tests/

bandit -r democritus_csv/

# we run black again at the end to undo any odd changes made by any of the linters above
black democritus_csv/ tests/
