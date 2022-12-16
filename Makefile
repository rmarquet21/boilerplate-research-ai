.DEFAULT_GOAL := help
.PHONY: help
help: ## provides cli help for this makefile (default)
	@grep -E '^[a-zA-Z_0-9-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: setup
setup: ## first time project setup
	poetry config virtualenvs.in-project true
	poetry install
	poetry shell

.PHONY: install
install: ## install all dependencies
	poetry install

.PHONY: update
update: ## update all dependencies
	poetry update

.PHONY: jupyter-lab
jupyter-lab: ## open jupyter-lab in notebooks folder
	jupyter lab

.PHONY: start-api
start-api: ## start api
	python app/main.py

.PHONY: start-db
start-db: ## start db
	docker-compose -f docker/docker-compose.yml up -d postgres

.PHONY: stop-db
stop-db: ## stop db
	docker-compose -f docker/docker-compose.yml down

.PHONY: start-metabase
start-metabase: ## start metabase
	docker-compose -f docker/docker-compose.yml up -d metabase

.PHONY: stop-metabase
stop-metabase: ## stop metabase
	docker-compose -f docker/docker-compose.yml down