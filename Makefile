include .env
export $(shell sed 's/=.*//' .env)
MANAGE = python src/manage.py
BACKEND_CONTAINER = backend
PROJECT_DIR=$(shell pwd)
WSGI_PORT=8000
RUN_COMMAND=gunicorn-run

help : Makefile
	@echo "+--------------------+"
	@echo "| AVAILABLE COMMANDS |"
	@echo "+--------------------+\n"
	@echo "REGULAR\n"
	@cat Makefile | grep "##" | grep -v "docker" | sed -n 's/^## /make /p' | column -t -s ':' && echo ""
	@echo "DOCKER\n"
	@cat Makefile | grep "##" | grep "docker" | sed -n 's/^## /make /p' | column -t -s ':' && echo ""

## run: run local (broadcast) server
run:
	$(MANAGE) runserver 0.0.0.0:$(WSGI_PORT)
	#open "http://127.0.0.1:$(WSGI_PORT)"

celery-run:
	cd src && celery -A core worker -l INFO

celerybeat-run:
	cd src && celery -A core beat -l INFO

## new-migrate: create new migration files by changes in models.
new-migrate:
	$(MANAGE) makemigrations

## migrate: apply migrations to storage (DB).
migrate:
	$(MANAGE) migrate

## check: check Django project.
check:
	$(MANAGE) check

## urls: show urls list.
urls:
	$(MANAGE) show_urls

rates_generate:
	$(MANAGE) rates_generate

posts_fetch:
		$(MANAGE) posts_fetch

posts_tr:
		$(MANAGE) posts_tr

## check-migrate: check Django migrations.
check-migrate:
	$(MANAGE) makemigrations --check --dry-run

## lint: do static code analyse.
lint:
	flake8 ./blog

## shell: open Django shell with autoloading of the apps database models and subclasses of user-defined classes.
shell:
	$(MANAGE) shell_plus --print-sql

createsuperuser:
	$(MANAGE) createsuperuser

gunicorn-run:
	gunicorn -w 1 -b 0.0.0.0:$(WSGI_PORT) --chdir $(PROJECT_DIR)/src core.wsgi --timeout 60 --log-level debug --max-requests 10000

gunicorn-run-8082:
	gunicorn -w 4 -b 0.0.0.0:8082 --chdir $(PROJECT_DIR)/src core.wsgi --timeout 30 --log-level debug --max-requests 10000

gunicorn-sock:
	gunicorn -w 4 -b unix:/tmp/gunicorn.sock --chdir $(PROJECT_DIR)/src core.wsgi --timeout 30 --log-level info --max-requests 10000

# docker exec -it bread-backend python ./src/manage.py collectstatic --noinput
# docker cp bread-backend:/tmp/static_content/static /tmp/static
# docker cp /tmp/static nginx:/var/bread-static

collect-static:
	$(MANAGE) collectstatic

test-run:
	cd src && pytest

tst:
	cd src && pytest
	#open static_content/coverage/index.html

## docker-run-dev: run project in dockers ("dev" mode).
docker-run-dev:
	$(eval RUN_COMMAND=run)
	docker-compose up --build
	make copy-static

## docker-run-production: run project in dockers ("production" mode).
docker-run-production: docker-down
	$(eval RUN_COMMAND=gunicorn-run)
	docker-compose up --build

## docker-down: stop docker containers.
docker-down:
	docker-compose down

docker-copy-static:
	docker exec -it bread-backend python ./src/manage.py collectstatic --noinput
	docker cp bread-backend:/tmp/static_content/static /tmp/static
	docker cp /tmp/static nginx:/etc/nginx

# for breakpoint()
docker-runserver-breakpoint:
	docker exec -it $(BACKEND_CONTAINER) $(MANAGE) runserver 0.0.0.0:9000

docker-new-migrate:
	docker exec -it $(BACKEND_CONTAINER) $(MANAGE) makemigrations

docker-migrate:
	docker exec -it $(BACKEND_CONTAINER) $(MANAGE) migrate

docker-createsuperuser:
	docker exec -it $(BACKEND_CONTAINER) $(MANAGE) createsuperuser

# User.objects.all().values('username', 'email')
docker-shell_plus:
	docker exec -it $(BACKEND_CONTAINER) $(MANAGE) shell_plus --print-sql
