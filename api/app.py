from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API running 🚀"}

@app.get("/data")
def data():
    return {
        "sales": [100, 200, 150, 300]
    }
