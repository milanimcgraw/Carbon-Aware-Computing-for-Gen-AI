import os
from dotenv import load_dotenv
from google.oauth2.service_account import Credentials

def authenticate():
    load_dotenv()

    # Load service account key from file
    key_path = "../key/prjct1-466121-beed6eec3f77.json"
    credentials = Credentials.from_service_account_file(
        key_path,
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )
    project_id = credentials.project_id
    return credentials, project_id


# Separate utility to load API key
from dotenv import load_dotenv, find_dotenv

def load_env():
    load_dotenv(find_dotenv())

def load_emaps_api_key(ret_key=True):
    load_env()
    global api_key
    api_key = os.getenv("ELECTRICITY_MAPS_API_KEY")
    if ret_key:
        return api_key

