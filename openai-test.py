import requests

# Your OpenAI API key
api_key = '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'

# The endpoint for the ChatGPT API
url = 'https://api.openai.com/v1/chat/completions'

# The headers for the request
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json',
}

# The data for the request
data = {
    'model': 'gpt-4o',  # or 'gpt-4', depending on your access
    'messages': [
        {'role': 'user', 'content': 'tell me how to survive as a PhD in a good university'}
    ]
}

# Make the POST request to the API
response = requests.post(url, headers=headers, json=data)

# Print the response from the API
if response.status_code == 200:
    response_data = response.json()
    print("ChatGPT response:", response_data['choices'][0]['message']['content'])
else:
    print(f"Error: {response.status_code}")
    print(response.text)
