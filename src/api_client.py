import os
import openai

def initialize_client():
    # Set up the API key and base URL
    openai.api_key = os.environ.get("cf011ac8-3e2f-41d9-9fcc-b35e3033fb90")
    openai.api_base = "https://api.sambanova.ai/v1"

    params = {}
    return openai, params

def call_api(client, prompt, params):
    try:
        # Use the client to call the API
        response = client.ChatCompletion.create(
            model=params["model"],
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1,
            top_p=0.1
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error during API call: {str(e)}")
        return None
