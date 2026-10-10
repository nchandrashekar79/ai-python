from dotenv import load_dotenv
import os
from openai import OpenAI

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

# Create a list of messages in the familiar OpenAI format

messages = [{"role": "user", "content": "Tell me a fun fact"}]


response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Tell me a fun fact"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)

print(response.choices[0].message.content)