from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import review, github, history
from database.connection import connect_db

app = FastAPI(title="AI Code Review Assistant", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(review.router, prefix="/api")
app.include_router(github.router, prefix="/api")
app.include_router(history.router, prefix="/api")

@app.on_event("startup")
async def startup():
    await connect_db()

@app.get("/")
async def root():
    return {"message": "AI Code Review Assistant is running"}
