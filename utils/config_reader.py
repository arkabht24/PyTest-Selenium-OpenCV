from dotenv import load_dotenv
import os

# Load values from .env file
load_dotenv(dotenv_path="config/config.env")

BASE_URL = os.getenv("BASE_URL")
BROWSER = os.getenv("BROWSER")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")


