# Package manager targets
.PHONY: initialize_env
initialize_env: 
	bash environment_init.sh

.PHONY: create_env
create_env: 
	poetry install


# Linting targets
.PHONY: lint_check
lint_check:
	poetry run ruff check .

.PHONY: lint_fix
lint_fix: 
	poetry run ruff check --fix .

.PHONY: format
format: 
	poetry run ruff format .

.PHONY: lint_and_format
lint_and_format: lint_fix format


# Pre-commit targets
.PHONY: initialize_precommit
initialize_precommit:
	poetry run pre-commit install --config configs/pre-commit/.pre-commit-config.yaml
	
.PHONY: autoupdate_precommit
autoupdate_precommit:
	poetry run pre-commit autoupdate --config configs/pre-commit/.pre-commit-config.yaml
