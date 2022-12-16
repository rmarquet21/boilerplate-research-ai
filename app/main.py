import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(
    title="API Title",
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
