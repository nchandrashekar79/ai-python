from xmlrpc import client

from config.deepseek_client import get_client



client = get_client()
# Create a list of messages in the familiar OpenAI format

question = "Please propose a hard, challenging question to assess someone's IQ. Respond only with the question."
messages = [{"role": "user", "content": question}]


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

