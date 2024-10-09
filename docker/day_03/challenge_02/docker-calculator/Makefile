IMAGE_NAME = diogoromero/calculator

build:
	docker-compose build

run:
	docker-compose up

push:
	docker tag docker-calculator-calculator $(IMAGE_NAME)
	docker push $(IMAGE_NAME)

exec:
	docker exec -it docker-calculator-calculator /bin/bash

stop:
	docker-compose down
