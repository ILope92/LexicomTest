from typing import Optional

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from redis import asyncio as aioredis
from redis.typing import ResponseT

from backend.applications.test.schemas import WriteUpdateSchema, WriteUpdateResult, AddrResult
from backend.core.redis import get_redis
from backend.core.loader import Settings


router = APIRouter()


@router.post("/write_data", response_model=WriteUpdateResult)
async def write_data(
    body: WriteUpdateSchema,
    redis: aioredis.Redis = Depends(get_redis)
) -> JSONResponse:
    """Add an entry

    Args:
        body (WriteUpdateSchema): The main body of the request
        redis (aioredis.Redis, optional): Object redis. Defaults to Depends(get_redis).

    Returns:
        JSONResponse: result write
    """
    result: Optional[bool] = await redis.setex(name=body.phone, value=body.address, time=Settings.default_time)
    return JSONResponse(content={"result": result}, status_code=status.HTTP_201_CREATED)


@router.put("/write_data", response_model=WriteUpdateResult)
async def write_data(
    body: WriteUpdateSchema,
    redis: aioredis.Redis = Depends(get_redis)
) -> JSONResponse:
    """Update the address by phone

    Args:
        body (WriteUpdateSchema): The main body of the request
        redis (aioredis.Redis, optional): Object redis. Defaults to Depends(get_redis).

    Returns:
        JSONResponse: result update
    """
    find: Optional[str] = await redis.get(name=body.phone)
    if isinstance(find, str):
        result: Optional[bool] = await redis.setex(name=body.phone, value=body.address, time=Settings.default_time)
        return JSONResponse(content={"result": result}, status_code=status.HTTP_202_ACCEPTED)

    return JSONResponse(content={"result": None}, status_code=status.HTTP_404_NOT_FOUND)

@router.get("/check_data", response_model=AddrResult)
async def check_data(
    phone: str,
    redis: aioredis.Redis = Depends(get_redis)
) -> JSONResponse:
    """Get the address by phone

    Args:
        phone (str): number phone
        redis (aioredis.Redis, optional): Object redis. Defaults to Depends(get_redis).

    Returns:
        JSONResponse: result data (address)
    """
    result: Optional[str] = await redis.get(name=phone)
    if isinstance(result, str):
        return JSONResponse(content={"result": result}, status_code=status.HTTP_200_OK)

    return JSONResponse(content={"result": None}, status_code=status.HTTP_404_NOT_FOUND)