#!/usr/bin/python3
import cgi
import json
import openai
import time
# Set the appropriate headers for a CGI script
print("Content-Type: text/html")
print()

# Get the user's message from the request
form = cgi.FieldStorage()
user_message = form.getvalue('message')
openai.api_key = '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'
 # Generate response using OpenAI GPT-3
response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=user_message,
        max_tokens=50,
        temperature=1.2,
        n=1,
        stop=None
        )
print(response.choices[0].text.strip())
