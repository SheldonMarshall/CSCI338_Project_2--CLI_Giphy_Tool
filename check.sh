#!/bin/bash


# I asked ChatGPT and it provided the following command located on lines 5-6#
# Enable strict mode:
set -e

poetry run black --check *.py
poetry run isort --check *.py
poetry run flake8 *.py

# If all we get to this point(We havn't exited due to a failed test) we have passed all tests
echo "All tests passed!"
