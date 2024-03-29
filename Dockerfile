FROM python:3.11


WORKDIR /app
RUN pip install pipenv
COPY Pipfile.lock Pipfile ./
RUN pipenv install --deploy --system --dev

COPY . .

CMD [ "python", "run_service.py"]