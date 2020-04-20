## Python Webapp REST API
Simple Python REST API for testing.

Everytime I needed to test something on K8S I was looking for a simple application that returns some values in JSON like:
 * fixed message ("Hello World")
 * hostname (OS, container or pod name)
 * kernel info
 * **version string coming from env variable**
 * date
 * HTTP headers 
 * cookie creation 

In order to keep things simple I've used Flask and the integrated Webserver so that this is absolutely not intended to be use in any production environment. 

## How to use it
### Plain Python 
```bash
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
Query the API:
```bash
curl http://localhost:5000/
curl http://localhost:5000/date
```

### Docker
First build the container image:
```bash
docker build --tag=nbianchi/pywebapp:v0.1 .
```
Run the container (passing the env variable "VERSION")
```bash
docker run -p 5000:5000 -e "VERSION=v100" nbianchi/pywebapp:v0.1
```

Query the API:
```bash
curl http://localhost:5000/
curl http://localhost:5000/version
curl http://localhost:5000/date
```

#### Docker Repo push
```bash
docker build --tag=nbianchi/pywebapp:v0.1 .
docker push nbianchi/pywebapp:v0.1
```

### Kubernetes 
Simple deployment example to deploy on K8S.
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: backend-v1
spec:
  replicas: 3
  selector:
    matchLabels:
      app: backend
      version: v1
  template:
    metadata:
      labels:
        app: backend
        version: v1
    spec:
      containers:
      - image: nbianchi/pywebapp
        imagePullPolicy: Always
        env:
        - name: VERSION
          value: "v1"
        name: python
        resources:
          limits:
            cpu: 100m
            memory: 100Mi
---
apiVersion: v1
kind: Service
metadata:
  labels:
    app: backend
  name: backend
spec:
  ports:
  - port: 80
    name: http
    targetPort: 5000
    protocol: TCP
  selector:
    app: backend
  type: ClusterIP
```
