from fastapi import FastAPI

app = FastAPI()
@app.get("/welcome")
def welcome():
    return {
        "message":"Mini RAG App is running"
    }