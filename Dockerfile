# BUILD
# docker build --tag=my_flask .

FROM python:alpine
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD ["app.py"]
