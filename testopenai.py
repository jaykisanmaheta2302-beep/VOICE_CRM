from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

response = client.chat.completions.create(
    model="openai/gpt-5.2",
    max_tokens=365, 
    messages=[
        {
            "role": "user",
            "content": "I spoke with customer Amit Verma today. His phone number is nine nine eight eight seven seven six six five five. He stays at 45 Park Street, Salt Lake, Kolkata. We discussed the demo and next steps. Find Phone , Address, Name and CIty"
        }
    ],
    extra_headers={
        "HTTP-Referer": "http://localhost",
        "X-Title": "OpenRouter India States Test",
    }
)

print(response.choices[0].message.content)