from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    # return "Hare Krishna!"
    return {"data": {"name": "Aaryan Jaydeep Apte"}}


@app.get('/about')
def going_deep():
    return "About page!"
