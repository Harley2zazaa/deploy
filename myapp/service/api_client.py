import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("SPOONACULAR_API_KEY")

def search_recipes_by_ingredient(ingredient, number=5):
    url = "https://api.spoonacular.com/recipes/complexSearch"
    params = {
        "apiKey": api_key,
        "includeIngredients": ingredient,
        "number": number
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        return {"error": "Failed to fetch data"}
