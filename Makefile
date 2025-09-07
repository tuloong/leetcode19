"""Makefile for common development tasks."""

.PHONY: help install install-dev test test-unit test-integration lint format type-check clean build docs

help:
	@echo "Available commands:"
	@echo "  install      Install the package"
	@echo "  install-dev  Install development dependencies"
	@echo "  test         Run all tests"
	@echo "  test-unit    Run unit tests only"
	@echo "  test-integration Run integration tests only"
	@echo "  lint         Run linting"
	@echo "  format       Format code"
	@echo "  type-check   Run type checking"
	@echo "  clean        Clean build artifacts"
	@echo "  build        Build the package"
	@echo "  docs         Generate documentation"
	@echo "  run-examples Run example scripts"

install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"
	pre-commit install

test:
	pytest

test-unit:
	pytest tests/unit/

test-integration:
	pytest tests/integration/

test-coverage:
	pytest --cov=src/leetcode19 --cov-report=html --cov-report=term-missing

lint:
	flake8 src/ tests/

format:
	black src/ tests/

type-check:
	mypy src/

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build:
	python -m build

docs:
	@echo "Documentation generation not implemented yet"
	@echo "Will be added when sphinx documentation is set up"

run-examples:
	python examples/usage_examples.py

demo:
	python -m leetcode19.cli --examples

interactive:
	python -m leetcode19.cli --interactive

benchmark:
	python -m leetcode19.cli --nums "1,2,3,4,5,6,7,8,9,10" --target 19 --benchmark

check: lint type-check test
	@echo "All checks passed!"

dev-setup: install-dev
	@echo "Development environment setup complete!"
	@echo "Don't forget to run 'pre-commit install' if you haven't already"