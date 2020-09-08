#!/usr/bin/env python

"""
# Entry point of API
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hellow World! The server is running."
