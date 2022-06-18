activate:
	@echo "🦔 | $$(date "+%F %T") | Activating virtual environment..."
	@printf "🦔 | $$(date "+%F %T") | Invoking " 
	poetry shell

install: 
	@echo "🦔 | $$(date "+%F %T") | Installing dependencies..."
	@printf "🦔 | $$(date "+%F %T") | Invoking " 
	poetry install
	@echo ""
	@printf "🦔 | $$(date "+%F %T") | Invoking " 
	poetry run pre-commit install

init: 
	@echo "🦔 | $$(date "+%F %T") | Initializing git..."
	git config --global init.defaultBranch "main"
	git init

setup: init install
	@echo "🦔 | $$(date "+%F %T") | Opening {{cookiecutter.directory_name}} package..."