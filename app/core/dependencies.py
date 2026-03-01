import uuid
from fastapi import Header, HTTPException

async def get_current_user_id(x_user_id: str = Header(...)) -> uuid.UUID:
    """
    Temp identity provider.
    Clients must send X-User-Id header as a UUID string

    TODO: later, this can change with JWT/OAuth without changing the route or service logic
    """

    try:
        return uuid.UUID(x_user_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid X-User-Id")
    
