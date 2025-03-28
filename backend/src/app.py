from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import habits

app = FastAPI(
    title="HealthHabit API",
    description="AI-powered health habit tracking system",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(habits.router, prefix="/api/habits", tags=["habits"])


@app.get("/")
async def root():
    return {"message": "Welcome to HealthHabit API"}
