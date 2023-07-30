"""
Multi-instance app test
=======================

Server
------

Server script that will generate expensive computaitons.
"""

import uuid

from fastapi import FastAPI


def expensive_function():
    """Simulate a long-running function."""
    ul = [uuid.uuid4() for _ in range(1000)]
    return ul[-1]


def inexpensive_function():
    """Simulate a short-running function."""
    return 'Hello World!'


app = FastAPI()

@app.get('/')
def index():
    """Default server endpoint."""
    msg = inexpensive_function()
    return {'message': msg}
