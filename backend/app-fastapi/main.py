from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}

# execute the command on bash terminal: uvicorn main:app --reload
