all: install format lint test build deploy

install:
	pip install --upgrade pip && \
	pip install -r requirements.txt

format:
	black *.py src/*.py

lint:
	pylint --disable=R,C *.py src/*.py

test:
	pytest -vv --cov=src tests/*.py

build:
	docker build -t deploy-fastapi .

deploy:
	aws ecr get-login-password --region eu-west-3 | docker login --username AWS --password-stdin 841032453446.dkr.ecr.eu-west-3.amazonaws.com
	docker build -t fastapi-gdc-lexbot .
	docker tag fastapi-gdc-lexbot:latest 841032453446.dkr.ecr.eu-west-3.amazonaws.com/fastapi-gdc-lexbot:latest
	docker push 841032453446.dkr.ecr.eu-west-3.amazonaws.com/fastapi-gdc-lexbot:latest