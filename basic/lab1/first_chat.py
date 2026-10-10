from xmlrpc import client

from config.deepseek_client import get_client



client = get_client()
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

