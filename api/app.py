from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is working 🚀"}

@app.get("/data")
def data():
    return {
        "sales": [100, 200, 150, 300],
        "profit": [20, 50, 30, 80]
    }
