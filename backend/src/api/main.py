from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import habits, agents

app = FastAPI(title="HealthHabit API")

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
app.include_router(agents.router, prefix="/api/agents", tags=["agents"])


@app.get("/")
async def root():
    return {"message": "Welcome to HealthHabit API"}
