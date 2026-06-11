from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Data Analysis API is running 🚀"}

@app.get("/data")
def get_data():
    return {
        "sales": [100, 200, 150, 300],
        "profit": [20, 50, 30, 80]
    }
