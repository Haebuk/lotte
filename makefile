.PHONY: run
run:
	poetry run python -m src.main

.PHONY: runf
runf:
	poetry run python -m src.$(f)

.PHONY: test
test:
	poetry run python -m pytest --cov-report term-missing --cov=src tests
