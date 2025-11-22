from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "youtube-ninez-IA funcionando"}
