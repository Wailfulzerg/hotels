export PYTHONPATH=src:.

ENV ?= dev
ENV_FILE = envs/$(ENV)/.env
include $(ENV_FILE)
export

COMPOSE_PROJECT_NAME = api_service_$(ENV)
PYTEST_TARGET ?= tests

start-env:
	docker-compose -p $(COMPOSE_PROJECT_NAME) --env-file envs/$(ENV)/.env -f envs/docker-compose.yml -f envs/$(ENV)/docker-compose.yml --profile app up -d --force-recreate --build

stop-env:
	docker-compose -p $(COMPOSE_PROJECT_NAME) --env-file envs/$(ENV)/.env -f envs/docker-compose.yml -f envs/$(ENV)/docker-compose.yml --profile app  stop

clear-env:
	docker-compose -p $(COMPOSE_PROJECT_NAME) --env-file envs/$(ENV)/.env -f envs/docker-compose.yml -f envs/$(ENV)/docker-compose.yml --profile app  down
	docker system prune -f

restart-apps:
	docker-compose -p $(COMPOSE_PROJECT_NAME) --env-file envs/$(ENV)/.env -f envs/docker-compose.yml -f envs/$(ENV)/docker-compose.yml --profile app up -d --force-recreate

cs:
	autoflake . && black . && isort .
