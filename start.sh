#!/bin/bash
set -e

# Run database migrations
python manage.py migrate

# Start Gunicorn with the PORT environment variable
# Use a default port if PORT is not set
PORT=${PORT:-8000}
exec gunicorn pdf2img_web.wsgi:application \
    --bind 0.0.0.0:$PORT \
    --workers 2 \
    --timeout 120
