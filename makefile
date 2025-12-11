.PHONY: clean
.PHONY: format
.PHONY: format-check
.PHONY: install-dev
.PHONY: install-prod
.PHONY: lint-check
.PHONY: test

clean:
	rm -rf dist/ logs/ .venv/

format:
	uv run black src

format-check:
	uv run black --check src

install-dev:
	uv sync

install-prod:
	uv sync --no-dev

lint-check:
	uv run pylint src

test:
	uv run pytest
