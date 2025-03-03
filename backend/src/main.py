from fastapi import FastAPI

app = FastAPI()
app.title = "Backend Frame - 2024"
app.version = "0.0.1"

@app.get("/")
def root():
    return {"message": "FastAPI funcionando correctamente..."}
