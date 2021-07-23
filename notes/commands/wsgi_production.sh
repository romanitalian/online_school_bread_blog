#!/bin/bash

gunicorn -w 1 -b 0.0.0.0:8000 --chdir ./src core.wsgi --timeout 60 --log-level debug --max-requests 10000
