build:
	docker build -t fastapi-app .

bash: build
	docker run -it --rm fastapi-app bash

run: build	
	docker run -it --rm -p 8000:8000 fastapi-app fastapi
	