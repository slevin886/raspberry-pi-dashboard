#!/usr/bin/env python
from home_helper import create_app
import os

settings = os.environ.get('APP_SETTINGS')

if settings == 'production':
    app = create_app(settings='production')
else:
    app = create_app(settings='development')


if __name__ == '__main__':
    app.run()
