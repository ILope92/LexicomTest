import uvicorn
from fastapi import FastAPI

from backend.applications.routes import include_routes, add_exceptions


docs_config = {
    "docs_url": "/api/docs/",
    "redoc_url": "/api/redocs/",
    "openapi_url": "/api/docs/openapi.json",
}

app = FastAPI(**docs_config)
app = include_routes(app=app)
app = add_exceptions(app=app)


def run():
    uvicorn.run(app, host="0.0.0.0", port=8002)


if __name__ == "__main__":
    run()