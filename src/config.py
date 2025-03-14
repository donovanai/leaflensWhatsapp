import os
from dotenv import load_dotenv

load_dotenv()

# Configuration settings for leaflensWhatsapp

# Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Stripe
STRIPE_API_KEY = os.getenv("STRIPE_API_KEY")

# OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# WhatsApp
WHATSAPP_API_KEY = os.getenv("WHATSAPP_API_KEY")
WHATSAPP_PHONE_NUMBER = os.getenv("WHATSAPP_PHONE_NUMBER")

# General
FREE_MESSAGES_PER_DAY = 3