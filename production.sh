#!/bin/bash
python3 app/load.py && gunicorn -w 4 -b 0.0.0.0:8080 app.api:app
