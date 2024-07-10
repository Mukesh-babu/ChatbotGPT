import os
from BotDefinition import OpenAIBot

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "sk-proj-CjFdiEQLTYbaGD5EQQ2KT3BlbkFJ5XRjMYDVyr6CImHmOGB2"

# Choose the model
model = "gpt-3.5-turbo"

# Create the ChatBot
try:
    chatbot = OpenAIBot(model)
except ValueError as e:
    print(f"Error initializing ChatBot: {e}")
    exit(1) 
while True:
    # Get Prompt from User
    prompt = input("You: ")

    # User can stop the chat by sending 'End Chat' as a Prompt
    if prompt.upper() == 'END CHAT':
        break

    # Generate and Print the Response from ChatBot
    response = chatbot.generate_response(prompt)
    if response:
        print(f"ChatBot: {response}")
    else:
        print("Error: Failed to generate a response.")