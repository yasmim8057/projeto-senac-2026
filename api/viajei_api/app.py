from http import HTTPStatus

from fastapi import FastAPI

from viajei_api.schemas import Message


app = FastAPI()


@app.get("/", 
        status_code=HTTPStatus.ACCEPTED, 
        response_model=Message)
def bem_vindo():
    return {"message": "Bem vindo!"}


@app.get("/hello")
def ola_mundo():
    return """
        <head>
        </head>
        <body>
            <h1> </h1>
        </body>
"""
