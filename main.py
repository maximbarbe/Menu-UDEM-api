from werkzeug.security import generate_password_hash
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
from helpers import check_password_validity

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

#######################################################################################################
################################### User Class ########################################################

class User:
    def __init__(self, user_id, username, email, role):
        self.id = user_id
        self.username = username
        self.email = email
        self.role = role


###################################### ROUTES ###############################################################
# Index page
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    # Retourner la page d'accueil.
    return templates.TemplateResponse("index.html", {"request": request, 'user': user})

@app.get("/login")
async def get_login_page():
    return {"Hello": "World"}

@app.get("/register", response_class=HTMLResponse)
async def get_register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request, 'errors': None, 'form_data': None}, )

@app.post("/register", response_class=HTMLResponse)
async def post_register_page(request: Request, form_data: RegisterForm = Depends()):
    query="SELECT * FROM users WHERE EMAIL = ?"
    res = db_cursor.execute(query, (form_data.email.lower(),))
    if res.fetchall() != []:
        return templates.TemplateResponse("register.html", {"request": request, 'errors': 'Email déjà existant, veuillez réessayer.', 'form_data': form_data})
    else:
        if len(form_data.username) < 6:
            return templates.TemplateResponse("register.html", {"request": request, 'errors': "Nom d'utilisateur trop court. Il devrait contenir au moins 6 caractères.", 'form_data': form_data})
        if form_data.password != form_data.confirmed_password:
            return templates.TemplateResponse('register.html', {"request": request, 'errors': 'Les mots de passes ne correspondent pas.', 'form_data': form_data})
        if not check_password_validity(form_data.password):
            return templates.TemplateResponse('register.html', {"request": request, 'errors': 'Le mot de passe doit contenir au moins 8 caractères dont au moins 1 lettre majuscule, 1 lettre minuscule, 1 chiffre et 1 caractère spécial.', 'form_data': form_data})
        query="INSERT INTO users VALUES(?, ?, ?, ?, 'MEMBER')"
        pw = generate_password_hash(password=form_data.password, method="pbkdf2:sha256", salt_length=8)
        db_cursor.execute(query, (None, form_data.username, form_data.email.lower(), pw,))
        connection.commit()
        return templates.TemplateResponse("register.html", {"request": request, 'errors': 'SUCCESS'})
    
@app.post("/login")
async def login(user_data: OAuth2PasswordRequestForm = Depends()):
    print(user_data)
    pass
##############################################################################################################