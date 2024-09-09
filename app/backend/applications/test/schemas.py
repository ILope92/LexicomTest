from pydantic import BaseModel, field_validator
from pydantic_extra_types.phone_numbers import PhoneNumber

import phonenumbers

from backend.applications.test.exceptions import PhoneError

class WriteUpdateSchema(BaseModel):
    phone: str
    address: str
    
    @field_validator("phone")
    def validate(cls, v: str):
        try:
            pn = phonenumbers.parse(v)
        except phonenumbers.phonenumberutil.NumberParseException:
            raise PhoneError('invalid phone number format')
        return phonenumbers.format_number(pn, phonenumbers.PhoneNumberFormat.E164)

class AddrResult(BaseModel):
    address: str
    

class WriteUpdateResult(BaseModel):
    result: bool