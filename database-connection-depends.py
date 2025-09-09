from fastapi import FastAPI, Depends

app = FastAPI()

def get_db():
    # connection string logic
    db = {'connection':'connection_str_mock'}
    try:
        yield db
    finally:
        db.close()

@app.route('/home')
def home(db=Depends(get_db)):
    return {'db_status': db["connection"]}