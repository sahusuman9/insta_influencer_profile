# Instagram Influencer Profile App

This is a full-stack web application that displays an Instagram influencer's profile, analytics, recent posts, and reels with basic analysis.

## Assumptions
- Hardcoded for @therock (public profile).
- Scraping uses instaloader for public data only.
- Analysis is simplified (dummy logic for tags/vibe).
- No authentication or production optimizations.
- Frontend uses Tailwind CSS for styling.

## Setup Instructions

### Backend
1. Navigate to `backend/`.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run: `uvicorn app:app --reload`.
   - Access API at http://127.0.0.1:8000 (e.g., /profile, /posts).

### Frontend
1. Navigate to `frontend/`.
2. Install dependencies: `npm install`.
3. Run: `npm start`.
   - Opens at http://localhost:3000.
   - Fetches data from backend on load.

## Usage
- On load, it scrapes and displays data.
- Responsive design with Tailwind CSS.

## Technologies
- Backend: FastAPI, Instaloader, OpenCV, SQLite.
- Frontend: React, Tailwind CSS, Chart.js.