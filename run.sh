#!/bin/bash
set -e

NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program gunicorn --worker-class gevent -w 3 --log-level=error -b 0.0.0.0:8000 mysite.wsgi