.PHONY: help

export PYTHONPATH=$(shell pwd)/
export PYTHONDONTWRITEBYTECODE=1

help:  ## This help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@rm -f .coverage
	@rm -rf .cache/
	@rm -rf htmlcov/
	@rm -f coverage.xml
	@rm -f *.log

dependencies:
	@pip install pipenv
	@pipenv lock
	@pipenv install . --dev

flake:
	@pipenv run flake8 --max-line-length=79 awsenviron.py

isort:  ## Check imports
	@pipenv run isort --recursive --diff --check-only awsenviron.py tests

fix-imports:  ## Fix imports
	@pipenv run isort --recursive awsenviron.py tests

lint: flake isort  ## Run code lint

cov-tests: clean  ## Run coverage tests
	@pipenv run py.test --cov awsenviron --cov-report=term-missing --cov-report=html:htmlcov

tests: clean  ## Run tests
	@pipenv run py.test -vv tests/

release-draft: ## Show new release changelog
	@pipenv run towncrier --draft

 release-patch: ## Create patch release
	@pipenv run bumpversion patch --dry-run --no-tag --no-commit --list | grep new_version= | sed -e 's/new_version=//' | xargs -n 1 pipenv run towncrier --yes --version
	@git commit -am 'Update CHANGELOG'
	@pipenv run bumpversion patch

 release-minor: ## Create minor release
	@pipenv run bumpversion minor --dry-run --no-tag --no-commit --list | grep new_version= | sed -e 's/new_version=//' | xargs -n 1 pipenv run towncrier --yes --version
	@git commit -am 'Update CHANGELOG'
	@pipenv run bumpversion minor

 release-major: ## Create major release
	@pipenv run bumpversion major --dry-run --no-tag --no-commit --list | grep new_version= | sed -e 's/new_version=//' | xargs -n 1 pipenv run towncrier --yes --version
	@git commit -am 'Update CHANGELOG'
	@pipenv run bumpversion major

publish:  ## Publish on pypi
	@pipenv run python setup.py sdist bdist_wheel upload
	@rm -fr build dist .egg awsenviron.egg-info
