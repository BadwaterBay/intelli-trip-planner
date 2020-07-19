#!/bin/bash

# Please see .env.example file at the root level for initial setup

export FLASK_APP=./src/app.py
flask run --port 5000
