from fastapi import FastAPI
from scraper import scrape_influencer
from database import init_db, get_profile, get_posts, get_reels
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()

@app.get("/scrape")
def scrape():
    try:
        scrape_influencer()
        return {"message": "Scraped and saved data"}
    except Exception as e:
        print(f"Error in scrape endpoint: {str(e)}")
        return {"error": str(e)}

@app.get("/profile")
def profile():
    return get_profile()

@app.get("/posts")
def posts():
    return get_posts()

@app.get("/reels")
def reels():
    return get_reels()