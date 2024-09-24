"""Main module to run the application."""

from contextlib import asynccontextmanager

import uvicorn
from config import app_configs, configs
from database import Base, engine
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Create all tables in the database
Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(application: FastAPI):
    """Context manager to start and stop the application."""
    # Set up your databases and resources here.
    yield


app = FastAPI(
    **app_configs,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=configs.CORS_ORIGINS,
    allow_origin_regex=configs.CORS_ORIGINS_REGEX,
    allow_credentials=True,
    allow_methods=("GET", "POST", "PUT", "PATCH", "DELETE"),
    allow_headers=configs.CORS_HEADERS,
)


@app.get("/healthcheck", include_in_schema=False)
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=configs.HOST,
        reload=configs.ENVIRONMENT.is_debug,
        port=configs.PORT,
    )
