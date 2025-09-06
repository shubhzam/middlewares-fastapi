from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'http:loaclhost:3000' # used to make connections with frontend
    ],
    allow_credentials=True,
    allow_methods = ['GET','POST','PUT','DELETE'],
    allow_headers=['*']
)

# define 