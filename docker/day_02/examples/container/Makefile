local:
	poetry run uvicorn src.api:app --host 0.0.0.0 --port 80
build-api:
	docker build -t api-f ops/api.Dockerfile .
run-api: build-api
	docker run -it --rm -p 8080:80 api $(command)
