import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

api_token = os.getenv("API_KEY")
