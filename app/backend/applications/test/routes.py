from typing import Optional

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from redis import asyncio as aioredis
from redis.typing import ResponseT

from backend.applications.test.schemas import WriteUpdateSchema
from backend.core.redis import get_redis
from backend.core.loader import Settings


router = APIRouter()


@router.post("/write_data")
async def write_data(
    body: WriteUpdateSchema,
    redis: aioredis.Redis = Depends(get_redis)
):
    result: Optional[bool] = await redis.setex(name=body.phone, value=body.address, time=Settings.default_time)
    return JSONResponse(content={"result": result}, status_code=status.HTTP_201_CREATED)


@router.put("/write_data")
async def write_data(
    body: WriteUpdateSchema,
    redis: aioredis.Redis = Depends(get_redis)
):
    result: Optional[bool] = await redis.setex(name=body.phone, value=body.address, time=Settings.default_time)
    return JSONResponse(content={"result": result}, status_code=status.HTTP_202_ACCEPTED)

@router.get("/check_data")
async def check_data(
    phone: str,
    redis: aioredis.Redis = Depends(get_redis)
):
    result: ResponseT = await redis.get(name=phone)
    return JSONResponse(content={"result": result}, status_code=status.HTTP_200_OK)