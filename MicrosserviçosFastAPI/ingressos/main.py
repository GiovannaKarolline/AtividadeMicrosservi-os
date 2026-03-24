from fastAPI import FastAPI
import requests
import os

app = FastAPI()

FILMES_URL = os.getenv("FILMES_URL")

@app.get("/ingressos/{id}")
def get_id(id:int):
    try:
        response = requests.get(f"{FILMES_URL}/filmes/{id}", timeout=2)
        cliente = response.json()
    except Exception:
        cliente = {"erro":"Serviço de filmes indisponível"}
    return{
        "id": id,
        "comprador":"nome",
        "cliente":cliente;
    }