from fastapi import APIRouter, HTTPException, Depends
from src.config import SUPABASE_URL, SUPABASE_KEY
from supabase import create_client

router = APIRouter()

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        user = supabase.auth.api.get_user(token)
        if user:
            return user
        else:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")

@router.post("/login")
async def login(email: str, password: str):
    try:
        user = supabase.auth.sign_in(email=email, password=password)
        return user
    except Exception as e:
        raise HTTPException(status_code=400, detail="Login failed")