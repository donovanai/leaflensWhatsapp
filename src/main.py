from fastapi import FastAPI
from src.whatsapp import router as whatsapp_router
from src.auth import router as auth_router
from src.billing import router as billing_router

app = FastAPI()

app.include_router(whatsapp_router, prefix="/whatsapp", tags=["whatsapp"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(billing_router, prefix="/billing", tags=["billing"])

@app.get("/")
def read_root():
    return {"message": "Welcome to leaflensWhatsapp"}