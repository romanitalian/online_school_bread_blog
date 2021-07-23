#!/bin/bash

celery -A core worker --loglevel=info --workdir=/srv/project/src
