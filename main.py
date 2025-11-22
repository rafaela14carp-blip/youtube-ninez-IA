from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok", "message": "youtube-ninez-IA funcionando correctamente"}
