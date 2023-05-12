import re
import werkzeug.security
from fastapi import FastAPI

# Create the app
app = FastAPI()


# Index page
@app.get("/")
def index():
    return "<p>Hello World</p>"