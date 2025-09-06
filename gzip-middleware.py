from fastapi import FastAPI
from starlette.middleware.gzip import GZipMiddleware

app = FastAPI()

app.add_middleware(
    GZipMiddleware, minimum_size = 1000 #enduser needs a large amount of output
)

#endpoints