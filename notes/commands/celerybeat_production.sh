#!/bin/bash

celery -A core beat --loglevel=info --workdir=/srv/project/src --schedule=/srv/project/tmp/celerybeat-schedule
