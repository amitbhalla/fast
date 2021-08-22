from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"data": {"name": "Amit"}}


@app.get("/about")
def index():
    return {"data": "This is the about page!"}
