#!/bin/bash


echo "-------------------------- SERVER_MODE: $(SERVER_MODE)"

if "$SERVER_MODE" == "dev"
then
  echo "Run dev wsgi-server"
  make run
else
  echo "Run production wsgi-server"
  make gunicorn-run
fi
