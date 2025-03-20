from openai import OpenAI

API_KEY="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"
BASE_URL="https://openrouter.ai/api/v1"

client = OpenAI(api_key=API_KEY, base_url=(BASE_URL))

chat = client.chat.completions.create(
    model="deepseek/deepseek-r1:free",
    messages=[
        {
            "role": "user",
            "content": "Annualize a 3% monthly inflation rate"
        }
    ]
)

print(chat.choices[0].message.content)
