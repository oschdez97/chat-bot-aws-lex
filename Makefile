all: install format lint test

install:
	python3 -m pip install --upgrade pip && \
	python3 -m pip install -r requirements.txt

format:
	black *.py src/*.py

lint:
	pylint --disable=R,C *.py src/*.py

test:
	pytest -vv --cov=main --cov=src tests/*.py

run:
	python3 main.py