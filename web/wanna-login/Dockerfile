FROM python:3.11-slim

WORKDIR /app

COPY challenge/app .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 1337

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=1337"]
