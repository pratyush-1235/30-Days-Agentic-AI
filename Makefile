.PHONY: install lint test format clean run-day

install:
	pip install -r requirements.txt

lint:
	ruff check .

format:
	ruff format .

test:
	pytest -v

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} +

# Usage: make run-day DAY=07
run-day:
	cd Day-$(DAY)*/code && python main.py
