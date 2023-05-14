import re
import werkzeug.security
from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordRequestFormStrict
from fastapi_login import LoginManager



##################################### FASTAPI SETUP ##################################################
# Create the app
app = FastAPI()

# Fichiers HTML et CSS
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
########################################################################################################




###################################### ROUTES ###############################################################
# Index page
@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/login")
def get_login_page():
    return {"Hello": "World"}

@app.get("/register", response_class=HTMLResponse)
def get_register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@app.post("/login")
def login(user_data: OAuth2PasswordRequestForm = Depends()):
    print(user_data)
    pass
##############################################################################################################