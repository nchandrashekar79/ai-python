from xmlrpc import client

from config.deepseek_client import get_client



client = get_client()
# Create a list of messages in the familiar OpenAI format
system_message = {"role": "system", "content": "You are a helpful assistant"}
user_message = {"role": "user", "content": "Tell me a fun fact"}



response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        system_message,
        user_message,
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)

print(response.choices[0].message.content)

