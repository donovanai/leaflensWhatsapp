import openai
from src.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def analyze_plant_image(image):
    response = openai.Image.create(
        model="gpt-4.0-mini",
        prompt="Analyze the health of this plant and provide a description.",
        image=image
    )
    return response["choices"][0]["text"]