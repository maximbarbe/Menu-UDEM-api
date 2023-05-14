import re
import werkzeug.security
from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordRequestFormStrict
from fastapi_login import LoginManager
from dotenv import load_dotenv
import os
import sqlite3

##################################### FASTAPI SETUP ##################################################
# Create the app
app = FastAPI()

# Fichiers HTML et CSS
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup le manager pour le login de utilisateurs
load_dotenv()
manager = LoginManager(os.environ.get('key'), '/login')


########################################################################################################
################################## DATABASE ###########################################################

connection = sqlite3.connect("data.db")
db_cursor = connection.cursor()
user = None
# def get_user(user_id) -None:
#     user = db_cursor.execute(sql)



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