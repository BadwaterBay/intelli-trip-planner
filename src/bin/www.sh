#!/bin/bash

export FLASK_ENV=development
export FLASK_APP=./src/app.py
flask run --port 5000
