# getting base image
FROM python:3.10
# installing poetry
RUN pip install poetry
# create the /api directory
WORKDIR /api
#copy pyproject to obtain dependencies
COPY pyproject.toml .
#copy api
RUN mkdir src
COPY src/api.py src/
#Install
RUN poetry install
#exposing the port 80
EXPOSE 80
#user
#USER 1000

CMD ["poetry", "run","uvicorn", "src.api:app", "--host", "0.0.0.0", "--port","80"]