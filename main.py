from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {'The fastAPI app works!'}
