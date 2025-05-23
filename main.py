from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randint

app = FastAPI()


class Trx(BaseModel):
    ticker: str
    amount: float
    price: float
    trx_type: str | None = "buy"


my_trxs = [
    {"ticker": "AAPL", "amount": 10, "price": 150, "trx_type": "buy", "id": 1},
    {"ticker": "TSLA", "amount": 5, "price": 700, "id": 2},
]


def find_trx(id):
    for t in my_trxs:
        if t["id"] == id:
            return t


@app.get("/")
def root():
    return {"message": "Welcome to my api"}


@app.get("/trxs")
def get_trxs():
    return {"data": my_trxs}


@app.post("/trxs")
def create_trxs(trx: Trx):
    trx_dict = trx.model_dump()
    trx_dict["id"] = randint(1, 1000000)
    my_trxs.append(trx_dict)
    return {"data": trx}


@app.get("/trxs/{id}")
def get_trx(id: int):
    trx = find_trx(id)
    return {"data": trx}
