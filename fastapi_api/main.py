from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class HelloData(BaseModel):
    name: str | None = None
    message: str | None = None

@app.get("/hello")
def get_hello():
    return {"message": "Hello from FastAPI!"}

@app.post("/hello", status_code=201)
def create_hello(data: HelloData):
    name = data.name if data.name else "sem nome"
    return {"message": f"Hello, {name}!"}

@app.put("/hello")
def update_hello(data: HelloData):
    return {"updated_message": data.message or "mensagem padrão"}

@app.delete("/hello")
def delete_hello():
    return {"message": "Recurso deletado (simulação)"}
