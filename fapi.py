from fastapi import FastAPI

ok = FastAPI()


@ok.get("/")
async def root():
    return {"message": "Hello World"}