

# Initialize the OpenAI client (automatically picks up OPENAI_API_KEY from environment)




# 1. Initialize the conversation history list
# The 'system' message sets the rules or personality of the AI



from config.deepseek_client import client_chat_conversation


conversation_history = [
    {"role": "system", "content": "You are a helpful and concise AI assistant."}
]

print("🤖 AI Chatbot Initialized! Type 'quit' or 'exit' to stop.\n")

while True:
    # 2. Get input from the user
    user_input = input("You: ")
    
    # Check if the user wants to break out of the loop
    if user_input.lower() in ['quit', 'exit']:
        print("Goodbye!")
        break
        
    # Skip empty inputs
    if not user_input.strip():
        continue

    # 3. Append the user's message to the conversation history
    conversation_history.append({"role": "user", "content": user_input})

    try:
        # 4. Send the entire history to OpenAI
    

        response = client_chat_conversation(conversation_history)
        
        # 5. Extract the AI's response text
        ai_response = response.choices[0].message.content
        print(f"\nAI: {ai_response}\n")
        
        # 6. Append the AI's response to the history so it remembers it next time
        conversation_history.append({"role": "assistant", "content": ai_response})

    except Exception as e:
        print(f"\nAn error occurred: {e}\n")
