IMAGE_NAME = diogoromero/calculator

build:
	docker-compose build

run:
	docker-compose up -d

enter_calculator:
	docker exec -it docker-calculator-calculator-1 python /app/calculator.py


enter_postgres:
	docker exec -it docker-calculator-postgres-1 psql -U calcuser -d calcdb -c "SELECT * FROM results;"

push:
	docker tag docker-calculator_calculator $(IMAGE_NAME)
	docker push $(IMAGE_NAME)

stop:
	docker-compose down
