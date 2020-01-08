#!/usr/bin/env bash

echo "Deleting migrations..."

# Deletes only xxxx_migrationdetails.py files
# Verbose but gets the job done
find `find . -type d -name migrations -not -path "./venv/*"` ! -name '__init__.py' -type f ! -path '*__pycache__/*' -exec rm -f {} \;

echo "Sucessfully deleted migrations..."
