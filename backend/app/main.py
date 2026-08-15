from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.chat import router as chat_router


app = FastAPI(
    title="Government Scheme Advisor API",
    version="1.0.0"
)


# ==========================================================
# Allowed Frontend Origins
# ==========================================================

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",

    # Production frontend deployed on Vercel
    "https://ai-government-scheme-advisor-q8u1m9fu6-tamnurunithins-projects.vercel.app",
]


# ==========================================================
# CORS Configuration
# ==========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================================================
# Register API Routes
# ==========================================================

app.include_router(chat_router)


# ==========================================================
# Root Endpoint
# ==========================================================

@app.get("/")
def root():
    return {
        "message": "Government Scheme Advisor API"
    }


# ==========================================================
# Health Check
# ==========================================================

@app.get("/health")
def health():
    return {
        "status": "ok",
        "message": "Government Scheme Advisor API is running"
    }
