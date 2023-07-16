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


app = FastAPI()

@app.get('/')
def index():
    """Default server endpoint."""
    msg = expensive_function()
    return {'message': msg}
