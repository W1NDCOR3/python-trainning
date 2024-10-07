build:
	docker build -t nginx-page:latest .

bash: build
	docker run -it --rm nginx-page:latest sh

run: build	
	docker run -p 8080:80 nginx-page:latest
	