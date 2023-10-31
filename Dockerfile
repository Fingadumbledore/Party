FROM python:3-alpine3.18
WORKDIR /app
COPY ./party /app
RUN pip install -r requierements.txt
EXPOSE 5000
RUN python main.py
EXPOSE 5000
