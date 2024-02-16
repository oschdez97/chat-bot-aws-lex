all: install format lint test build

install:
	python3 -m pip install --upgrade pip && \
	python3 -m pip install -r requirements.txt

format:
	black *.py src/*.py

lint:
	pylint --disable=R,C *.py src/*.py

test:
	pytest -vv --cov=src tests/*.py

build:
	docker build -t deploy-fastapi .