from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"  # Replace with your actual key
)

try:
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": "Hello"}]
    )
    print("✅ API Key works!")
    print(response.choices[0].message.content)
except Exception as e:
    print(f"❌ Error: {e}")