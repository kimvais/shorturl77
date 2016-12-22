dev-env:
	pip install -U pip-tools
	pip-compile
	pip-sync
