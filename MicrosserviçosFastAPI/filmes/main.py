from fastapi import FastAPI

app = FastAPI()

@app.get("/filmes/{id}")
def get_ingressos(id: int):
    return {
        "id": id,
        "titulo": "Filme Exemplo",
        "genero": "Suspense"
    }