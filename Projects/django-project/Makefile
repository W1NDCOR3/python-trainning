makemigrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

collectstatic:
	poetry run python manage.py collectstatic

run: collectstatic makemigrations migrate
	poetry run python manage.py runserver