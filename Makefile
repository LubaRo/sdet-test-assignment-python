venv_create:
	python3.10 -m venv venv

pip_install:
	pip install -r requirements.txt

pip_update_requirements:
	pip freeze > requirements.txt

test:
	pytest tests

test_and_report:
	pytest --alluredir=./allure_reports tests

watch_report:
	allure serve  allure_reports/
