from fastapi import FastAPI, Depends, Form, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

@app.post('/token')
def login(username : str = Form(...), password: str = Form(...)):
    if username == 'shubham' and password == 'pass123':
        return {'access_token':'valid_token', 'token_type':'bearer'}
    raise HTTPException(status_code=400, detail='Invalid Credentials')

def decode_token(token:str):
    if token == 'valid_token':
        return {'name':'shubham'}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                        detail='invalid credentials')

def get_curent_user(token: str = Depends(oauth2_scheme)):
    return decode_token(token)


@app.get('/profile')
def get_profile(user = Depends(get_curent_user)):
    return {'username': user['name']}