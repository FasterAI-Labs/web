from fasthtml.common import *
from monsterui.all import *
from datetime import datetime
from config import COMPANY_NAME, COMPANY_TAGLINE
from app import app, rt
from routes import about, team, index, blog, compress
from utils import *
from components.menu import *
from components.footer import *



if __name__ == "__main__":
    serve()
