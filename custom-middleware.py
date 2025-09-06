from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
import time

app = FastAPI()

class TimerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        duration = time.timer - start_time
        print(f'{duration} seconds')

app.middleware(TimerMiddleware)

@app.get('/hello')
async def hello():
    for _ in range(1001029):
        pass
    return{"message":"Hello World!"}

