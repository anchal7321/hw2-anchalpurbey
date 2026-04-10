# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "google-genai",
# ]
# ///

import os
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Summarize the key benefits of generative AI in healthcare in 3 bullet points.",
)

print(response.text)
