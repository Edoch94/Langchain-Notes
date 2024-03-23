PKG_MNGR := 
ENV_PATH := ./configs/environment/
ENV_NAME := langchain_notes
PYTHON_VERSION := 3.11


# Package manager targets
.PHONY: initialize_env
initialize_env: 
	bash environment_init.sh

.PHONY: create_env
create_env: 
	$(PKG_MNGR) env create -f $(ENV_PATH)$(ENV_NAME).yaml -y

.PHONY: install_prod_packages
install_prod_packages:
	$(PKG_MNGR) run -n $(ENV_NAME) poetry install --only main

.PHONY: install_all_packages
install_all_packages:
	$(PKG_MNGR) run -n $(ENV_NAME) poetry install


# Linting targets
.PHONY: lint_check
lint_check:
	$(PKG_MNGR) run -n $(ENV_NAME) ruff check .

.PHONY: lint_fix
lint_fix: 
	$(PKG_MNGR) run -n $(ENV_NAME) ruff check --fix .

.PHONY: format
format: 
	$(PKG_MNGR) run -n $(ENV_NAME) ruff format .

.PHONY: lint_and_format
lint_and_format: lint_fix format


# Pre-commit targets
.PHONY: initialize_precommit
initialize_precommit:
	$(PKG_MNGR) run -n $(ENV_NAME) pre-commit install --config configs/pre-commit/.pre-commit-config.yaml
	
.PHONY: autoupdate_precommit
autoupdate_precommit:
	$(PKG_MNGR) run -n $(ENV_NAME) pre-commit autoupdate --config configs/pre-commit/.pre-commit-config.yaml
