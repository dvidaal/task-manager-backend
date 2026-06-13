from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡Hola, mi Kanban Backend está vivo!"}

@app.get("/status")
def get_status():
    return {"status": "ok", "database": "Pronto la conectaremos"}
