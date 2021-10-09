from datetime import datetime
from fastapi_csv import FastAPI_CSV

app = FastAPI_CSV("data.txt")

@app.get("/")
def root():
    return { "time": datetime.now() }
