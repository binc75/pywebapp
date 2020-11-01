# BUILD
# docker build --tag=my_flask .

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV PORT=5000
ENV MAX_WORKERS=3
ENV WEB_CONCURRENCY=2
EXPOSE 5000
#RUN apk add --update curl && rm -rf /var/cache/apk/*
#ENTRYPOINT [ "python" ]
#CMD ["app.py"]
