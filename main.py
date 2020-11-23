#!/usr/local/env python3

#
# Utilities RestAPI
#  run w/: uvicorn main:app --reload


# Import modules
import datetime
import os
from typing import Optional
from fastapi import FastAPI, Request, Response, Cookie, HTTPException
from pydantic import BaseModel


# Initialize app
app = FastAPI(title="Pywebapp", description="Utility RestAPI", version="0.9")

# Vars
appVersion = os.environ.get("VERSION")
author = "bianchi.nicola@gmail.com"
app.flakycounter = 1


# Datamodel
class PayloadExample(BaseModel):
    name: str
    description: Optional[str] = None
    price: float


# Routes
@app.get("/")
def hello_world():
    '''Return basic informations'''

    myHostName = os.uname()
    output = {
        'message': 'Hello World!',
        'sysinfo': myHostName,
        'version': appVersion,
        'author': author,
    }

    return output


@app.get("/version")
def get_version():
    '''Return app version from ENV variable named VERSION'''

    output = {"version": appVersion}

    return output


@app.get("/headers")
def get_headers(request: Request):
    '''Return client request HTTP headers'''

    output = request.headers

    return output


@app.get("/date")
def get_date():
    '''Return current date'''

    output = {
        'date': str(datetime.date.today()),
        'time': str(datetime.datetime.now()).split(' ')[1]
    }

    return output


@app.get("/cookie")
def get_cookie(response: Response, canary: Optional[str] = Cookie(None)):
    '''
    Return cookie from client request
    test: curl -v --cookie "canary=betatester" http://127.0.0.1:8000/cookie
    '''
    # If not cookie "canary" is found, set it
    if not canary:
        response.set_cookie(key="canary", value="betatester", max_age=60 * 60)
        output = {"message": "no canary cookie set yet, setting now!"}
    else:
        # If cookie "canary" is present, return it.
        output = {"message": f"canary cookie value: {canary}"}

    return output


@app.post("/payload/{name}")
def read_payload(name: str,
                 payload: PayloadExample,
                 q1: Optional[str] = None,
                 q2: Optional[bool] = False):
    '''Return post payload & parameters'''

    return {"item_id": name, "q1": q1, "q2": q2, "payload": payload}


@app.get("/flaky")
def flaky_endpoint():
    '''Flaky endpoint that return random HTTP errors'''

    # Define rate for errors
    # 1 = 100% success rate
    # 2 = 50% success rate
    # 3 = 33% success rate
    # 4 = 25% success rate
    divider = 3

    # If counter is divisible by divider return HTTP 2000
    if app.flakycounter % divider == 0:
        app.flakycounter += 1
        print(app.flakycounter)
        return {"message": "flaky but working this time"}
    else:
        # If counter it's not divisible by divider return HTTP 500 (with rise)
        app.flakycounter += 1
        print(app.flakycounter)
        raise HTTPException(status_code=503, detail="Flaky")
