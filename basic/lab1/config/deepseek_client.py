from dotenv import load_dotenv

import os
from openai import OpenAI

def get_client():
    load_dotenv(override=True)
    deepseek_api_key = os.getenv('DEEPSEEK_API_KEY')

    base_url="https://api.deepseek.com"


    if deepseek_api_key:
        print(f"Deepseek API Key exists and begins {deepseek_api_key[:3]}")
    else:
        print("Deepseek API Key not set - please head to the troubleshooting guide in the setup folder")

    client = OpenAI(    
        api_key=deepseek_api_key,
        base_url=base_url)
    return client