from fastapi import APIRouter
import stripe
from src.config import STRIPE_API_KEY

router = APIRouter()

stripe.api_key = STRIPE_API_KEY

@router.post("/create-checkout-session")
async def create_checkout_session():
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': 'leaflensWhatsapp Subscription',
                },
                'unit_amount': 1000,
            },
            'quantity': 1,
        }],
        mode='subscription',
        success_url='https://your-success-url.com',
        cancel_url='https://your-cancel-url.com',
    )
    return {"id": session.id}