# BUILD
# docker build --tag=my_flask .

FROM python:alpine
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN apk add --update curl && rm -rf /var/cache/apk/*
ENTRYPOINT [ "python" ]
CMD ["app.py"]
