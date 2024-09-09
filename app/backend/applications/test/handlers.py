from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi import status


from backend.applications.test.exceptions import PhoneError

async def phone_exception_handler_func(request: Request, exception: PhoneError):
    if exception.status_code == status.HTTP_400_BAD_REQUEST:
        return JSONResponse(
            content={"Error": exception.detail}, status_code=exception.status_code
        )


exception_handlers = {PhoneError: phone_exception_handler_func}