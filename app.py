from fastapi import FastAPI, Request, Query
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()
API = os.getenv("API_KEY")

app = FastAPI()

# Enable CORS (optional for frontend integration)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static and templates folders
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# HTML home route
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# API: Get countries
@app.get("/api/countries")
async def get_countries():
    r = requests.get(f"{API}/countries")
    return JSONResponse(content=r.json())

# API: Get stations by country
@app.get("/api/stations")
async def get_stations(country: str = Query(...)):
    r = requests.get(f"{API}/stations/bycountry/{country}")
    return JSONResponse(content=r.json())
