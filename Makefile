name := app_name

deps:  # Установка зависимостей
	pip install flake8 flask-sqlalchemy flask-wtf flask waitress flask-bcrypt

lint:  $(name) # Проверка на pep8
	flake8 $(name)

push:  # Пуш кода на гитхаб
	git push && git push --tags

db-init: $(name)
	flask --app $(name) db init

db: $(name)
	flask --app $(name) db migrate
	flask --app $(name) db upgrade

test:  # Тесты
	echo "Реализуй"

debug: $(name)
	flask --app $(name) --debug run

deploy: $(name) lint
	waitress-serve --port=8080 --call $(name):create_app