from dotenv import load_dotenv, find_dotenv
import os

def load_env():
    load_dotenv(dotenv_path="../.env")  

def load_emaps_api_key(ret_key=True):
    load_env()
    global api_key
    api_key = os.getenv("ELECTRICITY_MAPS_API_KEY")

    if ret_key:
        return api_key
