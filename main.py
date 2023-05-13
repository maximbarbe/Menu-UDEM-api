import re
import werkzeug.security
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Create the app
app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Index page
@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})