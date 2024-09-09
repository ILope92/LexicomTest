from fastapi import FastAPI

from backend.applications.test.routes import router as test_router
from backend.applications.test.exceptions import PhoneError
from backend.applications.test.handlers import exception_handlers

def include_routes(app: FastAPI) -> FastAPI:
    app.include_router(test_router, tags=["Test Routes"])
    return app

def add_exceptions(app: FastAPI) -> FastAPI:
    app.exception_handlers = exception_handlers
    return app