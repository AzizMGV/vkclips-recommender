from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="VK Clips Recsys Demo")

class Pair(BaseModel):
    user_id: int
    item_id: int

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(pairs: list[Pair]):
    return {"predictions": [{"user_id": p.user_id, "item_id": p.item_id, "predict": 0.0} for p in pairs]}
