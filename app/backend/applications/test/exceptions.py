from fastapi import status


class PhoneError(Exception):
    status_code: int = status.HTTP_400_BAD_REQUEST
    
    def __init__(self, *args):
        if args:
            self.detail = args[0]
        else:
            self.detail = "invalid phone number format"

    def __str__(self):
        if self.detail:
            return 'PhoneError, {0} '.format(self.detail)
        else:
            return 'PhoneError has been raised'
        
