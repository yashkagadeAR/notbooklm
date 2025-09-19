# FastAPI entrypoint for OpenNotebook backend
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

# Placeholder for /query endpoint
@app.post("/query")
def query(user_id: str, notebook_id: str, prompt: str):
    # ...implement retriever, agent orchestration...
    return {"result": "Not implemented"}
