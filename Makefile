venv_create:
	python3.10 -m venv venv

pip_install:
	pip install -r requirements.txt

pip_update_requirements:
	pip freeze > requirements.txt

test:
	pytest tests
