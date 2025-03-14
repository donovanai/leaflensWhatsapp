from src.config import SUPABASE_URL, SUPABASE_KEY
from supabase import create_client

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def increment_message_count(user_id):
    # Increment the message count for the user in the database
    pass

def check_message_limit(user_id):
    # Check if the user has reached the free message limit
    return True