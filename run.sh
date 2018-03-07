#!/bin/bash
gunicorn --bind 0.0.0.0:5000 --workers 8 main:app
