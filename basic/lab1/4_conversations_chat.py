from xmlrpc import client
from IPython.display import Markdown, display

from config.deepseek_client import get_client



client = get_client()
# Create a list of messages in the familiar OpenAI format

question = "Please propose a hard, challenging question to assess someone's IQ. Respond only with the question."
messages = [{"role": "user", "content": question}]

system_message = {"role": "system", "content": "You are a helpful assistant"}
user_message = {"role": "user", "content": "Tell me a fun fact"}

def client_chat(system_message, user_message):
    return client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        system_message,
        user_message,
    ],
    stream=False,
    reasoning_effort="low",
    extra_body={"thinking": {"type": "enabled"}}
)

response = client_chat(system_message, user_message)

question=response.choices[0].message.content

messages = [{"role": "user", "content": question}]

