import re
import werkzeug.security
from fastapi import FastAPI, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordRequestFormStrict
from fastapi_login import LoginManager
from dotenv import load_dotenv
import os
import sqlite3
from forms import RegisterForm

##################################### FASTAPI SETUP ##################################################

user = None

# Create the app
app = FastAPI()

# Fichiers HTML et CSS
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup le manager pour le login de utilisateurs
load_dotenv()
manager = LoginManager(os.environ.get('key'), '/login', use_cookie=True)
manager.cookie_name="udem_cookie"


@manager.user_loader
def load_user():
    pass

########################################################################################################
################################## DATABASE ###########################################################

connection = sqlite3.connect("data.db", check_same_thread=False)
db_cursor = connection.cursor()

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
    return templates.TemplateResponse("register.html", {"request": request, 'errors': None}, )

@app.post("/register", response_class=HTMLResponse)
def post_register_page(request: Request, form_data: RegisterForm = Depends()):
    query="SELECT * FROM users WHERE EMAIL = ?"
    res = db_cursor.execute(query, (form_data.email,))
    if res != []:
        return templates.TemplateResponse("register.html", {"request": request, 'errors': 'EMAIL ALREADY EXISTS'})
    else:
        return templates.TemplateResponse("login.html", {"request": request, "errors": None})
    
@app.post("/login")
def login(user_data: OAuth2PasswordRequestForm = Depends()):
    print(user_data)
    pass
##############################################################################################################